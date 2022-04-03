# Excepciones
Ejercicio de Excepciones en POO - ENTREGA INDIVIDUAL

La dirección del repositorio es la siguiente: 
https://github.com/ESTHERRODRIGUEZGARCIA/Excepciones.git

Enunciado: escriba un programa que simule la conexión de un usuario a un sitio web para el que ya se ha registrado, solo con su dirección de correo electrónico (la gestión de una contraseña está fuera del alcance de esta sección). 

Este programa debe ofrecer la posibilidad al usuario de introducir una dirección de correo electrónico, y mostrará diferentes mensajes de error en función de la cadena introducida. 

El programa debe continuar si el correo electrónico indicado tiene un formato incorrecto y finalizar si no se reconoce el correo electrónico, ya que se podría tratar de un ciberataque. 

Importante: el método que analiza la cadena de caracteres no debe devolver ningún valor.

Requisitos previos:

Puede usar el módulo de expresiones regulares ofrecido por Python, para determinar si la cadena de caracteres tiene el formato correcto. Para hacerlo, importe el módulo "re" (import re) y utilice el método search() de la siguiente manera: re.search(". * @. * \ .. *", s). Esta línea devolverá None si la cadena s no tiene el formato de una dirección de correo electrónico.

El método input(’->’) le permite recopilar una cadena de caracteres escrita en la entrada estándar (la consola, en este caso).

Comportamiento esperado: la ejecución del programa en una consola se debe desarrollar de la siguiente manera:

````
vicente: $ python exceptions.py 
--> 
'' es una entrada incorrecta. Introduzca una dirección de correo 
electrónico 
--> t 
Una dirección de correo electrónico debe tener el formato xxx@xxx.xx 
--> t@t.t 
Cuenta bloqueada a causa de un ataque 
vicente: $ python exceptions.py 
--> vicente@eni.es 
¡Bienvenido Vicente! 

````

Código:

````
import re

class Excepcion():
    def __init__(self, correo): # Este atributo permite tener una información adicional sobre el motivo del desencadenamiento.
        self.correo = correo
    def __str__(self): #Para poder visualizar una excepción correctamente
        pass     # Mensaje de error que se podrá mostrar si la excepción se captura.

try:
    print("Introduzca un correo electrónico: ")
    correo = input()
    mail = correo
    s = re.search(". * @. * \ .. *", mail)
    error = s
    if error (True):
        print("El correo es válido. Bienvenido.")
    else:
        raise Excepcion(mail)

except TypeError as e:
    print(e)
    print("Cuenta bloqueada a causa de un ataque.")

finally:
    print("Gracias por usar nuestro programa.")

````
