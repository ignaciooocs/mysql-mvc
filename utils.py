from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

# Carga las variables de entorno del archivo .env en os.environ
load_dotenv()
key = os.getenv("SECRET_KEY")

def encrypt(texto):
  f = Fernet(key)
  encrypted_text = f.encrypt(texto.encode())
  return encrypted_text

def decrypt(texto_encriptado):
  f = Fernet(key)
  decrypted_text = f.decrypt(texto_encriptado).decode()
  return decrypted_text
