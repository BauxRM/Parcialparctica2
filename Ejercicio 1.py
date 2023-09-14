"""Crea un programa en python que permita convertir 
entre Celsius y Fahrenheit. Crea dos funciones modulares: una para convertir de Celsius a 
Fahrenheit y otra para convertir de Fahrenheit a Celsius."""

# Función para convertir de Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Función para convertir de Fahrenheit a Celsius
def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Menú de selección para el usuario
while True:
    print("Selecciona una opción:")
    print("1. Convertir de Celsius a Fahrenheit")
    print("2. Convertir de Fahrenheit a Celsius")
    print("3. Salir")
    
    opcion = input("Ingrese el número de la opción deseada: ")
    
    if opcion == "1":
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        fahrenheit = celsius_a_fahrenheit(celsius)
        print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
    elif opcion == "2":
        fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
        celsius = fahrenheit_a_celsius(fahrenheit)
        print(f"{fahrenheit} grados Fahrenheit son {celsius} grados Celsius.")
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1, 2 o 3).")

    