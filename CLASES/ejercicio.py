import re

class Excepcion():
    def __init__(self, correo): # Este atributo permite tener una información adicional sobre el motivo del desencadenamiento.
        self.correo = correo
    def __str__(self):
        return ("El correo es válido. Bienvenido.")

try:
    print("Introduzca un correo electrónico: ")
    correo = input()
    s = correo
    re.search(". * @. * \ .. *", s)
    if re.search(". * @. * \ .. *", s):
        print("El correo es válido. Bienvenido.")
    else:
        raise TypeError("Es una entrada incorrecta. Introduzca una dirección de correo electrónico. Debe tener el formato xxx@xxx.xx ")

except TypeError as e:
        print(e)
        print("Cuenta bloqueada a causa de un ataque.")

finally:
    print("Gracias por usar nuestro programa.")

