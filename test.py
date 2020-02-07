import sys

def suma(x,y):
    return x+y

def resta(x,y):
    return x-y

def multiplica(x,y):
    return x*y

def divide(x,y):
    return x/y

def pedirNumeros():
    num1 = int(input("N1: "))
    num2 = int(input("N2: "))
    return num1, num2

def menu():
    print("--- Calculadora ---")
    print("1 - Suma")
    print("2 - Resta")
    print("3 - Multiplica")
    print("4 - Divide")
    print("5 - Salir")
    print()
    
    opcion_escogida = input("> Escoge opción: ")

    if opcion_escogida in "1234":
        num1, num2 = pedirNumeros()
        
        if opcion_escogida == "1":
            print(suma(num1,num2))

        elif opcion_escogida == "2":
            print(resta(num1,num2))

        elif opcion_escogida == "3":
            print(multiplica(num1,num2))

        elif opcion_escogida == "4":
            print(divide(num1,num2))

        elif opcion_escogida == "5":
            sys.exit()

    else:
        print("! Qué haces gilipollas no ves que no existe esta opción? XD")

while True:
    menu()