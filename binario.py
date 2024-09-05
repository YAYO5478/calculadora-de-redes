# Función para convertir de binario a decimal
def binario_a_decimal(binario):
    try:
        return int(binario, 2)
    except ValueError:
        return "Entrada no válida. Asegúrate de ingresar un número binario."

# Función para convertir de decimal a binario
def decimal_a_binario(decimal):
    try:
        return bin(int(decimal))[2:]  # bin() devuelve un string con '0b' al inicio, lo quitamos con [2:]
    except ValueError:
        return "Entrada no válida. Asegúrate de ingresar un número decimal."

# Función para convertir de hexadecimal a decimal
def hexadecimal_a_decimal(hexadecimal):
    try:
        return int(hexadecimal, 16)
    except ValueError:
        return "Entrada no válida. Asegúrate de ingresar un número hexadecimal."

# Función para convertir de decimal a hexadecimal
def decimal_a_hexadecimal(decimal):
    try:
        return hex(int(decimal))[2:]  # hex() devuelve un string con '0x' al inicio, lo quitamos con [2:]
    except ValueError:
        return "Entrada no válida. Asegúrate de ingresar un número decimal."

# Menú principal para la calculadora
def calculadora():
    while True:
        print("\n--- Calculadora de Conversión ---")
        print("1. Binario a Decimal")
        print("2. Decimal a Binario")
        print("3. Hexadecimal a Decimal")
        print("4. Decimal a Hexadecimal")
        print("5. Salir")
        
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == '1':
            binario = input("Ingresa un número binario: ")
            print(f"Binario a Decimal: {binario_a_decimal(binario)}")
        
        elif opcion == '2':
            decimal = input("Ingresa un número decimal: ")
            print(f"Decimal a Binario: {decimal_a_binario(decimal)}")
        
        elif opcion == '3':
            hexadecimal = input("Ingresa un número hexadecimal: ")
            print(f"Hexadecimal a Decimal: {hexadecimal_a_decimal(hexadecimal)}")
        
        elif opcion == '4':
            decimal = input("Ingresa un número decimal: ")
            print(f"Decimal a Hexadecimal: {decimal_a_hexadecimal(decimal)}")
        
        elif opcion == '5':
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecutar la calculadora
calculadora()
