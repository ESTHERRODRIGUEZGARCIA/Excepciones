import re

class Excepcion():
    def __init__(self, correo):
        self.correo = correo
    def __str__(self):
        return self.correo

try:
    print("Introduzca un correo electrónico")
    correo = input()
    s = correo
    re.search(". * @. * \ .. *", s)
    if re.search(". * @. * \ .. *", correo):
        print("El correo es válido")
    else:
        raise Excepcion("Podría tratarse de un ciberataque. ")
except Excepcion as e:
    print("Excepción capturada: {}".format(e))
