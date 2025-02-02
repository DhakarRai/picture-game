import os
from flask import Flask, jsonify, send_file, render_template, request, redirect
import mysql.connector
from flask_cors import CORS
import boto3
from botocore.exceptions import ClientError

app = Flask(__name__)
CORS(app)

# Database configuration using environment variables
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'Dhakar@2002'),
    'database': os.getenv('DB_NAME', 'picture_game'),
    'auth_plugin': 'mysql_native_password'
}

# AWS S3 configuration
s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.getenv('AWS_SECRET_KEY')
)
BUCKET_NAME = os.getenv('S3_BUCKET_NAME')

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
    """Serve image from S3."""
    try:
        connection = get_db_connection()
        if not connection:
            return 'Database connection failed', 500
        
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT s3_key FROM game_questions WHERE id = %s', (image_id,))
        result = cursor.fetchone()
        
        if result and result['s3_key']:
            try:
                url = s3_client.generate_presigned_url('get_object',
                    Params={'Bucket': BUCKET_NAME, 'Key': result['s3_key']},
                    ExpiresIn=3600
                )
                return redirect(url)
            except ClientError as e:
                return str(e), 500
                
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
        cursor.execute('SELECT id, s3_key, correct_answer, hint FROM game_questions')
        questions = cursor.fetchall()
        
        game_data = []
        for question in questions:
            cursor.execute('SELECT option_text FROM question_options WHERE question_id = %s', (question['id'],))
            options = [option['option_text'] for option in cursor.fetchall()]
            
            # Generate presigned URL for S3 image
            image_url = s3_client.generate_presigned_url('get_object',
                Params={'Bucket': BUCKET_NAME, 'Key': question['s3_key']},
                ExpiresIn=3600
            ) if question['s3_key'] else None
            
            game_data.append({
                'image_path': image_url,
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
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
