import re

print("Introduzca un correo electrónico")
correo = input()
s = correo
re.search(". * @. * \ .. *", s)
if re.search(". * @. * \ .. *", correo):
    print("El correo es válido")
else:
    print("Podría tratarse de un ciberataque. ")
