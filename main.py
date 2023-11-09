import mysql.connector

def connect():
  try:
    connection = mysql.connector.connect(
      host="localhost", 
      user="root", 
      passwd="",
      database="bd1"
    )
    print('database connected')
    return connection
  except: 
    print('Database connection error')

def create_user(conn, nombre, edad):
  cursor = conn.cursor()
  query = 'insert into users (nombre, edad) values (%s, %s)'
  data = (nombre, edad)
  cursor.execute(query, data)
  conn.commit()
  cursor.close()
  return True
    
def get_all_users(conn):
  cursor = conn.cursor()
  cursor.execute('select * from users')
  users = cursor.fetchall()
  cursor.close()
  return users
  
def delete_user(conn, id_usuario):
  cursor = conn.cursor()
  query = 'delete from users where id_usuario = %s'
  data = (id_usuario,)
  cursor.execute(query, data)
  conn.commit()
  cursor.close()
  
def update_user(conn, id, nombre, edad):
  cursor = conn.cursor()
  query = 'update users set nombre=%s, edad=%s where id_usuario = %s'
  data = (nombre, edad, id )
  cursor.execute(query, data)
  conn.commit()
  cursor.close()

# Si la longitud de la lista users es menor a 1, devuelve un False y muestra un mensaje, y si no devuelve un True.
def verificar_usuarios(conn):
  users=get_all_users(conn)
  if len(users) < 1:
    print("no hay usuarios registrados")
    return False
  else:
    return True

# Si el id es igual al primer elemento de la lista users (el id del usuario), devuelve un True y si no un False y muestra un mensaje
def verificar_usuarios_por_id(conn, id):
  users = get_all_users(conn)
  for user in users:
    if user[0] == id:
      return True
  print("El usuario no existe")
  return False
  
def mostrar_menu():
  print("\n--- Menú ---")
  print("1. Crear usuario")
  print("2. Leer usuarios")
  print("3. Actualizar usuario")
  print("4. Eliminar usuario")
  print("5. Salir")
  
def main():
    conn=connect()
    if not conn:
      return
    while True:
        mostrar_menu()
        opcion= input("seleccione una opción: ")
        if opcion == "1":
            nombre=input("ingrese el nombre del usuario: ")
            edad=int(input("ingrese la edad el usuario: "))
            status = create_user(conn,nombre,edad)
            if status:
              print("usuario creado exitosamente")
              
        elif opcion == "2":
          #primero se verifica que existan usuarios, si no existen no entra en el if y muestra un mensaje
            verify = verificar_usuarios(conn)
            if verify:
              #si existen se muestran, sino no entra en este if
              usuarios=get_all_users(conn)
              print("\n--- usuarios ---")
              for usuario in usuarios:
                print(F"Id: {usuario[0]}, nombre: {usuario[1]}, edad: {usuario[2]}")

        elif opcion == "3":
          # Primero se verifica que existan usuarios, si no existen no entra en el if y muestra un mensaje
          verify = verificar_usuarios(conn)
          if verify:
            # si existen entra en el if, se pide el id del usuario a actualizar
            id=int(input("ingrese el id del usuario a actualizar: "))
            # Se verifica que el id exista, si no existe no entra en el if y muestra un mensaje
            id_found = verificar_usuarios_por_id(conn, id)
            if id_found:
              # Si el id existe entra en el if
              nombre=input("ingrese el nuevo nombre del usuario: ")
              edad=int(input("ingrese la edad nueva del usuario: "))
              update_user(conn, id, nombre, edad)
              print("usuario actualizado correctamente")         
            
        elif opcion == "4":
          # Primero se verifica que existan usuarios, si no existen no entra en el if y muestra un mensaje
          verify = verificar_usuarios(conn)
          if verify:  
            # si existen entra en el if, se pide el id del usuario a eliminar
            id=int(input("ingrese el ID del usuario a eliminar: "))
            # Se verifica que el id exista, si no existe no entra en el if y muestra un mensaje
            id_found = verificar_usuarios_por_id(conn, id)
            if id_found:
              # Si el id existe entra en el if
              delete_user(conn, id)
              print("usuario eliminado correctamente")
            
        elif opcion == "5":
            print("¡hasta luego!")
            break
          
        else:
            print("opcion invalida, coloque una opcion valida")
            
    conn.close()
    
if __name__ == "__main__":
    main()