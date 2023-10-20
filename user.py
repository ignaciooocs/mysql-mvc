import mysql.connector

def connect():
  try:
    connection = mysql.connector.connect(
      host="localhost", 
      user="root", 
      passwd="",
      database="db2"
    )
    print('database connected')
    return connection
  except: 
    print('Database connection error')

def create_user(conn, nombre, edad, password):
  try:
    cursor = conn.cursor()
    query = 'insert into users (nombre, edad, password) values (%s, %s, %s)'
    data = (nombre, edad, password)
    cursor.execute(query, data)
    conn.commit()
    cursor.close()
    return True
  except:
    print('Ocurrio un error al crear al usuario')
    
def get_all_users(conn):
  try:
    cursor = conn.cursor()
    cursor.execute('select * from users')
    users = cursor.fetchall()
    cursor.close()
    return users
  except:
    print('Ocurrio un error al leer los usuarios')
  
def delete_user(conn, id_usuario):
  try:
    cursor = conn.cursor()
    query = 'delete from users where id_usuario = %s'
    data = (id_usuario,)
    cursor.execute(query, data)
    conn.commit()
    cursor.close()
  except:
    print('Ocurrio un error al eliminar al usuario')
    
def update_user(conn, id, nombre, edad):
  try:
    cursor = conn.cursor()
    query = 'update users set nombre=%s, edad=%s where id_usuario = %s'
    data = (nombre, edad, id )
    cursor.execute(query, data)
    conn.commit()
    cursor.close()
  except:
    print('Ocurrio un error al actualizar al usuario')
    
def verify_user(conn):
  users=get_all_users(conn)
  if len(users) < 1:
    print("no hay usuarios registrados")
    return False
  return True

def verify_user_id(conn, id):
  users = get_all_users(conn)
  if id in [user[0] for user in users]:
    return True
  print("El usuario no existe")
  return False