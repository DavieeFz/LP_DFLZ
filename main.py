import random
import string

def generar_contraseña(longitud):
    # Definimos los caracteres que queremos incluir en la contraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Generamos la contraseña seleccionando caracteres aleatorios
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    
    return contraseña

# Solicitamos al usuario la longitud deseada para la contraseña
longitud = int(input("Introduce la longitud de la contraseña: "))

# Generamos y mostramos la contraseña
contraseña_generada = generar_contraseña(longitud)
print("Tu nueva contraseña es:", contraseña_generada)