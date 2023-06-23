"""Usando el concepto y funciones de listas, realizar un programa con
las siguiente características (3 ptos):
Reglas:
- Crear una lista con 10 valores random o aleatorios (Pista: Usar el método
append y for)
- Llenar otra lista con sus cubos.
- Llenar una lista nueva con sus cuadrados.
- Mostrar de manera inversa la suma de ambas listas creadas."""

import random
list1 = []
list_2 = []
list_3 = []

for _ in range(10):

 list1.append(random.randint(1, 10))
list_2 = [num ** 3 for num in list1]
list_3 = [num ** 2 for num in list1]
inversa = list(reversed(list_2 + list_3))

print(" mi lista inicial es de:", list1)
print(" mi lista elevado al cubo es de:", list_2)
print(" mi lista elevado al cuadrado es de:", list_3)
print("La suma inversa es de:", inversa)