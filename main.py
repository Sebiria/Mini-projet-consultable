from affichage import (afficher_menu_principal, afficher_liste_erreur, afficher_liste_vide,
                       afficher_liste_utilisateurs, afficher_statistiques)
from utilisateur import (ajouter_utilisateur, supprimer_utilisateur, modifier_mot_de_passe_utilisateur,
                         implementer_donnees_test)
from validation import validation_choix_fonctionnalite
from stockage import charger_utilisateurs, sauvegarder_utilisateurs

if __name__ == "__main__":
    liste_utilisateurs = charger_utilisateurs()

    while True: # Tant que le programme est en cours d'exécution
        fonctionnalite = {"1": ajouter_utilisateur,
                          "2": supprimer_utilisateur,
                          "3": modifier_mot_de_passe_utilisateur,
                          "4": afficher_liste_utilisateurs,
                          "5": afficher_statistiques,
                          "000": implementer_donnees_test}
        afficher_menu_principal()
        choix = input("Votre choix : ")
        erreurs = validation_choix_fonctionnalite(choix)
        if erreurs:
            afficher_liste_erreur(erreurs)
        elif choix == "6":
            print("\n\n💤💤💤 Fin du programme 💤💤💤")
            break
        elif choix in ("000", "1"):
            liste_utilisateurs = fonctionnalite[choix](liste_utilisateurs)
        elif choix in ("2", "3", "4", "5") and liste_utilisateurs:
            liste_utilisateurs = fonctionnalite[choix](liste_utilisateurs)
        elif choix in ("2", "3", "4", "5"):
            afficher_liste_vide()
