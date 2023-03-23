# Fichier qui teste l'affichage

from medias.py.initialisation import Joueurs, Manche
from medias.py.affichage_console import *

deck = {1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 7: 2, 9: 1, 11: 2, 13: 1, 14: 1, 15: 1, 17: 1, "araignées": 3, "serpents": 3,
            "laves": 3, "boulets": 3, "béliers": 3, "relique": 5}

olive = Joueurs(0, "Olivier")
tom = Joueurs(1, "Thomas")
sacha = Joueurs(2, "Satoshi")
l_j = [olive, tom, sacha]

tom.set_ajout_inv_manche(2000)
sacha.set_ajout_inv_manche(5)




def test_afg_lancement_manche():
    manche = Manche(deck, l_j)
    afg_lancement_manche(manche)

    manche = Manche(deck, l_j, 2)
    manche.set_ajout_liste_manche_reussite_ou_non(True)
    afg_lancement_manche(manche)

    manche = Manche(deck, l_j, 2)
    manche.set_ajout_liste_manche_reussite_ou_non(False)
    afg_lancement_manche(manche)

    manche = Manche(deck, l_j, 3)
    manche.set_ajout_liste_manche_reussite_ou_non(True)
    manche.set_ajout_liste_manche_reussite_ou_non(True)
    afg_lancement_manche(manche)

    manche = Manche(deck, l_j, 3)
    manche.set_ajout_liste_manche_reussite_ou_non(False)
    manche.set_ajout_liste_manche_reussite_ou_non(True)
    afg_lancement_manche(manche)

    manche = Manche(deck, l_j, 3)
    manche.set_ajout_liste_manche_reussite_ou_non(False)
    manche.set_ajout_liste_manche_reussite_ou_non(False)
    afg_lancement_manche(manche)

#test_afg_lancement_manche()

def test_afg_accident_danger_fin_manche():
    afg_accident_danger_fin_manche("laves","Robert",255)
    afg_accident_danger_fin_manche("boulets", "Jean", 25)
    afg_accident_danger_fin_manche("béliers", "Michel", 2)
    afg_accident_danger_fin_manche("serpents", "Augustin", 55)
    afg_accident_danger_fin_manche("araignées", "Machin", 85252542)

#test_afg_accident_danger_fin_manche()