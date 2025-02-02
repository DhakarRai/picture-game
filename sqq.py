import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Dhakar@2002',
    auth_plugin='mysql_native_password',
    database='picture_game'
)

mycursor = mydb.cursor()

def get_next_id(cursor, start_id=205):
    cursor.execute("SELECT MAX(id) FROM game_options")
    result = cursor.fetchone()[0]
    return start_id if result is None or result < start_id else result + 1

# Insert options with sequential IDs
def insert_game_option(cursor, db, question_id, option_text, start_id=205):
    next_id = get_next_id(cursor, start_id)
    
    insert_query = """
    INSERT INTO game_options (id, question_id, option_text)
    VALUES (%s, %s, %s)
    """
    values = (next_id, question_id, option_text)
    
    cursor.execute(insert_query, values)
    db.commit()
    return next_id

# mycursor.execute('''
#   CREATE TABLE IF NOT EXISTS game_questions(
#       id INT ,
#       image_path VARCHAR(255),
#       correct_answer VARCHAR(50),
#       hint VARCHAR(255)
#   )
#   ''')

mycursor.execute('''
  CREATE TABLE IF NOT EXISTS  game_options(
      id INT ,
      question_id INT,
      option_text VARCHAR(50),
      FOREIGN KEY (question_id) REFERENCES game_questions(id)
  )
  ''')

# sql = 'INSERT INTO game_questions (image_data, correct_answer, hint) VALUES(%s,%s,%s)'
# vin = ('images/apple.jpg', '41', 'sum = 90 !')
# mydb.commit()
# mycursor.execute(sql,vin)

# val = ('images/cat.jpg', '41,42,60', 'sum = 90 !')
# mydb.commit()
# mycursor.execute(sql,val)

#####################################

vin = 'INSERT INTO question_options (question_id, option_text) VALUES(%s,%s)'
# val = (41, 'solid to liquid')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (41, 'liquid to solid')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (41, 'liquid to gas')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (41, 'solid to gas')
# mycursor.execute(vin,val)
# mydb.commit()

# val = (42, 'The one in sunlight')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (42, 'The one in the dark room')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (42, 'both will grow the same')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (42, 'neither will grow')
# mycursor.execute(vin,val)
# mydb.commit()

# val = (43, 'To control breathing')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (43, 'To digest food')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (43, 'To pump blood')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (43, 'To produce energy')
# mycursor.execute(vin,val)
# mydb.commit()

# val = (44, 'food chain')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (44, 'water cycle')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (44, 'rock cycle')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (44, 'digestive system')
# mycursor.execute(vin,val)
# mydb.commit()

# val = (45, 'egg')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (45, 'butterfly')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (45, 'chrysalls')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (45, 'caterpillar')
# mycursor.execute(vin,val)
# mydb.commit()

# val = (46, '8')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (46, '6')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (46, '5')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (46, '9')
# mycursor.execute(vin,val)
# mydb.commit()


# val = (47, 'A rolling ball')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (47, 'A streched rubber')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (47, 'A battery')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (47, 'A book on a shelf')
# mycursor.execute(vin,val)
# mydb.commit()

# val = (48, 'Ruler')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (48, 'Barometer')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (48, 'Speedometer')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (48, 'Thermometer')
# mycursor.execute(vin,val)
# mydb.commit()

# val = (49, 'Stomach')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (49, 'pancreas')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (49, 'Liver')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (49, 'Small intestine')
# mycursor.execute(vin,val)
# mydb.commit()

# val = (50, 'small intestine')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (50, 'Liver')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (50, 'pancreas')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (50, 'stomach')
# mycursor.execute(vin,val)
# mydb.commit()

# val = (51, '1')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (51, '2')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (51, '3')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (51, 'none')
# mycursor.execute(vin,val)
# mydb.commit()

# val = (36, 'plastic')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (36, 'tree')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (36, 'water')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (36, 'soil')
# mycursor.execute(vin,val)
# mydb.commit()

# val = (37, '1')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (37, '7')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (37, '2')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (37, '4')
# mycursor.execute(vin,val)
# mydb.commit()

# val = (38, 'sink')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (38, 'float')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (38, 'middle')
# mycursor.execute(vin,val)
# mydb.commit()
# val = (38, 'none')
# mycursor.execute(vin,val)
# mydb.commit()

val = (53, 'H20')
mycursor.execute(vin,val)
mydb.commit()
val = (53, 'H2O2')
mycursor.execute(vin,val)
mydb.commit()
val = (53, 'HO2')
mycursor.execute(vin,val)
mydb.commit()
val = (53, '(HO)2')
mycursor.execute(vin,val)
mydb.commit()


val = (52, 'Pascal')
mycursor.execute(vin,val)
mydb.commit()
val = (52, 'Joule')
mycursor.execute(vin,val)
mydb.commit()
val = (52, 'Newton')
mycursor.execute(vin,val)
mydb.commit()
val = (52, 'Watt')
mycursor.execute(vin,val)
mydb.commit()
