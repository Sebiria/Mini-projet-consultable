from affichage import afficher_menu_principal, afficher_liste_erreur, afficher_liste_vide
from utilisateur import ajouter_utilisateur
from validation import validation_choix_fonctionnalite


if __name__ == "__main__":
    liste_utilisateurs = []

    while True: # Tant que le programme est en cours d'exécution
        print(liste_utilisateurs)
        afficher_menu_principal()
        choix = input("Votre choix : ")
        erreurs = validation_choix_fonctionnalite(choix)
        if erreurs:
            afficher_liste_erreur(erreurs)
        else:


            #ACCES AUX FONCTIONNALITES

            if choix == "1": # Ajouter un utilisateur
                liste_utilisateur = ajouter_utilisateur(liste_utilisateurs)

            elif not liste_utilisateurs:
                afficher_liste_vide()
            else:

                #if choix == "2":  # Ajouter un utilisateur


                #if choix == "3":  # Ajouter un utilisateur


                #if choix == "4":  # Ajouter un utilisateur


                #if choix == "5":  # Ajouter un utilisateur


                if choix == "6":  # Ajouter un utilisateur
                    break

                #if choix == "000":
