# coding: utf-8
"""
Ce fichier contient la fonction principale du jeu et s'occupe de son fonctionnement.

Il utilise les fichiers (stocké dans medias/py):
    - initialisation.py     : pour initialiser les variables de bases et les objets.
    - fonctions.py          : pour utiliser les autres fonctions du jeu
    - affichage_console.py  : pour l'affichage du jeu dans la console.

"""

#from medias.py.initialisation import *
from medias.py.fonctions import *
# from medias.py.affichage_console import *
# from time import sleep

print("Chargement du jeu...")

debug = False



def partie_de_jeu():
    """
    Principe :
        Fonction principale qui execute le jeu
    Entrée :
        Aucune
    Sortie :
        Aucune
    """
    if debug:
        print("DEBUG DIAMANTS.PY >> Lancement du jeu")

    for tour_manche in range(1, 6):
        if tour_manche == 1:
            if debug:
                print("DEBUG DIAMANTS.PY >> Création de la première manche")

            manche = creer_manche()  # On crée la manche
        else:

            if debug:
                print("DEBUG DIAMANTS.PY >> Création d'une nouvelle manche")

            # Nouvelle              Ancienne
            # |                     |

            manche = creer_manche(
                manche)  # On réadapte l'objet manche correspondant à la manche précédente pour la nouvelle manche.

        afg_lancement_manche(manche)

        while manche.manche_en_cours:

            afg_tirer_une_carte()  # Demande au joueur de tirer une carte
            manche = deploie_carte(manche)  # Déploie une carte


            if manche.manche_en_cours:  # S'il n'y a pas eu d'accident durant la manche

                decision_joueur(manche)  # Demande à chaque joueur s'il continue

                verifie_etat_jeu(manche)  # Vérifie qu'il y a encore des joueurs en jeu

    partie_terminer = importe_creer_nouvelle_manche(manche)

    fin_de_jeu(partie_terminer)


choix = None

while choix != '3':
    choix = afg_ecran_titre()
    print(choix)
    if choix == '1':
        partie_de_jeu()
    elif choix == '2':
        afg_regles()
    elif choix == '3':
        print(">> Arrêt du jeu, relancer le script pour rejouer.")
    else:
        afg_erreur(0)
