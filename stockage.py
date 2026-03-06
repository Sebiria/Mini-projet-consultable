import json

def charger_utilisateurs():
    try:
        with open("utilisateurs.json", "r") as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        return []

def sauvegarder_utilisateurs(liste_utilisateurs):
    with open("utilisateurs.json", "w") as fichier:
        json.dump(liste_utilisateurs, fichier, indent=4)