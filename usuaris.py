usuari = input("Entra el teu nom d'usuari: ")
contrassenya = input("Entra la teva contrassenya: ")
with open("dades.txt", "a") as arxiu:
    arxiu.write(usuari+","+contrassenya+"\n")