import re

class miExcepcion():
    def __init__(self, mensaje):
        self.mensaje = mensaje
    def __str__(self):
        return self.mensaje

try:
    print("Introduzca un correo electrónico")
    correo = input()
    s = correo
    re.search(". * @. * \ .. *", s)
    if re.search(". * @. * \ .. *", correo):
        print("El correo es válido")
    else:
        raise miExcepcion("Podría tratarse de un ciberataque. ")
except miExcepcion as e:
    print("Excepción capturada: {}".format(e))
