import re

class Excepcion():
    def __init__(self, correo): # Este atributo permite tener una información adicional sobre el motivo del desencadenamiento.
        self.correo = correo
    def __str__(self):
        pass

try:
    print("Introduzca un correo electrónico: ")
    correo = input()
    mail = correo 
    s = re.search(". * @. * \ .. *", correo)
    if s(True):
        print("El correo es válido. Bienvenido.")
    else:
        raise Excepcion(correo)

except TypeError as e:
    print(e)
    print("Cuenta bloqueada a causa de un ataque.")

finally:
    print("Gracias por usar nuestro programa.")

