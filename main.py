#GENERADOR DE CONTRASELAS
#David LIgña
import random  # Libreria para utilizar numeros aleatorios
import string  # Libreria para coleccion de cadenas de texto

def generar_contraseña(longitud):
    # Definimos los caracteres que queremos incluir en la contraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Generamos la contraseña seleccionando caracteres aleatorios
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    
    return contraseña

while True:
    # Solicitamos al usuario la longitud deseada para la contraseña
    longitud = int(input("Introduce la longitud de la contraseña: "))
    
    # Generamos y mostramos la contraseña
    contraseña = generar_contraseña(longitud)
    print(f"Tu contraseña generada es: {contraseña}")
    
    # Preguntamos al usuario si desea generar otra contraseña
    otra = input("¿Deseas generar otra contraseña? (s/n): ").strip().lower()
    if otra != 's':
        break