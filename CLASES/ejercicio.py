import re

class Excepcion():
    def __init__(self, correo):
        self.correo = correo
    def __str__(self):      #Para poder visualizar una excepción correctamente
        return self.correo

try:
    print("Introduzca un correo electrónico: ")
    correo = input()
    s = correo
    re.search(". * @. * \ .. *", s)
    if re.search(". * @. * \ .. *", correo):
        print("El correo es válido. Bienvenido.")
    else:
        raise Excepcion(correo, " es una entrada incorrecta. Introduzca una dirección de correo electrónico. ")
    try:
        if re.search(". * @. * \ .. *", correo):
            print("El correo es válido. Bienvenido.")
        else:
            raise Excepcion("Una dirección de correo electrónico debe tener el formato xxx@xxx.xx")
    except Excepcion():
        print("Cuenta bloqueada a causa de un ataque.")

finally:
    print("Gracias por usar nuestro programa.")

