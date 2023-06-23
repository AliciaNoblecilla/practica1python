"""Usando los tipos de datos y sus conversiones realizar lo siguiente. (3 ptos)
Reglas:
- Pedir por consola nombre y edad de un usuario.
- Edad tiene que ser tipo entero, para esto apoyarse
  de la conversión de datos
- Identificar los tipos ingresados y mostrarlos en pantalla.
- Pedir los nombres y edades para dos trabajadores y finalmente
agregarlos a una lista. Mostrar la suma de las edades de los trabadores
localizándolos por la posición en la lista."""

nombre_usuario = input("Ingrese nombre: ")
edad_usuario = input("Ingrese edad: ")
edadconversion = int(edad_usuario)
print(type(nombre_usuario))
print(type(edad_usuario))
print(type(edadconversion))
nombre_usuario2 = input("Ingrese nombre: ")
edad_usuario2 = input("Ingrese edad: ")
edadconversion2 = int(edad_usuario2)
print(type(nombre_usuario2))
print(type(edad_usuario2))
print(type(edadconversion2))
personas = [nombre_usuario, edadconversion, nombre_usuario2, edadconversion2]
suma = personas[1] + personas[3]
print("la suma de las edades es de: {}".format(suma))
