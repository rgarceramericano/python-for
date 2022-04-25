

import random
#agregar el resto del abecedario

#volver el codigo inifinito usando un while True
base="abcde1"

passw=""

#permite que el usuario seleccione la longitud de su
# password

for i in range (15):
	passw=passw+random.choice(base)
print("password ", passw)
input()
#punto extra al que logre ademas que el usuario decida cuantas contrseñas desea generar














"""   
for i in range(3):
	print("reprobades")
	input("ingresa tu nombre: ")

for g in ("hola"):
	print(g)

for d in ["manzana","pera","reprobados","mucha tarea"]:
	print(d)

import random
#agregar el resto del abecedario
base="abcde"

"""
print("            DESAFIO                  ")
passw=""
#permite que el usuario seleccione la longitud de su
# password
x=int(input("selecciona la cantidad de passwords: "))
y=int(input("selecciona la longitud del password: "))

for passwords in range (x):
	for i in range (y):
		passw=passw+random.choice(base)

	
	print("password ",passwords, passw)
	passw=""
		

#punto extra al que logre ademas que el usuario decida cuantas contrseñas desea generar





