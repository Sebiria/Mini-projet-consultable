from affichage import afficher_menu_principal
#from utilisateur import


if __name__ == "__main__":
    while True: # Tant que le programme est en cours d'exécution
        afficher_menu_principal()
        try:
            choix = int(input("Votre choix : "))
        except ValueError:
            print("Veuillez entrer un nombre")
        else:


            if choix == 1:
