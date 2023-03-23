# Fichier de test de la classe Joueur

from medias.py.initialisation import Joueurs
'''
# appending the parent directory path
sys.path.append('..')

# importing the methods
from initialisation import *
'''
def test_ajout_inv_manche():
    olive = Joueurs(0, "Olivier")
    # On teste l'ajout de diamants
    assert olive.inv_manche == 0
    olive.set_ajout_inv_manche(989)
    assert olive.inv_manche == 989
    olive.set_ajout_inv_manche(0)
    assert olive.inv_manche == 989
    olive.set_ajout_inv_manche()
    assert olive.inv_manche == 990


def test_plantage_ajout_inv_manche(x):
    olive = Joueurs(0, "Olivier")
    # On vérifie que la fonction renvoie un message d'erreur

    if x == 0: olive.set_ajout_inv_manche(-5)
    if x == 1: olive.set_ajout_inv_manche("pomme")
    if x == 2: olive.set_ajout_inv_manche('5')


def test_reset_inv_manche():
    olive = Joueurs(0, "Olivier")
    olive.set_ajout_inv_manche(9)
    olive.set_reset_inv_manche()
    assert olive.inv_manche == 0


def test_ajout_inv_partie():
    olive = Joueurs(0, "Olivier")
    # On teste l'ajout de diamants
    assert olive.inv_partie == 0
    olive.set_ajout_inv_partie(989)
    assert olive.inv_partie == 989
    olive.set_ajout_inv_partie(0)
    assert olive.inv_partie == 989
    olive.set_ajout_inv_partie()
    assert olive.inv_partie == 990


def test_plantage_ajout_inv_partie(x):
    olive = Joueurs(0, "Olivier")
    # On vérifie que la fonction renvoie un message d'erreur

    if x == 0: olive.set_ajout_inv_partie(-5)
    if x == 1: olive.set_ajout_inv_partie("pomme")
    if x == 2: olive.set_ajout_inv_partie('5')


def test_set_etat():
    olive = Joueurs(0, "Olivier")
    nouv_etat = "Sortie" if olive.etat == "En_Jeu" else "En_Jeu"
    olive.set_etat(nouv_etat)
    assert olive.etat == nouv_etat

    nouv_etat = "Sortie" if olive.etat == "En_Jeu" else "En_Jeu"
    olive.set_etat(nouv_etat)
    assert olive.etat == nouv_etat


def test_preparatif_nouvelle_manche():
    olive = Joueurs(0, "Olivier")
    olive.set_ajout_inv_manche(222)
    olive.set_ajout_inv_partie(78)
    olive.set_etat("Sortie")

    olive.preparatif_nouvelle_manche(True)

    assert olive.inv_manche == 0
    assert olive.inv_partie == 300
    assert olive.etat == "En_Jeu"

    olive.preparatif_nouvelle_manche(False)

    assert olive.inv_manche == 0
    assert olive.inv_partie == 300
    assert olive.etat == "En_Jeu"



# test_ajout_inv_manche()
# test_plantage_ajout_inv_manche(0)
# test_reset_inv_manche()
# test_ajout_inv_partie()
# test_plantage_ajout_inv_partie(2)
# test_set_etat()
test_preparatif_nouvelle_manche()
