import os
############################################################################## FUNCIONS
def entrar_dades():
    usuari = input("\n> Entra el teu nom d'usuari: ")
    contrassenya = input("> Entra la teva contrassenya: ")
    with open("usuaris.txt", "a") as arxiu:
        arxiu.write(usuari+", "+contrassenya+"\n")
    print()

def llistar_usuaris():
    try:
        with open("usuaris.txt", "r") as arxiu:
            contingut = arxiu.read()
    except FileNotFoundError:
        print("\n! Encara no s'ha creat l'arxiu amb dades, n'has d'introduir.\n")
    else:
        print("\n- Llista d'usuaris:\n"+contingut)

def esborrar_dades():
    try:
        os.remove("usuaris.txt")
    except FileNotFoundError:
        print("\n! No s'ha trobat cap arxiu que borrar.\n")
    else:
        print("\nL'arxiu ha sigut borrat correctament.\n")


############################################################################# MENU
def menu():
    executant = True
    while executant:
        # ----------------------------------------------------- | PINTAR MENU
        print("1 - Entrar dades")
        print("2 - Llistar usuaris")
        print("3 - Esborrar l'arxiu de dades")
        print("4 - Sortir")
        print()
        opcio = input("> Escull una opció: ")
        # ------------------------------------------------ | OPCIONS DEL MENU
        if opcio.isdigit():
            opcio = int(opcio)
            if opcio not in range(1,4+1):
                print("\n! Opció incorrecte. Has de triar una opció entre l'1 i el 4.\n")
            elif opcio == 1:
                entrar_dades()
            elif opcio == 2:
                llistar_usuaris()
            elif opcio == 3:
                esborrar_dades()
            elif opcio == 4:
                print("\n> Has decidit sortir.\n")
                executant = False
        else:
            print("\n! Entrada incorrecte. Has d'entrar un número per escollir una opció.\n")
    

############################################################################# PROGRAMA
menu()