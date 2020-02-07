import os
from datetime import datetime 
############################################################################## FUNCIONS
def entrar_dades():
    nom = input("\n> Entra el nom del treballador: ")
    cognom = input("> Entra el seu cognom: ")
    data = input("> Entra la seva data de naixement en un format DD-MM-AAAA: ")
    try:
        datetime.strptime(data, '%d-%m-%Y')
    except ValueError:
        print("Format incorrecte de data")
    with open("personal.txt", "a") as arxiu:
        arxiu.write(nom+","+cognom+","+data+"\n")
    print()

def llistar_usuaris(opcio):
    try:
        with open("personal.txt", "r") as arxiu:
            contingut = arxiu.readlines()
    except FileNotFoundError:
        print("\n! Encara no s'ha creat l'arxiu amb dades, n'has d'introduir.\n")
    else:
        if opcio == 3:
            llista_temp = []
            filtre = input("\n> Introdueix una string que contingui el nom / cognom de qui busques: ")
            for linia in contingut:
                if filtre in linia.split(",")[0] or filtre in linia.split(",")[1]:
                    llista_temp.append(linia)
            contingut = list(llista_temp)
        elif opcio == 4:
            contingut = sorted(contingut, key = lambda dada: dada[2])
        print("\n- Llista del personal:\n")
        for elem in contingut:
            print(elem, end="")
        print()

def esborrar_dades():
    try:
        os.remove("personal.txt")
    except FileNotFoundError:
        print("\n! No s'ha trobat cap arxiu que borrar.\n")
    else:
        print("\nL'arxiu ha sigut borrat correctament.\n")


############################################################################# MENU
def menu():
    executant = True
    while executant:
        # ----------------------------------------------------- | PINTAR MENU
        print("1 - Entrar dades de personal")
        print("2 - Llistar personal")
        print("3 - Llistar personal amb filtre")
        print("4 - Llistar per data de naixement")
        print("5 - Esborrar l'arxiu de dades")
        print("6 - Sortir")
        opcio = input("\n> Escull una opció: ")
        # ------------------------------------------------ | OPCIONS DEL MENU
        if opcio.isdigit():
            opcio = int(opcio)
            if opcio not in range(1,6+1):
                print("\n! Opció incorrecte. Has de triar una opció entre l'1 i el 6.\n")
            elif opcio == 1:
                entrar_dades()
            elif opcio == 2:
                llistar_usuaris(opcio)
            elif opcio == 3:
                llistar_usuaris(opcio)
            elif opcio == 4:
                llistar_usuaris(opcio)
            elif opcio == 5:
                esborrar_dades()
            elif opcio == 6:
                print("\n> Has decidit sortir.\n")
                executant = False
        else:
            print("\n! Entrada incorrecte. Has d'entrar un número per escollir una opció.\n")
    

############################################################################# PROGRAMA
menu()