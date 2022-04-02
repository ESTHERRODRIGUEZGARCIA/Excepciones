import re
s = correo
re.search(". * @. * \ .. *", s)
print("Introduzca un correo electrónico")
correo = input()
if re.search(". * @. * \ .. *", correo):
    print("El correo es válido")
else:
    print("Podría tratarse de un ciberataque. ")
