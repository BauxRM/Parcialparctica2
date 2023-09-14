"""Crea un programa que permita realizar operaciones matemáticas 
básicas (suma, resta, multiplicación y división) utilizando funciones modulares para cada 
operación."""

# Función para realizar una suma
def suma(a, b):
    return a + b

# Función para realizar una resta
def resta(a, b):
    return a - b

# Función para realizar una multiplicación
def multiplicacion(a, b):
    return a * b

# Función para realizar una división
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

# Menú de selección para el usuario
while True:
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    
    opcion = input("Ingrese el número de la operación deseada: ")
    
    
    if opcion == "5":
        print("¡Hasta luego!")
        break
    
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    if opcion == "1":
        resultado = suma(num1, num2)
        print(f"Resultado: {resultado}")
        input("presione Enter cualquier tecla para seguir")
    elif opcion == "2":
        resultado = resta(num1, num2)
        print(f"Resultado: {resultado}")
        input("presione Enter cualquier tecla para seguir")
    elif opcion == "3":
        resultado = multiplicacion(num1, num2)
        print(f"Resultado: {resultado}")
        input("presione Enter cualquier tecla para seguir")
    elif opcion == "4":
        resultado = division(num1, num2)
        print(f"Resultado: {resultado}")
        input("presione Enter cualquier tecla para seguir")
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1, 2, 3, 4 o 5).")
    
   
    