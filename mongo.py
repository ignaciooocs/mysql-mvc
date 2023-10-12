import pymongo

# Conexión a la base de datos
client = pymongo.MongoClient("mongodb+srv://ignaciooocs:0joc4KXQmAzLGLTz@cluster0.cr7jewn.mongodb.net/")

# Acceder a una base de datos
db = client["mongo-python"]

# Acceder a una colección (tabla)
usuarios = db["usuarios"]

# Ejemplo de inserción de un documento
usuario = {"nombre": "Ana", 
"edad": 28}
usuarios.insert_one(usuario)

# Realizar consulta
resultado = usuarios.find_one({"nombre": "Ana"})
print(resultado)

# Cerrar la conexión
client.close()

