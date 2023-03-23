"""
Ce fichier contient les fonctions secondaires.

Il est utilisé par le fichier Diamants.py.
"""
from medias.py.initialisation import *
# from medias.py.affichage_console import *
from random import *

global mode

print("Chargement des composants 2/2 du jeu...")


def mode_affichage():
    """
    #Note : S'exécute dès le lancement de ce script.

    Principe :
        Petit affichage sur console qui demande avec quel mode d'affichage on souhaite lancer le jeu

            OPTION 1 : Mode Graphique
            OPTION 2 : Mode Console

        Le choix de l'utilisateur est pris en compte par un input().

        En fonction du résultat, soit affichage_fenetre.py sera chargé, soit (par défaut) affichage_console.py.

        Note : les fonctions des 2 modes possèdent les MÊMES nom !
    Entrée :
        Aucune
    Sortie:
        Aucune
    """

    choix = None

    print("\n\n\n")
    while choix == None:
        print("Pour lancer le jeu, vous devez sélectionner l'un des modes suivants:")
        print("OPTION 1 [TOUCHE: A]: Mode Graphique")
        print("OPTION 2 [TOUCHE: B]: Mode Console\n")
        choix = input("Quel est votre choix ? [touche A (OU) B]\n> ")

        if choix in ['A','a']:
            return "GRAPHIQUE"
        elif choix in ['B','b']:
            return "CONSOLE"
        else:
            print("\n\n\nERREUR >> Impossible de lancer le jeu si vous ne sélectionner pas le mode !")
            print("          Veuillez sélectionner un mode pour continuer...\n")
            choix = None


mode_pour_jouer = mode_affichage()


if mode_pour_jouer == "CONSOLE":
    from medias.py.affichage_console import *
    print("MODE D'AFFICHAGE: Interface console")
elif mode_pour_jouer == "GRAPHIQUE":
    from medias.py.affichage_graphique import *
    ouvrir_affichage()
    print("MODE D'AFFICHAGE: Interface graphique")











def creer_joueur():
    """
    Principe :
        Demande le nombre de joueurs qui vont jouer, puis créer un à un les joueurs.

        La fonction demande le pseudonyme de chaque joueur pour créer un objet qui lui sera associé.
        Chaque joueur sera différencié par un identifiant unique "no_joueur".
        Cet identifiant représente l'emplacement du joueur dans la liste liste_joueur

        Il ajoute les joueurs dans liste_joueurs et ajuste ensuite la taille de la liste decision_joueurs.

    À quel moment est appelée cette fonction ? :
        Au lancement du jeu, avant la première manche.
    Entrée :
        Aucune
    Sortie :
        liste_joueurs       [LIST > JOUEURS] : Liste contenant les objets de type Joueurs.
    """

    # Demande le nombre de joueurs participant à la partie         3 <= nb_joueur <= 8

    valide_nbr_joueur = False  # Indique si l'utilisateur a entré une valeur attendue.
    nbr_joueur = 0
    pseudo = "MISSINGNO."

    while not valide_nbr_joueur:
        nbr_joueur = afg_creer_joueur_demande_nbjoueurs()

        if type(nbr_joueur) == str:
            if nbr_joueur.isdigit():  # Si c'est un nombre au format texte
                nbr_joueur = int(nbr_joueur)  # Conversion

        # Vérification de la validité de la valeur
        if type(nbr_joueur) == int:
            valide_nbr_joueur = True if 3 <= nbr_joueur <= 8 else False

    # Création des joueurs
    liste_joueurs = []
    for no_joueur in range(nbr_joueur):

        pseudo_valide = False
        while not pseudo_valide:  # Tant que le pseudonyme du joueur n'est pas valide (ou n'existe pas).
            pseudo = afg_creer_joueur_demande_pseudo(no_joueur + 1)
            pseudo_valide = True if 0 < len(pseudo) <= 12 else False
            if not pseudo_valide:
                afg_erreur(2)

        joueur_partie = Joueurs(no_joueur, pseudo)
        liste_joueurs.append(joueur_partie)

    return liste_joueurs


def creer_manche(ancienne_manche=None):
    """
    Principe :
        Créer une nouvelle manche à partir de la manche précédente.
        Si c'est la première, on crée la manche à partir des informations par défaut
    À quel moment est appelé cette fonction ? :
        Au moment de créer une nouvelle manche.
    Entrée :
        - ancienne_manche       [objet MANCHE]: la manche précédente
    Sortie :
        - objet                 [objet MANCHE]: l'objet représentant la nouvelle manche

    """

    # Initialise la première manche
    if ancienne_manche is None:
        liste_joueurs = creer_joueur()  # On crée la liste de joueurs

        deck = {1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 7: 2, 9: 1, 11: 2, 13: 1, 14: 1, 15: 1, 17: 1, "araignées": 3,
                "serpents": 3,
                "laves": 3, "boulets": 3, "béliers": 3, "relique": 1}

        manche_en_cours = Manche(deck, liste_joueurs)

    # Sinon, on importe la manche précédente et on prépare la nouvelle
    else:
        manche_en_cours = importe_creer_nouvelle_manche(ancienne_manche)

    # Renvoie objet
    return manche_en_cours


def decision_joueur(manche):
    """
    Principe :
        Demande un par un à chaque joueur leur décision, s'ils veulent continuer ou rentrer an campement
    Entrée :
        manche  [objet MANCHE]: Objet représentant la manche.
    Sortie :
        Aucune
    """
    etat_joueurs = manche.etat_joueurs_dans_la_manche
    liste_joueur = manche.liste_joueurs_dans_la_manche
    joueur_sorti = []

    for joueur in range(len(etat_joueurs)):
        decision_nn_valide = True

        if etat_joueurs[joueur] == "En_Jeu":

            while decision_nn_valide:
                decision = afg_demande_decision_joueur(liste_joueur[joueur], manche)  # Demande le choix au joueur

                if decision in ['R', 'r']:  # rentre au campement
                    joueur_sorti.append(liste_joueur[joueur])
                    decision_nn_valide = False

                elif decision in ['C', 'c']:  # continue l'exploration
                    decision_nn_valide = False

                else:
                    afg_erreur(0)

    if joueur_sorti:
        retour_campement(joueur_sorti, manche)

        for joueur in joueur_sorti:  # On change l'état des joueurs en "Sortie".
            manche.set_etat_joueur_dans_la_manche(joueur.no_joueur, "Sortie")

    # Affiche l'état des joueurs.
    for joueur in range(len(etat_joueurs)):
        afg_decision_joueur(liste_joueur[joueur], etat_joueurs[joueur])

    return joueur_sorti


def verifie_etat_jeu(manche):
    """
    Principe :
        Vérifie s'il reste au moins un Joueur En_Jeu dans la manche actuel.
        Arrête la manche s'il y a plus de joueur.
    Entrée :
        manche  [objet MANCHE]: Objet représentant la manche.
    Sortie :
        Aucune
    """
    assert type(manche) == Manche, "ERREUR >> PARAMÈTRE invalide, ça doit être un objet de type MANCHE."

    if manche.nb_joueur_actif < 1:  # True s'il y a plus de joueurs, False sinon.
        manche.set_manche_termine()
        manche.set_ajout_liste_manche_reussite_ou_non(True)  # On marque l'exploration comme étant une réussite

        if debug:
            print("DEBUG VEJ >> Plus de joueur en jeu, arrêt de la manche...")
    elif debug:
        print("DEBUG VEJ >> Il y a encore des joueurs, poursuite de la partie.")


def deploie_carte(manche):
    """
    Principe :
        Appel la méthode tirage_de_carte de l'objet MANCHE.
        Il appelle également la fonction afg_deploie_carte().

        Appel la fonction execute_carte() [situé dans fonctions.py] ensuite.
    À quel moment est appelée cette fonction ? :
        À chaque début de tour.
    Entrée :
        manche  [objet MANCHE]: Objet représentant la manche.
    Sortie :
        manche  [objet MANCHE]: Objet (modifié) représentant la manche.
    """
    assert type(manche) is Manche, "ERREUR >> Le paramètre ne correspond pas à ce qu'attendait la fonction."

    carte_tiree = manche.tirage_de_carte()

    afg_deploie_carte(carte_tiree, manche)

    execute_carte(carte_tiree, manche)

    afg_deploie_carte(carte_tiree, manche)



    return manche


def execute_carte(carte_tiree, manche):
    """
    Principe :
        En fonction du type de carte, il appelle sa composante adéquate pour exécuter son action
    Entrée :
        carte_tiree         [STR / INT] : Nom de la carte à exécuter (INT si c'est une carte trésor, STR sinon)
        manche                 [MANCHE] : Manche actuel
    Sortie :
        Aucune
    """
    assert type(manche) is Manche, "ERREUR >> PARAMÈTRE 2 (MANCHE) invalide -> Ca doit être un objet de type Manche !"
    assert carte_tiree in manche.deck.keys(), "ERREUR >> PARAMÈTRE 1 (CARTE_TIREE) invalide. -> Il n'existe pas ou du moins sous cette forme dans le deck"

    if carte_tiree in ["araignées", "serpents", "laves", "boulets", "béliers"]:
        execute_carte_danger(carte_tiree, manche)
    elif carte_tiree == "relique":
        # elif décoratif, mais aidant à la compréhension du code (⇒ si c'est une relique, on ne fait rien).
        pass
    else:
        execute_carte_tresor(carte_tiree, manche)


def execute_carte_tresor(carte_tiree, manche):
    """
    Principe :
        Distribue équitablement les diamants de la carte trésor.
        Et stocke le surplus dans le reste du trésor

    Entrée :
        carte_tiree            [int]: Carte trésor tirée dans le tour actuelle.

    Sortie :
        None
    """
    assert type(
        manche) is Manche, "ERREUR ECT >> PARAMÈTRE 2 (MANCHE) invalide -> Ca doit être un objet de type Manche !"
    assert type(carte_tiree) == int, "ERREUR ECT >> PARAMÈTRE 1 (CARTE_TIREE) invalide. -> Ce n'est pas un entier."
    assert carte_tiree in manche.deck.keys(), "ERREUR ECT >> PARAMÈTRE 1 (CARTE_TIREE) invalide. -> Il n'existe pas ou du moins sous cette forme dans le deck."
    assert manche.nb_joueur_actif >= 1, "ERREUR ECT >> Il n'y a aucun joueur en jeu."

    etat_joueur = manche.etat_joueurs_dans_la_manche
    distribution = carte_tiree // manche.nb_joueur_actif
    reste = carte_tiree % manche.nb_joueur_actif

    for joueur in range(len(etat_joueur)):
        if etat_joueur[joueur] == "En_Jeu":
            manche.liste_joueurs_dans_la_manche[joueur].set_ajout_inv_manche(distribution)

    manche.set_ajoute_diamant_tresor(reste)


def execute_carte_danger(carte_danger, manche):
    """
    Principe :
        Provoque ou pas l'accident.

        Soit le danger est seul, et dans ce cas-là, on ne fait rien.
        SOIT le danger complémente un autre, et alors :
            - On affiche un message annonçant l'accident (et donc la fin de manche).
            - On termine la manche.

    Entrée :
        carte_danger             [STR] : Carte danger tirée dans le tour actuelle.
        manche               [MANCHE] : Manche en cours d'exécution.

    Sortie :
        Aucune
    """
    assert carte_danger in ["araignées", "serpents", "laves", "boulets",
                            "béliers"], "ERREUR >> PARAMÈTRE 1 (carte_danger) INVALIDE ! Ce n'est pas une carte danger."
    assert type(manche) == Manche, "ERREUR >> PARAMÈTRE 2 (manche) INVALIDE ! Ce n'est pas un objet de type Manche."

    if manche.il_a_til_deux_dangers():  # 2 dangers identiques == arrêt de la manche
        manche.set_manche_termine()  # Arrêt de la manche
        manche.set_ajout_liste_manche_reussite_ou_non(False)  # On dit que l'exploration est un échec

        if manche.nb_joueur_actif >= 1:  # En principe, il y a au moins un joueur qui était en jeu, mais au cas où...

            # On souhaite que le message qui sera affiché fasse référence à un joueur au hasard durant l'évènement.
            # On crée une liste des joueurs présents pendant l'accident
            # De plus, on souhaite pour l'affichage connaître la somme totaux d'argent qu'ils avaient sur eux.
            joueurs_en_jeu = []
            somme_total = 0
            for joueur in manche.liste_joueurs_dans_la_manche:
                if joueur.etat == "En_Jeu":
                    joueurs_en_jeu.append(joueur)
                    somme_total += joueur.inv_manche

            joueur_select = choice(joueurs_en_jeu).pseudo  # On en choisit un au hasard, on garde que son pseudonyme.
        else:
            joueur_select = "un inconnu"
            somme_total = 0

        # envoie pseudo choisit
        afg_accident_danger_fin_manche(carte_danger, joueur_select, somme_total)  # Message


def importe_creer_nouvelle_manche(ancienne_manche):
    """
    Principe :
        Récupère certaines informations de la manche précédente (celle importée) et les réadapte pour créer une nouvelle manche avec.
        Il prépare également le deck qui sera utilisé par la nouvelle manche.
    Entrée :
        manche          [MANCHE] : Objet de l'ancienne manche (celle qui vient de se terminer)
    Sortie :
        manche          [MANCHE] : Objet de la nouvelle manche qui va commencer
    """

    assert type(
        ancienne_manche) == Manche, "ERREUR >> PARAMÈTRE (ANCIENNE_MANCHE) est invalide ! Ca doit être un objet de type Manche."

    # On récupère les informations concernant la manche précédente
    no_manche = ancienne_manche.no_manche + 1
    nb_relique_pas_sortie = ancienne_manche.deck["relique"]
    dangers_a_retirer = ancienne_manche.dangers_a_retirer
    nb_relique_sortie = ancienne_manche.nb_relique_sortie
    liste_joueurs = ancienne_manche.liste_joueurs_dans_la_manche
    liste_manche_reussite_ou_non = ancienne_manche.liste_manche_reussite_ou_non

    print(liste_joueurs,"aaaaaaaaaaaaaaaaaaaaa------------------------------------------------------------------------------")

    manche_remporter = not ancienne_manche.il_a_til_deux_dangers()  # Si 2 dangers --> True. Donc la manche n'a pas été remporté (donc not True --> False)
    # Sinon --> False. Donc la manche a été remporté (not False --> True)

    for joueur in liste_joueurs:
        # On initialise les objets joueurs pour cette nouvelle manche.
        joueur.preparatif_nouvelle_manche(manche_remporter)

    # DECK ----------------------------------------
    # Deck par défaut
    deck = {1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 7: 2, 9: 1, 11: 2, 13: 1, 14: 1, 15: 1, 17: 1, "araignées": 3, "serpents": 3,
            "laves": 3, "boulets": 3, "béliers": 3, "relique": 0}

    # On réajuste le deck pour cette partie
    for danger in dangers_a_retirer.keys():
        # On retire les cartes qui ont précédemment fait terminer une manche
        deck[danger] -= dangers_a_retirer[danger]

    # On ajoute les reliques qui ne sont pas sorties + on rajoute la relique de cette nouvelle manche
    deck["relique"] = nb_relique_pas_sortie + 1
    # ---------------------------------------------

    nouvelle_manche = Manche(deck, liste_joueurs, no_manche, nb_relique_sortie, dangers_a_retirer,
                             liste_manche_reussite_ou_non)

    return nouvelle_manche


def retour_campement(joueur_sorti, manche):
    """
    Principe :
        Rajoute les diamants des joueurs dans l'inventaire de la partie.
    Entrée :
        joueur_sorti        [LIST] : liste des joueurs qui sont sortis ce tour
        manche      [objet MANCHE] : Objet représentant la manche.
    Sortie :
        Aucune
    """
    assert type(joueur_sorti) == list, "ERREUR >> PARAMÈTRE 1 (joueur_sorti) INVALIDE. Ca doit être une liste !"

    for objet in joueur_sorti:
        assert type(
            objet) == Joueurs, "ERREUR >> PARAMÈTRE 1 (joueur_sorti) INVALIDE. La liste contient des éléments en dehors de la classe Joueurs !"

    assert type(manche) == Manche, "ERREUR >> PARAMÈTRE 2 (manche) INVALIDE. Ca doit être un objet de type Manche !"

    manche.distribution_du_reste_tresor(joueur_sorti)

    if len(joueur_sorti) == 1 and manche.banc.count("relique") >= 1:
        manche.distribution_relique(joueur_sorti[0])
        # On l'ajoute dans son inventaire de manche, car c'est lié à cette manche.
        # Dans tous les cas, la boucle suivante l'exportera dans l'inventaire de la partie.

    for joueur in joueur_sorti:
        joueur.preparatif_nouvelle_manche(True, False)


def scoreboard(partie_terminer):
    """
    Principe :
        Parcours la liste des joueurs et range le joueur en fonction de son classement.

        Mauvais joueur               Bon joueur
        |                            |
        [============================]>

        Note : Cette fonction est appelée uniquement par fin_de_jeu
    Entrée :
        partie_terminer                 [MANCHE] : Objet manche (n° 6) représentant la partie terminée.
    Sortie :
        tableau_des_scores      [LIST > JOUEURS] : Liste contenant les joueurs classés par leur nombre de diamants.
    """
    assert type(partie_terminer) == Manche, "ERREUR > Le paramètre n'est pas un objet de type Manche"

    tableau_des_scores = [partie_terminer.liste_joueurs_dans_la_manche[
                              0]]  # On stocke le premier joueur comme référence pour la première comparaison.

    liste_joueurs = partie_terminer.liste_joueurs_dans_la_manche  # Pour que ce soit plus simple et court

    for joueur in range(1, len(liste_joueurs)):  # On parcourt la liste de joueurs, en esquivant le premier.

        joueur_placer = False  # False ⇒ le joueur n'est pas placé dans tableau_des_scores
        #  True ⇒ le joueur est placé dans tableau_des_scores

        joueur_precedent = joueur - 1

        while not joueur_placer and joueur_precedent >= 0:  # Tant que le joueur n'est pas placé, parcours du joueur précédent au premier joueur de la liste de joueur.

            if liste_joueurs[joueur].inv_partie > tableau_des_scores[
                joueur_precedent].inv_partie:  # Si le joueur possède un plus grand score que le joueur actuellement sélectionné dans le score board.
                tableau_des_scores.insert(joueur_precedent + 1,
                                          liste_joueurs[joueur])  # On ajoute le joueur à sa droite
                joueur_placer = True

            joueur_precedent -= 1

            # Le joueur possède un plus petit nombre de diamants que le joueur sélectionné dans le scoreboard

        if not joueur_placer:  # Si le joueur n'a toujours pas été placé (car il possède la plus petite valeur du scoreboard).
            tableau_des_scores.insert(0, liste_joueurs[joueur])

    return tableau_des_scores


def fin_de_jeu(partie_terminer):
    """
    Principe :
        S'occupe de la fin de la partie

        -- Annonce le vainqueur
        -- Fait afficher le classement

        -- Résumé de la partie

        -- Félicite les joueurs (ou pas) et les incites à rejouer.
    Entrée :
        partie_terminer          [MANCHE] : Objet manche (n° 6) représentant la partie terminée.
    Sortie :
        Aucune
    """

    assert type(partie_terminer) == Manche, "ERREUR > Le paramètre n'est pas un objet de type Manche"

    tableau_des_scores = scoreboard(partie_terminer)  # scoreboard trié du moins bon au meilleur joueur


    afg_fin_jeu_histoire_1(tableau_des_scores, partie_terminer)  # Petite histoire du retour des joueurs au village

    # Note : Continuer, permet de savoir si les joueurs souhaite passer certaines "cinématiques" du jeu.
    #        Si continuer == "STOP", alors on saute.

    continuer = afg_fin_jeu_stats_2(tableau_des_scores, partie_terminer)  # Affiche les statistiques
    if continuer != "STOP":
        afg_fin_jeu_remerciement_3()  # Remerciement pour le joueur
    return
