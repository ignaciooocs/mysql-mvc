import mysql.connector


def connect():
  connection = mysql.connector.connect(
    host="localhost", 
    user="root", 
    passwd="",
    database="db2"
  )
  return connection

def create_user(conn, nombre, edad):
  cursor = conn.cursor()
  query = 'insert into users (nombre, edad) values (%s, %s)'
  data = (nombre, edad)
  cursor.execute(query, data)
  conn.commit()
  cursor.close()
  
def get_all_users(conn):
  cursor = conn.cursor()
  cursor.execute('select * from users')
  users = cursor.fetchall()
  for user in users:
    print(user)
  cursor.close()
  
def delete_user(conn, id_usuario):
  cursor = conn.cursor()
  query = 'delete from users where id_usuario = %s'
  data = (id_usuario,)
  cursor.execute(query, data)
  conn.commit()
  cursor.close()
  
def update_user(conn, nombre, edad, id):
  cursor = conn.cursor()
  query = 'update users set nombre=%s, edad=%s where id_usuario = %s'
  data = (nombre, edad, id )
  cursor.execute(query, data)
  conn.commit()
  cursor.close()
  
  
connection = connect()
update_user(connection, "Juan", 32, 11)
# create_user(connection, "Pablo", 12)   
# delete_user(connection, 10)
get_all_users(connection)

connection.close()


