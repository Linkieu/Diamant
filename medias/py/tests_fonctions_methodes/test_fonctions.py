# Fichier de tests des fonctions de fonctions.py

# Certaines ont été épargnés, car on a jugé qu'elles n'étaient pas intéressante à placer dans ce fichier,


from medias.py.fonctions import *

deck = {1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 7: 2, 9: 1, 11: 2, 13: 1, 14: 1, 15: 1, 17: 1, "araignées": 3, "serpents": 3,
            "laves": 3, "boulets": 3, "béliers": 3, "relique": 5}

def test_calcul_scoreboard():
    for i in range(500):
        olive = Joueurs(0, "Olivier")
        tom = Joueurs(1, "Thomas")
        sacha = Joueurs(2, "Satoshi")
        sachaa = Joueurs(3, "Sato")
        yo = Joueurs(4,"Yoplay")
        l_j = [olive, tom, sacha, sachaa, yo]  # liste joueurs

        jsp = [randint(0,255) for i in range(5)]  # Valeurs distribuées aux objets
        print(jsp)
        olive.set_ajout_inv_partie(jsp[0])
        tom.set_ajout_inv_partie(jsp[1])
        sacha.set_ajout_inv_partie(jsp[2])
        sachaa.set_ajout_inv_partie(jsp[3])
        yo.set_ajout_inv_partie(jsp[4])

        olivier = Manche(deck, l_j)

        jerome = scoreboard(olivier)  # test du scoreboard

        #for i in jerome:
        #    print(i.inv_partie)

        assert jerome[0].inv_partie <= jerome[1].inv_partie <= jerome[2].inv_partie <= jerome[3].inv_partie <= jerome[4].inv_partie, "ERREUR >> Ce n'est pas trié !"

#test_calcul_scoreboard()

def test_importation_manche():
    deck = {1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 7: 2, 9: 1, 11: 2, 13: 1, 14: 1, 15: 1, 17: 1, "araignées": 3, "serpents": 3,
            "laves": 3, "boulets": 3, "béliers": 3, "relique": 1}

    olive = Joueurs(0, "Olivier")
    tom = Joueurs(1, "Thomas")
    sacha = Joueurs(2, "Satoshi")
    sachaa = Joueurs(3, "Sato")
    yo = Joueurs(4, "Yoplay")
    l_j = [olive, tom, sacha, sachaa, yo]  # liste joueurs

    manche = Manche(deck, l_j)

    manche.set_ajoute_relique_sortie(2)
    manche.set_ajoute_dangers_a_retirer("laves")
    manche.set_ajoute_dangers_a_retirer("boulets")
    manche.set_ajout_liste_manche_reussite_ou_non(True)

    manche2 = importe_creer_nouvelle_manche(manche)

    assert manche2.no_manche != manche.no_manche
    assert manche2.nb_relique_sortie == manche.nb_relique_sortie
    assert manche2.dangers_a_retirer == manche.dangers_a_retirer
    assert manche2.liste_manche_reussite_ou_non == manche.liste_manche_reussite_ou_non
    assert manche2.liste_joueurs_dans_la_manche == manche.liste_joueurs_dans_la_manche

#test_importation_manche()