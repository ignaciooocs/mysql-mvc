from utils import encrypt, decrypt

def mostrar_menu():
  print("\n--- Menú ---")
  print("1. Crear usuario")
  print("2. Leer usuarios")
  print("3. Actualizar usuario")
  print("4. Eliminar usuario")
  print("5. Salir")
  
def get_data_user():
  nombre=input("ingrese el nombre del usuario:")
  edad=int(input("ingrese la edad el usuario:"))
  password = input("ingrese la contraseña del usuario:")
  hash_password = encrypt(password)
  return nombre ,edad ,hash_password

def data_update():
  nombre=input("ingrese el nombre del usuario:")
  edad=int(input("ingrese la edad el usuario:"))
  return nombre, edad

def show_users(users):
  print("\n--- usuarios ---")
  for usuario in users:
    password = decrypt(usuario[3])
    print(F"Id: {usuario[0]}, nombre: {usuario[1]}, edad: {usuario[2]}, password: {password}")
    
def get_id ():
  return int(input("ingrese el id del usuario:"))

def confirm_delete():
  return input(f'¿Estas seguro que deseas eliminar el usuario? Si/No ').capitalize()

def message(message):
  print(message)
  