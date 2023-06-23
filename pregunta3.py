"""
Teniendo presente el uso y concepto de diccionarios en Python, realizar un
programa con los siguientes requerimientos (4 ptos)
Reglas:
- Crear un diccionario con los keys de nombre, apellidos, edad y dni.
- Pedir por consola los valores para estos keys.
- Mostrar en pantalla sólo los values del diccionario
- Agregar un key adicional con el nombre de “profesion” y un valor para este key
nuevo.
- Eliminar el key dni y mostrar el nuevo diccionario."""

dicc_1 = {"nombre": input("Ingresar su nombre: "),
          "apellidos": input("Ingrese los apellidos: "),
           "edad": int(input("Ingrese la edad: ")),
          "dni": int(input("Ingrese el DNI: "))}
for value in dicc_1.values():
    print("los datos actuales son : {}".format(value))
dicc_1["profesion"] = input("Ingrese la profesión: ")
del dicc_1["dni"]
for value in dicc_1.values():
    print("los datos actualizados son : {}".format(value))