# BasicMath: Operaciones matemáticas básicas
# Objetivo: Practicar ingreso de datos

# Función que realiza operaciones matemáticas simples
def basic_math_operations(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2
    exponentiation = num1 ** num2
    modulo = num1 % num2

    print(f"Suma: {num1} + {num2} = {addition}")
    print(f"Resta: {num1} - {num2} = {subtraction}")
    print(f"Multiplicación: {num1} * {num2} = {multiplication}")
    print(f"División: {num1} / {num2} = {division}")
    print(f"Potencia: {num1} ** {num2} = {exponentiation}")
    print(f"Modulo: {num1} % {num2} = {modulo}")
# end basic_math_operations(num1, num2):


# Main function, toma los datos y llama a las funciones 
# usa input para el ingreso de datos
# float los convierte en números de punto flotante
def main():
    try:
        num1 = float(input("Ingrese el operador 1: "))
        num2 = float(input("Ingrese el operador 2: "))

        basic_math_operations(num1, num2)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
# end main()

# llamada
main()
