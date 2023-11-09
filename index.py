from user import connect, create_user, get_all_users, update_user, delete_user, verify_user, verify_user_id
from vista import get_data_user, get_id, show_users, message, data_update, confirm_delete, mostrar_menu
  
def main():
  conn = connect()
  if not conn:
    return
  while True:
      mostrar_menu()
      opcion= input("seleccione una opción :")
      if opcion == "1":
          nombre, edad, hash_password = get_data_user()
          status = create_user(conn,nombre,edad, hash_password)
          if status:
            message("usuario creado exitosamente")
          
      elif opcion == "2":
          verify = verify_user(conn)
          if verify:
            users=get_all_users(conn)
            show_users(users)

      elif opcion == "3":
        verify = verify_user(conn)
        if verify:  
          id = get_id()
          id_found = verify_user_id(conn, id)
          if id_found:
            nombre, edad = data_update()
            update_user(conn, id, nombre, edad)
            message("usuario actualizado correctamente")         
          
      elif opcion == "4":
        verify = verify_user(conn)
        if verify:  
          id = get_id()
          id_found = verify_user_id(conn, id)
          if id_found:
            confirm = confirm_delete()
            if confirm == 'Si':
              delete_user(conn, id)
              message("usuario eliminado correctamente")
            elif confirm == 'No':
              message('No se eliminó el usuario')
            else:
              message('Opcion ingresada no valida')
          
      elif opcion == "5":
          message("¡hasta luego!")
          break
        
      else:
          message("opcion invalida, coloque una opcion valida")
          
  conn.close()
    
if __name__ == "__main__":
    main()