"""Escribe un programa en Python que realice una búsqueda de un número 
dado, en un arreglo. Crea una función modular para llevar a cabo la búsqueda"""

# Función para buscar un número en un arreglo
def buscar_numero(arreglo, numero):
    for elemento in arreglo:
        if elemento == numero:
            return True
    return False

# Arreglo de ejemplo
arreglo = [10, 22, 55, 66, 75]

# Número que deseamos buscar
numero_a_buscar = int(input("ingrese el numero que desea buscar: "))

# Llamar a la función para buscar el número en el arreglo
resultado = buscar_numero(arreglo, numero_a_buscar)

# Verificar el resultado de la búsqueda
if resultado:
    print(f"El número {numero_a_buscar} fue encontrado en el arreglo.")
else:
    print(f"El número {numero_a_buscar} no fue encontrado en el arreglo.")
