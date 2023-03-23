# Fichier de test de la classe Manche

from medias.py.initialisation import *

deck = {1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 7: 2, 9: 1, 11: 2, 13: 1, 14: 1, 15: 1, 17: 1, "araignées": 3, "serpents": 3,
        "laves": 3, "boulets": 3, "béliers": 3, "relique": 5}

#Joueurs
olive = Joueurs(0, "Olivier")
tom = Joueurs(1, "Thomas")
sacha = Joueurs(2, "Satoshi")
l_joueurs = [olive, tom, sacha]


def test_set_ajoute_enleve_carte_banc():
    manche = Manche(deck, l_joueurs)
    manche.set_ajoute_carte_banc("araignées")
    assert "araignées" in manche.banc
    print(manche.banc)

    manche.set_enleve_carte_banc("araignées", 1)
    assert "araignées" not in manche.banc


def test_set_enleve_carte_deck():
    manche = Manche(deck, l_joueurs)
    nb_de_5 = manche.deck[5]
    manche.set_enleve_carte_deck(5)
    assert manche.deck[5] == nb_de_5 - 1

    manche.set_enleve_carte_deck('5')
    assert manche.deck[5] == nb_de_5 - 2

    nb_de_relique = manche.deck["relique"]
    manche.set_enleve_carte_deck("relique")
    assert manche.deck["relique"] == nb_de_relique - 1


def test_set_ajoute_enleve_diamant_tresor():
    manche = Manche(deck, l_joueurs)
    manche.set_ajoute_diamant_tresor(125)
    assert manche.reste_tresor == 125
    manche.set_enleve_diamant_tresor(25)
    assert manche.reste_tresor == 100

def test_set_ajoute_relique_sortie():
    manche = Manche(deck, l_joueurs)
    manche.set_ajoute_relique_sortie(2)
    manche.set_ajoute_relique_sortie(3)

    assert manche.nb_relique_sortie == 5
    print(manche.nb_relique_sortie)

    # La ligne suivante fait afficher un message d'erreur, ce qui est normal.
    # manche.set_ajoute_relique_sortie()

# test_set_ajoute_enleve_carte_banc()
# test_set_enleve_carte_deck()
# test_set_ajoute_enleve_diamant_tresor()
#test_set_ajoute_relique_sortie()

def test_set_etat_joueur_dans_la_manche():
    manche = Manche(deck, l_joueurs)

    manche.etat_joueurs_dans_la_manche[0] == "En_Jeu"
    manche.set_etat_joueur_dans_la_manche(0, "Sortie")
    manche.etat_joueurs_dans_la_manche[0] == "Sortie"
    manche.set_etat_joueur_dans_la_manche(0, "En_Jeu")
    manche.etat_joueurs_dans_la_manche[0] == "En_Jeu"



def test_execute_carte_tresor():
    olive = Joueurs(0, "Olivier")
    tom = Joueurs(1, "Thomas")
    sacha = Joueurs(2, "Satoshi")
    manche = Manche(deck, [olive, tom, sacha])

    carte = manche.tirage_de_carte(5)
    assert carte == 5

    carte = manche.tirage_de_carte("relique")
    assert carte == "relique"
    print(carte)


# test_set_etat_joueur_dans_la_manche()
# test_execute_carte_tresor()