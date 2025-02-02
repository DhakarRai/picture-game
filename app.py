import os
from flask import Flask, jsonify, send_file, render_template, request
import mysql.connector
from flask_cors import CORS
import io

app = Flask(__name__)
CORS(app)

# Database configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'Dhakar@2002'),
    'database': os.getenv('DB_NAME', 'picture_game'),
    'auth_plugin': 'mysql_native_password'
}

def get_db_connection():
    """Create database connection."""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except mysql.connector.Error as err:
        print(f"Database Connection Error: {err}")
        return None

@app.route('/test_connection')
def test_connection():
    """Test database connectivity."""
    connection = get_db_connection()
    if connection:
        connection.close()
        return "Database connection successful!", 200
    return "Database connection failed", 500

@app.route('/game_image/<int:image_id>')
def serve_image(image_id):
    """Serve image from database."""
    try:
        connection = get_db_connection()
        if not connection:
            return 'Database connection failed', 500

        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT image_data FROM game_questions WHERE id = %s', (image_id,))
        result = cursor.fetchone()

        if result and result['image_data']:
            return send_file(
                io.BytesIO(result['image_data']), 
                mimetype='image/jpeg', 
                as_attachment=False,
                download_name=f"image_{image_id}.jpg"
            )
        
        return 'Image not found', 404

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

@app.route('/get_game_data')
def get_game_data():
    """Fetch game data."""
    try:
        connection = get_db_connection()
        if not connection:
            return jsonify({'error': 'Database connection failed'}), 500

        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT id, correct_answer, hint FROM game_questions')
        questions = cursor.fetchall()
        
        game_data = []
        for question in questions:
            cursor.execute('SELECT option_text FROM question_options WHERE question_id = %s', (question['id'],))
            options = [option['option_text'] for option in cursor.fetchall()]
            
            game_data.append({
                'image_path': f"/game_image/{question['id']}", 
                'correct_answer': question['correct_answer'], 
                'options': options, 
                'hint': question['hint']
            })
        
        return jsonify(game_data)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

@app.route('/')
def index():
    """Render main page."""
    return render_template('iiii.html')

if __name__ == "__main__":
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
