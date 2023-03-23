# coding: utf-8
from medias.py.tkiteasy import *
from medias.py.fonctions_graphique import *
from medias.py.initialisation import Joueurs, Manche
from random import choice

g = None
elements_graphique_tapis = []


def ouvrir_affichage():
    global g
    global DIMENSION_X_FEN, DIMENSION_Y_FEN  # les valeurs proviennent du fichier fonctions_graphique.py

    g = ouvrirFenetre(DIMENSION_X_FEN, DIMENSION_Y_FEN)

    return g

def afg_erreur(id_erreur=None):
    """
    Principe :
        Affiche une erreur en fonction de l'identifiant reçu.
        Attend que le joueur clic pour poursuivre.
    Entrée :
        id_erreur   [INT / NONE]: l'identifiant de l'erreur
                                  Si None : on affiche le message par défaut.
    Sortie :
        Aucune
    """

    a = g.afficherImage(0, 0, "medias/img/fond_jeu.jpg")

    if id_erreur == 0:
        affiche_ligne_dans_boite_dialogue(g,["ERREUR >> Votre choix n'est pas valide !","Veuillez recommencer avec une valeur comprise entre 3 et 8 inclus."])
    elif id_erreur == 1:
        affiche_ligne_dans_boite_dialogue(g,["ERREUR >> Votre choix n'est pas valide !","Veuillez recommencer avec une valeur comprise entre 3 et 8 inclus."])
    elif id_erreur == 2:
        affiche_ligne_dans_boite_dialogue(g,["ERREUR >> Votre pseudonyme doit faire 1 à 12 caractères compris !"])
    else:
        affiche_ligne_dans_boite_dialogue(g,["ERREUR >> Une erreur est survenu."])

    g.supprimer(a)

def afg_ecran_titre():
    """
    FONCTION APPELÉE PAR DIAMANTS.PY

    Affiche :
        - Nom du jeu
        - Matthieu  & Tom  IUT de Vélizy
        - Option 1 : Lancer le jeu
        - Option 2: Lire les règles
        - Option 3 : Quitter
    Entrée :
        Aucune
    Sortie :
        option  [STR]: Choix de l'utilisateur entre l'option 1 ou 3.
    """

    global g
    a0 = g.afficherImage(0, 0, "medias/img/ecran_titre.jpg")

    pas_decision = True
    while pas_decision:
        click = g.attendreClic()
        if click.x > 1075 and click.x < 1475 and click.y > 295 and click.y < 395:  # Jouer
            g.supprimer(a0)
            return '1'
        elif click.x > 1075 and click.x < 1475 and click.y > 460 and click.y < 560:  # Règles
            g.supprimer(a0)
            return '2'
        elif click.x > 1075 and click.x < 1475 and click.y > 650 and click.y < 750:  # Quitter
            g.fermerFenetre()
            return '3'

def afg_regles():
    global g
    a0 = g.afficherImage(0, 0, "medias/img/regle.jpg")
    pas_decision = True
    while pas_decision:
        click = g.attendreClic()
        if click.x > 1325 and click.x < 1725 and click.y > 765 and click.y < 865:  # Retour Menu
            g.supprimer(a0)
            return '1'

def afg_creer_joueur_demande_nbjoueurs():
    """
    FONCTION APPELÉE PAR LA FONCTION CREER_JOUEUR DE FONCTIONS.PY

    Principe :
        Demande le nombre de joueurs
    Entrée :
        Aucune
    Sortie:
        nb_joueurs  [STR] : Nombre de joueurs participant à la partie
    """
    global g
    a0 = g.afficherImage(0, 0, "medias/img/nb_joueur.jpg")
    pas_decision = True
    while pas_decision:
        click = g.attendreClic()
        if click.x > 150 and click.x < 300 and click.y > 470 and click.y < 620:
            g.supprimer(a0)
            return 3
        elif click.x > 415 and click.x < 565 and click.y > 470 and click.y < 620:
            g.supprimer(a0)
            return 4
        elif click.x > 1075 and click.x < 680 and click.y > 830 and click.y < 620:
            g.fermerFenetre()
            return 5
        elif click.x > 1075 and click.x < 940 and click.y > 1090 and click.y < 620:
            g.supprimer(a0)
            return 6
        elif click.x > 1195 and click.x < 1345 and click.y > 470 and click.y < 620:
            g.supprimer(a0)
            return 7
        elif click.x > 1425 and click.x < 1575 and click.y > 470 and click.y < 620:
            g.supprimer(a0)
            return 8

def afg_creer_joueur_demande_pseudo(no_joueur):
    global g

    a0 = g.afficherImage(0, 0, "medias/img/pseudo.jpg")
    a1 = g.afficherTexte("Quel est le pseudonyme du joueur n°" + str(no_joueur) + " (12 caractère maximum): ", 875, 200,
                         "black", 34)  ##### nouveau

    non_fini = True
    aff_pseudo = g.afficherTexte("", 875, 550, "black", 34)
    pseudo = ""

    while non_fini:
        temps = 0
        touche = None
        while touche is None:
            touche = g.recupererTouche()
            temps += 1
            if (temps // 2000) % 2 == 1 or len(pseudo) >= 12:
                g.changerTexte(aff_pseudo, pseudo + "  ")
            else:
                g.changerTexte(aff_pseudo, pseudo + "_")

        if len(touche) == 1 or touche == "space":
            if touche == "space":
                touche = " "
            if len(pseudo) < 12:
                pseudo = pseudo + touche
                g.actualiser()
                g.changerTexte(aff_pseudo, pseudo)
        else:
            if touche == "Return":
                for i in [a0, a1, aff_pseudo]:
                    g.supprimer(i)
                g.actualiser()
                return pseudo
            elif touche == "BackSpace":
                if len(pseudo) > 0:
                    pseudo = pseudo[:-1]
                    g.actualiser()
                    g.changerTexte(aff_pseudo, pseudo + "_")


def afg_tapis_de_jeu(manche):
    """
    FONCTION APPELÉE PAR LA FONCTION PARTIE_DE_JEU DE DIAMANTS.PY

    Principe :
        Affiche l'état actuel du jeu

    Entrée :
        - manche    [objet MANCHE] : objet qui contient les informations sur la manche actuelle

    Sortie :
        Aucune
    """
    global g
    global elements_graphique_tapis

    assert g is not None, "ATTENTION, il n'y a pas de fenêtre !"

    elements_graphique_tapis = []

    elements_graphique_tapis.append(g.afficherImage(0, 0, "medias/img/fond_jeu.jpg"))

    elements_graphique_tapis.append(g.afficherImage(725, 30, "medias/img/Titre.png"))

    # manche
    elements_graphique_tapis.append(g.dessinerRectangle(1500, 30, 200, 75, "#374D34"))
    elements_graphique_tapis.append(g.afficherTexte("Manche n°" + str(manche.no_manche), 1600, 65, "beige"))

    pos = [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1), (3, 1)]
    liste_joueurs = manche.liste_joueurs_dans_la_manche
    for i in range(len(liste_joueurs)):

        if manche.etat_joueurs_dans_la_manche[i] == "En_Jeu":
            elements_graphique_tapis.append(
                g.afficherImage(45 + pos[i][0] * 420, pos[i][1] * 120 + 125, "medias/img/joueur_grotte.png"))
        elif manche.etat_joueurs_dans_la_manche[i] == "Sortie":
            elements_graphique_tapis.append(
                g.afficherImage(45 + pos[i][0] * 420, pos[i][1] * 120 + 125, "medias/img/sortie_grotte.png"))

        elements_graphique_tapis.append(
            g.afficherTexte(liste_joueurs[i].pseudo, 45 + pos[i][0] * 420 + 250, pos[i][1] * 120 + 140, "beige"))

        elements_graphique_tapis.append(
            g.afficherTexte(liste_joueurs[i].inv_partie, 45 + pos[i][0] * 420 + 108, pos[i][1] * 120 + 190, "#D1E3ED",
                            24))  # nb coffre diamant
        elements_graphique_tapis.append(g.afficherImage(45 + pos[i][0] * 420 + 135, pos[i][1] * 120 + 160,
                                                        "medias/img/coffre_joueur.png"))  # image coffre diamant

        elements_graphique_tapis.append(
            g.afficherTexte(liste_joueurs[i].inv_manche, 45 + pos[i][0] * 420 + 225, pos[i][1] * 120 + 190, "#18fff0",
                            24))  # nb diamant
        elements_graphique_tapis.append(g.afficherImage(45 + pos[i][0] * 420 + 250, pos[i][1] * 120 + 170,
                                                        "medias/img/diamant.png"))  # image diamant
        elements_graphique_tapis.append(
            g.afficherTexte(liste_joueurs[i].inv_relique, 45 + pos[i][0] * 420 + 320, pos[i][1] * 120 + 190, "#f5ff00",
                            24))  # nb relique
        elements_graphique_tapis.append(g.afficherImage(45 + pos[i][0] * 420 + 335, pos[i][1] * 120 + 160,
                                                        "medias/img/relique.png"))  # image relique

    # banc

    elements_graphique_tapis.append(g.dessinerRectangle(175, 400, 1400, 400, "#18232B"))

    elements_graphique_tapis.append(g.afficherTexte("Dangers :", 262, 500))
    elements_graphique_tapis.append(g.afficherTexte("Relique :", 262, 680))

    elements_graphique_tapis.append(g.afficherImage(1200, 450, "medias/img/tresor.png"))
    elements_graphique_tapis.append(g.afficherTexte(str(manche.reste_tresor), 1325, 575, "white", 64))

    # elements_graphique_tapis = [a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15]

    afg_reaffiche_cartes(manche)


def suppr_tapis_jeu_elements():
    global g
    global elements_graphique_tapis

    assert g is not None, "ATTENTION, il n'y a pas de fenêtre !"
    assert elements_graphique_tapis is not None, "ATTENTION, il n'y a pas d'éléments affichés !"

    for element in elements_graphique_tapis:
        g.supprimer(element)

    elements_graphique_tapis = None


def afg_deploie_carte(carte_tiree, manche):
    global g
    assert type(manche) == Manche
    assert carte_tiree in manche.deck.keys()
    assert g is not None, "ATTENTION, il n'y a pas de fenêtre !"
    suppr_tapis_jeu_elements()
    afg_tapis_de_jeu(manche)

    pos = [0, 1, 2, 3, 4, 5]
    no_danger = (len(manche.banc) - manche.banc.count("relique")) - 1  # Position de la dernière carte danger de sortie
    no_relique = manche.banc.count("relique") - 1  # Position de la dernière relique sortie

    a0 = g.dessinerRectangle(175, 830, 1400, 50, "#18232B")

    if carte_tiree == "araignées":
        g.afficherImage(350 + pos[no_danger] * 140, 425, "medias/img/carte_araignees.png")
        a1 = g.afficherTexte("La carte tirée est la carte danger : " + carte_tiree, 875, 855, "#ff4141", 24)
    elif carte_tiree == "serpents":
        g.afficherImage(350 + pos[no_danger] * 140, 425, "medias/img/carte_serpents.png")
        a1 = g.afficherTexte("La carte tirée est la carte danger : " + carte_tiree, 875, 855, "#ff4141", 24)
    elif carte_tiree == "laves":
        g.afficherImage(350 + pos[no_danger] * 140, 425, "medias/img/carte_laves.png")
        a1 = g.afficherTexte("La carte tirée est la carte danger : " + carte_tiree, 875, 855, "#ff4141", 24)
    elif carte_tiree == "boulets":
        g.afficherImage(350 + pos[no_danger] * 140, 425, "medias/img/carte_boulets.png")
        a1 = g.afficherTexte("La carte tirée est la carte danger : " + carte_tiree, 875, 855, "#ff4141", 24)
    elif carte_tiree == "béliers":
        g.afficherImage(350 + pos[no_danger] * 140, 425, "medias/img/carte_beliers.png")
        a1 = g.afficherTexte("La carte tirée est la carte danger : " + carte_tiree, 875, 855, "#ff4141", 24)
    elif carte_tiree == "relique":
        g.afficherImage(350 + pos[no_relique] * 140, 605, "medias/img/carte_relique.png")
        a1 = g.afficherTexte("La carte tirée est une relique", 875, 855, "#f5ff00",24)
    else:
        a1 = g.afficherTexte("La carte tirée est une carte trésor de " + str(carte_tiree) + " diamants", 875, 855,"#18fff0", 24)
    g.actualiser()
    sleep(0.5)
    g.actualiser()
    suppr_tapis_jeu_elements()
    afg_tapis_de_jeu(manche)
    for i in [a0, a1]:
        g.supprimer(i)


def afg_reaffiche_cartes(manche):
    assert type(manche) == Manche, "ERREUR >> Le paramètre n'est pas une MANCHE !"
    assert g is not None, "ATTENTION, il n'y a pas de fenêtre !"
    relique_a_afficher = 0

    for carte in range(len(manche.banc)):

        nom_carte = manche.banc[carte]

        if nom_carte == "araignées":
            nom_carte = "araignees"
        elif nom_carte == "béliers":
            nom_carte = "beliers"
        elif nom_carte == "relique":
            relique_a_afficher += 1

        if nom_carte == "relique":
            g.afficherImage(350 + (relique_a_afficher - 1) * 140, 605, "medias/img/carte_relique.png")
        else:
            g.afficherImage(350 + (carte - relique_a_afficher) * 140, 425, "medias/img/carte_" + nom_carte + ".png")

def afg_decision_joueur(joueur, decision):
    assert type(joueur) == Joueurs, "ERREUR GRAPHIQUE >> Paramètre 1 n'est pas un objet joueur."

    img = "narration"

    if decision == "En_Jeu":
        choix = "continuer l'exploration."
    elif decision == "Sortie":
        choix = "retourner au campement."
    else:
        choix = "un choix... étrange"
        img = None


    affiche_ligne_dans_boite_dialogue(g,[str(joueur.pseudo).upper()+" a fait comme choix de:",choix],img)

def afg_accident_danger_fin_manche (carte_danger, pseudo_joueur_victime, somme_total):
    """
        Entrée :
            carte_danger                [STR] : Carte danger qui a provoqué l'accident.
            pseudo_joueur_victime       [STR] : Un joueur victime sévèrement de l'accident selon l'histoire.
            somme_total                 [INT] : Somme total de tous les diamants qu'avait les joueurs au moment de l'accident.
        """

    global g
    assert g is not None, "ATTENTION, il n'y a pas de fenêtre !"

    titre = "Un MISSINGNO. sauvage apparaît !"
    evenement2 = "les données allaient être corrompu"

    pronom = "des"

    if carte_danger == "araignées":
        titre = "DERNIÈRE MINUTE ! Des araignées mutantes prennent au piège un groupe d'explorateur..."
        evenement2 = "les araignées étaient en train de se métamorphoser pour mieux vous digérer"
    elif carte_danger == "serpents":
        titre = "DERNIÈRE MINUTE ! Des serpents jaune fluo attaquent des explorateurs !"
        evenement2 = "les serpents allaient totalement vous aveugler par la luminance de leur peau"
    elif carte_danger == "laves":
        pronom = "de la"
        titre = "DERNIÈRE MINUTE ! La lave, ça brûle, et l'eau, ça mouille... Mais pas pour ce groupe d'explorateur..."
        evenement2 = "les petites goûtes se transformèrent en torrent brûlant de laves"
    elif carte_danger == "boulets":
        titre = "DERNIÈRE MINUTE ! BOOM BOOM BOOM Des explorateurs frappés par des boulets."
        evenement2 = "un boulet allait tomber pile sur " + pseudo_joueur_victime
    elif carte_danger == "béliers":
        titre = "DERNIÈRE MINUTE ! Des explorateurs frappés par un bélier !"
        evenement2 = "le bélier était revenu vous éventrer"
    affiche_ligne_dans_boite_dialogue(g, [titre,"☠ Avide de gloire et de fortune, vous vous êtes beaucoup trop enfoncé dans la grotte. ☠",
                                          "",
                                          "Vous n'avez pas cru les paroles de ce villageois il y a quelques temps:"], "journal")
    affiche_ligne_dans_boite_dialogue(g, ["Attention jeunes aventuriers et aventurières ! De multiple dangers dont " + pronom + " " + carte_danger + " s'y trouve !"],"papy_paroles")
    affiche_ligne_dans_boite_dialogue(g, ["Pris de peur," + pseudo_joueur_victime + " a fait un malaise.",
                                          "Vous avez réussit à le sauver, et juste au moment où " + evenement2 + "... Vous vous êtes enfuis.",
                                          "",
                                          "Par la panique, vous avez oublié vos sacs...",
                                          "Vous avez perdu au total " + str(somme_total) + " diamants."], "journal")

def afg_tirer_une_carte():
    # Demande juste au joueur d'appuyer pour poursuivre

    global g

    DIMENSION_X_FEN, DIMENSION_Y_FEN = 1750, 900



    zone_cliquer = False

    x1 = DIMENSION_X_FEN // 2 -190
    x2 = DIMENSION_X_FEN // 2 +110
    y1 = DIMENSION_Y_FEN // 4 -100
    y2 = 575

    elements_boite_dialogue = []

    elements_boite_dialogue.append(g.afficherImage(DIMENSION_X_FEN // 2 - 190, DIMENSION_Y_FEN // 4 - 100, "medias/img/carte_inconnu.png"))

    TAILLE_FOND = [1225,255]  # X, Y
    POS_X_FD = DIMENSION_X_FEN // 2 - TAILLE_FOND[0] // 2
    POS_Y_FD = DIMENSION_Y_FEN - TAILLE_FOND[1] - 20

    elements_boite_dialogue.append(g.afficherImage(0, 0, "medias/img/effet_bas_noir_transparent.png"))
    elements_boite_dialogue.append(g.afficherImage(300, 300, "medias/img/"+"unknowb"+".png"))
    elements_boite_dialogue.append(g.afficherImage(POS_X_FD, POS_Y_FD, "medias/img/fond_dialogue.png"))

    elements_boite_dialogue.append(g.afficherTextePlus("Cliquez sur la carte pour la piocher !", DIMENSION_X_FEN // 2, POS_Y_FD + 130,
                                                       "black", 45, "Papyrus", "bold"))

    while not zone_cliquer:
        #affiche_ligne_dans_boite_dialogue(g, ["Cliquez sur la carte pour la piocher !"])

        clic = g.attendreClic()
        if clic != None:
            if clic.x > x1 and clic.x < x2:
                if clic.y > y1 and clic.y < y2:
                    zone_cliquer = True


    for i in elements_boite_dialogue:
        g.supprimer(i)


def afg_demande_decision_joueur(joueur, manche):
    global g
    assert g is not None, "ATTENTION, il n'y a pas de fenêtre !"

    # cadre de décision
    a0 = g.dessinerRectangle(175, 830, 1400, 50, "#18232B")
    a1 = g.afficherTexte(joueur.pseudo + " doit choisir entre poursuivre l'exploration et rentrer au campement :", 630,
                         855, "white", 17)

    a2 = g.afficherImage(1085, 835, "medias/img/explorer.png")

    a3 = g.afficherImage(1305, 835, "medias/img/sortir.png")

    pas_decision = True
    while pas_decision:
        click = g.attendreClic()
        if click.x > 1085 and click.x < 1285 and click.y > 835 and click.y < 875:
            for i in [a0, a1, a2, a3]:
                g.supprimer(i)
            return "C"
        elif click.x > 1305 and click.x < 1565 and click.y > 835 and click.y < 875:
            for i in [a0, a1, a2, a3]:
                g.supprimer(i)
            return "R"


def fermer_fenetre():
    global g
    assert g is not None, "ATTENTION, il n'y a pas de fenêtre !"

    while g.recupererClic() == None:
        continue
    # fermeture fenêtre
    g.fermerFenetre()


def afg_lancement_manche(manche):
    # Message annonçant la nouvelle manche

    assert type(manche) == Manche, "ERREUR >> Le paramètre n'est pas un objet de type manche."

    joueur_au_pif = choice(manche.liste_joueurs_dans_la_manche).pseudo


    if manche.no_manche == 1:
        affiche_ligne_dans_boite_dialogue(g, [
            ">> Manche 1 >> Explorateurs, exploratrices vous venez d'entrer dans l'antre de la grotte du Pindaï.","Votre première exploration ne fait que de commencer !"])
    elif manche.no_manche == 2:
        if manche.liste_manche_reussite_ou_non[0]:
            affiche_ligne_dans_boite_dialogue(g, [
                ">> Manche 2 >> Après la réussite de la première manche,","vous décidez de vous avancer d'avantage dans la grotte..."])

        else:
            affiche_ligne_dans_boite_dialogue(g, [
                ">> Manche 2 >> Votre épopée a très mal commencé.","Par chance, " + joueur_au_pif + " a vu un petit passage durant la première quête.","Vous décidez alors de le suivre..."])

    elif manche.no_manche == 3:
        if manche.liste_manche_reussite_ou_non.count(True) == 2:
            affiche_ligne_dans_boite_dialogue(g, [
                ">> Manche 3 >> Comme on le dit dans le milieu, jamais 2 sans 3 !"," Assuré par une certaine confiance, vous prenez cette fois-ci un chemin découvert par..." + joueur_au_pif + " !"])

        elif manche.liste_manche_reussite_ou_non[1]:
            affiche_ligne_dans_boite_dialogue(g, [
                ">> Manche 3 >> Malgré la chance que vous avez eu en changeant de chemin, vous avez décidé de prendre son opposé."," En effet, la grotte du Pindaï cache encore des surprises !"])

        else:
            affiche_ligne_dans_boite_dialogue(g, [
                ">> Manche 3 >> Vous prenez un nouveau chemin tout en réfléchissant à ce villageois que vous détestez tant...","Ah et " + joueur_au_pif + " a faillit oublier la carte pour vous repérer...","Quel tête en l'air..."])

    elif manche.no_manche == 4:
        if manche.liste_manche_reussite_ou_non.count(True) == 3:
            affiche_ligne_dans_boite_dialogue(g, [
                ">> Manche 4 >> Excellent ! Fabuleux !"," Alors que vous vous esclaffer en pensant à votre bulletin et votre chance inouï..." + joueur_au_pif + " a oublié les sandwich..."])

        elif manche.liste_manche_reussite_ou_non[0] and manche.liste_manche_reussite_ou_non.count(True) == 2:
            affiche_ligne_dans_boite_dialogue(g, [">> Manche 4 >> Jamais 2 sans 3... Bon...","Déçus, vous continuer votre quête."])

        elif manche.liste_manche_reussite_ou_non[1]:
            affiche_ligne_dans_boite_dialogue(g, [">> Manche 4 >> La dernière exploration a été une réussite !"," Grotte du Pindaï nous revoilà !"])

        else:
            affiche_ligne_dans_boite_dialogue(g, [
                ">> Manche 4 >> Après avoir mangé les sandwich préparés par " + joueur_au_pif + " vous continuez votre aventure."])

    elif manche.no_manche == 5:
        joueur_au_pif2 = choice(manche.liste_joueurs_dans_la_manche).pseudo
        while joueur_au_pif == joueur_au_pif2:
            joueur_au_pif2 = choice(manche.liste_joueurs_dans_la_manche).pseudo

        if manche.liste_manche_reussite_ou_non.count(True) == 4:
            affiche_ligne_dans_boite_dialogue(g, [
                ">> Manche 5 >> Pas le temps de réfléchir. Tout le village attend impatiemment votre retour.","C'est avec une peur de ne pas revenir totalement vainqueur, que vous poursuivez...","Avec un peu de chance, vous aurez du chocolat chaud à votre retour !"])

        if manche.liste_manche_reussite_ou_non.count(True) == 3:
            affiche_ligne_dans_boite_dialogue(g, [
                ">> Manche 5 >> Bon. Vous avez échoué une fois.","Mais vous y êtes presque !" + joueur_au_pif + ", faites attention, " + joueur_au_pif2 + " réfléchi à comment vous piquez vos diamants..."])

        if manche.liste_manche_reussite_ou_non.count(True) == 2:
            affiche_ligne_dans_boite_dialogue(g, [
                ">> Manche 5 >> Aurez vous plus gagné que perdu durant l'aventure ?","Tel est la question...","Des diamants vous attende pour cette dernière quête. Nouveau chemin et z'est partizz !"])

        else:
            affiche_ligne_dans_boite_dialogue(g, [
                ">> Manche 5 >> " + joueur_au_pif + " dessine une cinquième barre. " + joueur_au_pif2 + " pleure."," Serpents, béliers, boulets... Et la même critique du villageois qui reviens."," Avant d'abandonné l'aventure, vous reprenez courage et vous poursuivez la quête...","","Mais par une autre entrée !"])


def afg_podium(tableau_des_scores):
    global g
    elements_graphique_tapis.append(g.afficherImage(0,0,"medias/img/podium.jpg"))

    for i in range (0,len(tableau_des_scores)-3):
        elements_graphique_tapis.append(g.afficherTexte(tableau_des_scores[i].pseudo,1400, 815 - 95*i ,"white",28))

    elements_graphique_tapis.append(g.afficherTexte(tableau_des_scores[-1].pseudo, 530, 190,"white",28))
    elements_graphique_tapis.append(g.afficherTexte(tableau_des_scores[-2].pseudo, 250, 555,"white",28))
    elements_graphique_tapis.append(g.afficherTexte(tableau_des_scores[-3].pseudo, 815, 615,"white",28))

def afg_fin_jeu_histoire_1(tableau_des_scores, partie_terminer):
    # Affiche une petite histoire pour la fin de la partie

    # tableau_des_scores    [LIST > JOUEURS] : classé du plus mauvais au meilleur joueur
    # partie_terminer               [MANCHE] : Objet manche (n° 6) représentant la partie terminée.

    # Retourne RIEN

    assert type(tableau_des_scores) == list, "ERREUR >> Le paramètre n'est pas une liste"
    assert type(partie_terminer) == Manche, "ERREUR > Le paramètre n'est pas un objet de type Manche"

    # Test du contenu de la liste
    for element in tableau_des_scores:
        assert type(element) == Joueurs, "ERREUR >> La liste contient un élément non objet de type joueur."

    l_joueur = partie_terminer.liste_joueurs_dans_la_manche  # Liste des joueurs dans la partie

    # Pour l'histoire, on choisit 3 joueurs différents au hasard
    J1 = choice(l_joueur).pseudo
    J2 = choice(l_joueur).pseudo
    J3 = choice(l_joueur).pseudo


    while J1 == J2:
        J2 = choice(l_joueur).pseudo

    while J3 == J1 or J3 == J2:
        J3 = choice(l_joueur).pseudo

    prenoms_classe = ["ALexis", "Chakib", "Eliott", "Enzo", "Florent", "Kylian", "Maxence", "Tom", "Matthieu", "Assia",
                      "Eden", "Fabien", "Raphaël", "Ostap", "Yanis", "Yassine", "Souhayl", "Aaron", "Mathys"]

    eleve_classe = choice(prenoms_classe)

    vainqueur = tableau_des_scores[len(tableau_des_scores) - 1]

    affiche_ligne_dans_boite_dialogue(g, ["..."])
    affiche_ligne_dans_boite_dialogue(g, [J1+": On est bientôt arrivé ?"],"joueur1")
    affiche_ligne_dans_boite_dialogue(g, [J2+": Oui !","","","Je vois la lueur de l'épicier du coin de ma rue !"], "joueur2")
    affiche_ligne_dans_boite_dialogue(g, ["Villageois: Alors, vous avez eu combien de problème au total ? hé hé hé"], "papy")

    affiche_ligne_dans_boite_dialogue(g,[J3+": "+str(partie_terminer.liste_manche_reussite_ou_non.count(False))],"joueur3")

    if partie_terminer.liste_manche_reussite_ou_non.count(False) == 0:
        affiche_ligne_dans_boite_dialogue(g, ["Villageois: Comment est-ce possible, seriez-vous les élus ?"], "papy")

    elif partie_terminer.liste_manche_reussite_ou_non.count(False) == len(partie_terminer.liste_manche_reussite_ou_non):
        affiche_ligne_dans_boite_dialogue(g, ["Villageois: Félicitation ah ah ah !","J'étais sûr que vous n'y arriverez pas."], "papy")
    else:
        affiche_ligne_dans_boite_dialogue(g, ["Villageois: Je vous avais prévenu 😈 !","Niark niark niark"], "papy")


    affiche_ligne_dans_boite_dialogue(g, [eleve_classe+": Comment allez-vous, alors qui a ramené le plus de diamant ?"], "villageois")

    if J1 == vainqueur.pseudo:  # Cas où celui qui parle est celui qui a remporté la partie
        affiche_ligne_dans_boite_dialogue(g, [J1 + ": C'est...","","","MOI !","","","  Avec " + str(vainqueur.inv_partie) + " diamants !"], "joueur1")
    else:
        affiche_ligne_dans_boite_dialogue(g, [J1 + ": C'est...","","",str(tableau_des_scores[0].pseudo) + " !","","","  Avec " + str(vainqueur.inv_partie) + " diamants !"], "joueur1")

    if vainqueur.inv_partie == 0:
        affiche_ligne_dans_boite_dialogue(g,[eleve_classe + ": Dommage..."],"villageois")
    else:
        affiche_ligne_dans_boite_dialogue(g,[eleve_classe + ": Bravo !"],"villageois")


    affiche_ligne_dans_boite_dialogue(g, [eleve_classe + ": Vous prendrez un peu de chocolat chaud ?","Tout le village sauf l'autre villageois là vous attend."], "villageois")

    affiche_ligne_dans_boite_dialogue(g, [J2+ ": Volontier !"], "joueur2")

    affiche_ligne_dans_boite_dialogue(g, [J3 + ": Allons-y !"], "joueur3")

def afg_fin_jeu_stats_2(tableau_des_scores, partie_terminer):
    # Affiche les statistiques de la partie

    # tableau_des_scores    [LIST > JOUEURS] : classé du plus mauvais au meilleur joueur
    # partie_terminer               [MANCHE] : Objet manche (n° 6) représentant la partie terminée.

    # Sorti : None ou "STOP" si le joueur ne veut pas afficher le message suivant.

    reussites = int(partie_terminer.liste_manche_reussite_ou_non.count(True))
    defaites = int(partie_terminer.liste_manche_reussite_ou_non.count(False))

    total_diams = 0
    for joueur in tableau_des_scores:
        total_diams += joueur.inv_partie

    reliques_sorties = partie_terminer.nb_relique_sortie

    affiche_ligne_dans_boite_dialogue(g, ["NARRATEUR: Et c'est ainsi que se termine votre épopée dans la grotte du Pindaï...","","","NARRATEUR: Au total, votre aventure c'est..."], "narration")

    affiche_ligne_dans_boite_dialogue(g, [str(reussites) + " manches de réussites", str(defaites) + " manches d'échouées", str(total_diams) + " diamants récupérés", str(reliques_sorties) + " reliques qui ont été récupérées"], "narration")

    affiche_ligne_dans_boite_dialogue(g, ["NARRATEUR: Mais également...","","","des accidents...","","","Avec:"], "narration")


    il_y_a_pas_eu_de_probleme = True
    l_dangers = partie_terminer.dangers_a_retirer
    for danger in l_dangers:
        if danger == "araignées" and l_dangers[danger] > 0:
            affiche_ligne_dans_boite_dialogue(g, [str(l_dangers[danger])+" fois où des araignées mutantes qui voulaient vous digérer"],"narration")
            il_y_a_pas_eu_de_probleme = False

        if danger == "serpents" and l_dangers[danger] > 0:
            affiche_ligne_dans_boite_dialogue(g, [str(l_dangers[danger])+" fois où des serpents jaune fluo qui voulaient vous aveugler à vie"],"narration")
            il_y_a_pas_eu_de_probleme = False

        if danger == "laves" and l_dangers[danger] > 0:
            affiche_ligne_dans_boite_dialogue(g, [str(l_dangers[danger])+" fois où de la lave à faillit vous carboniser"],"narration")
            il_y_a_pas_eu_de_probleme = False

        if danger == "boulets" and l_dangers[danger] > 0:
            affiche_ligne_dans_boite_dialogue(g, [str(l_dangers[danger])+" fois où des boulets vous ont frôlé"],"narration")
            il_y_a_pas_eu_de_probleme = False

        if danger == "béliers" and l_dangers[danger] > 0:
            affiche_ligne_dans_boite_dialogue(g, [str(l_dangers[danger])+" fois où des béliers déchaînés ont essayés de vous éventrer"],"narration")
            il_y_a_pas_eu_de_probleme = False


    if il_y_a_pas_eu_de_probleme:
        affiche_ligne_dans_boite_dialogue(g, ["Aucune égratignure, en effet, vous avez échappé au pire !"],"narration")

        affiche_ligne_dans_boite_dialogue(g, ["Villageois: Briguant, au voleur !","A l'assassin, au meurtrier !"],"papy")


    affiche_ligne_dans_boite_dialogue(g, ["NARRATEUR: Voici le tableau des scores:"],"narration")



    afg_podium(tableau_des_scores)
    g.actualiser()
    sleep(3)

    affiche_ligne_dans_boite_dialogue(g, ["Cliquez pour continuer"])

    return

def afg_fin_jeu_remerciement_3():
    affiche_ligne_dans_boite_dialogue(g, ["Merci d'avoir joué à ce jeu","De jeunes personnes qui sont Matthieu  et Tom  ont fait un travaille acharné dessus.","Nous espérons que vous avez passé un excellent moment !"],"narration")


    affiche_ligne_dans_boite_dialogue(g, ["N'hésitez pas à relancer une partie pour une toute nouvelle aventure inédite !"],"narration")

    affiche_ligne_dans_boite_dialogue(g, ["Villageois: Ne vous en fait pas, je serais de retour pour vous faire un mauvais tour !","","","Afin de préserver le monde des voleurs","","","Afin de rallier tous les escrocs dans la prison du Pindaï","","","Afin de d'écraser votre courage et votre brav..."],"papy")

    affiche_ligne_dans_boite_dialogue(g, ["..."],"papy")

    affiche_ligne_dans_boite_dialogue(g, ["Petite fille : Papy, vient prendre tes médicaments, il se fait tard, tu vas prendre froid !"],"fillette")


    affiche_ligne_dans_boite_dialogue(g, ["Villageois : Bon d'accord...","","","Mais rendez-vous tous, ou vous aurez la guerre !"],"papy")

    affiche_ligne_dans_boite_dialogue(g, ["Jeu terminé >> Cliquez pour retourner à l'écran d'accueil."])

    g.dessinerRectangle(0,0,1750,900,"black")


















