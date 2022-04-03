import re

class Excepcion():
    def __init__(self, correo):
        self.correo = correo
    def __str__(self):
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
        re.search(". * @. * \ .. *", s)
        if re.search(". * @. * \ .. *", correo):
            print("El correo es válido. Bienvenido.")
        else:
            raise Excepcion(" Cuenta bloqueada a causa de un ataque.")
    
