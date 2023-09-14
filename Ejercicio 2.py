"""Escribe un programa en Python que encuentre y 
muestre todos los números primos dentro de un rango dado. Utiliza una función modular 
para determinar si un número es primo. """

# Función para verificar si un número es primo
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Entrada de usuario para el rango
inicio = int(input("Ingrese el inicio del rango: "))
fin = int(input("Ingrese el final del rango: "))

# Bucle para encontrar y mostrar los números primos en el rango
print(f"Números primos en el rango de {inicio} a {fin}:")
for numero in range(inicio, fin + 1):
    if es_primo(numero):
        print(numero)
