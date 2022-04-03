import re

class miExcepcion(Excepcion):
    def __init__(self, correo): # Este atributo permite tener una información adicional sobre el motivo del desencadenamiento.
        self.correo = correo
    def __str__(self):      #Para poder visualizar una excepción correctamente
        return self.correo  # Mensaje de error que se podrá mostrar si la excepción se captura.

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
    except Excepcion as e:
        print(e)
        print("Cuenta bloqueada a causa de un ataque.")

finally:
    print("Gracias por usar nuestro programa.")

