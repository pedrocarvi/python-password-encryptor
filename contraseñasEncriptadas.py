# Modulos
from cryptography.fernet import Fernet
import cv2
import sys


# Intro Programa
print("###################################################################################################")
print("##### ¡Bienvenido! Con nuestro programa vas a poder guardar tus contraseñas de manera segura  #####")
print("###################################################################################################\n")
print("")


# CRYPTOGRAPHY 
def write_key():
    key = Fernet.generate_key();
    with open ("key.key", "wb") as keyfile:
        keyfile.write(key)

def load_key():
    archivo = open("key.key", "rb");
    key = archivo.read();
    archivo.close();
    return key

key = load_key()
fer = Fernet(key)


# CONTRASEÑA MAESTRA
contador = 0
while contador < 3:
    contraseñaMaestra = input("Ingrese la contraseña maestra: ")
    
    if contraseñaMaestra == "pwMaestra":
        print("")
        break
    else:
        print("Prueba", contador+1, ".Intente nuevamente");
        contador = contador + 1
        
        if contador == 3:
            # CV2 
            cap = cv2.VideoCapture(0)
            leido, frame = cap.read();
            cv2.imwrite("captura.png", frame)
            cap.release()
            sys.exit()


# FUNCIONES DEL PROGRAMA -----
# Funcion para ver las contraseñas guardadas sin encriptar
def ver():
    with open('contraseñas.txt', 'r') as archivo:
        for data in archivo.readlines():
            cuenta, usuario, contraseña = data.split("|")
            print("Cuenta:", cuenta, "- Usuario:", usuario, "- Contraseña:", fer.decrypt(contraseña.encode()).decode())
    
    print("")
# Funcion para agregar nuevas contraseñas.
def agregar():
    cuenta = input("Cuenta a guardar: ");
    nombreUsuario = input("Nombre de usuario o Email: ");
    contraseña = input("Contraseña: ");

    with open('contraseñas.txt', 'a') as archivo:
        archivo.write(cuenta + "|" + nombreUsuario + "|" + fer.encrypt(contraseña.encode()).decode() + "\n")

    print("")



# Mensaje para que el usuario entienda el funcionamiento del programa.
print("Escriba: \n'ver' para ver una cuenta ya registrada, \n'agregar' para agregar una nueva, \n'salir' para salir del programa, \n")


# PEDIDO DE LA ACCION Y LLAMADA DE LAS FUNCIONES -----
while True:

    accion = input("Accion: ");
    accion = accion.lower()

    if accion == "ver":   
        ver();

    elif accion == "agregar":        
        agregar();

    elif accion == "salir":
        break
    
    else:
        print("Escriba correctamente la accion a realizar. (ver / agregar / salir)")
        continue