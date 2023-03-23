"""
Ce fichier s'occupe de l'affichage du jeu dans la console.

Il est utilisé par les fichiers Diamants.py et fonctions.py.
"""
from medias.py.initialisation import Joueurs, Manche
from time import *
from random import choice



def vide_terminal(): print("\n" * 50)


def afg_erreur(id_erreur=None):
    """
    Principe :
        Affiche une erreur en fonction de l'identifiant reçu.
        Attend que le joueur appuie sur Entrée pour poursuivre.
    Entrée :
        id_erreur   [INT / NONE]: l'identifiant de l'erreur
                                  Si None : on affiche le message par défaut.
    Sortie :
        Aucune
    """
    vide_terminal()

    if id_erreur == 0:
        print("ERREUR >> Votre choix n'est pas valide !\nVeuillez recommencer.")
    elif id_erreur == 1:
        print(
            "ERREUR >> Votre choix n'est pas valide !\nVeuillez recommencer avec une valeur comprise entre 3 et 8 inclus.")
    elif id_erreur == 2:
        print("ERREUR >> Votre pseudonyme doit faire 1 à 12 caractères compris !")
    else:
        print("ERREUR >> Une erreur est survenu.")

    input("\nAppuyez sur ENTRÉE pour poursuivre.")


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
    vide_terminal()

    print("===================================================")
    print("|                    Diamant                      |")
    print("|                                                 |")
    print("|     Matthieu  & Tom  IUT de Vélizy     |")
    print("|    -----------------------------------------    |")
    print("| Appuyez sur la touche associée pour poursuivre  |")
    print("| 1 >> Lancer le jeu                              |")
    print("| 2 >> Lire les règles                            |")
    print("| 3 >> Quitter                                    |")
    print("===================================================")
    choix = input("> ")

    return choix


def afg_regles():
    """
    FONCTION APPELÉE PAR LA FONCTION PARTIE_DE_JEU DE DIAMANTS.PY OU AFG_ECRAN_TITRE DE CE FICHIER

    Principe :
        Affiche le menu des règles avec :
            - OPTION 1
            - OPTION ...
            - OPTION ÉCHAP  -> Quitte le menu des règles

        On rentre dans une boucle while qui s'exécute tant que choix ne correspond pas à la touche ÉCHAP
            ⇒ Input demandant un choix à l'utilisateur, stock le résultat dans "choix".

            Parcours une série de "if" jusqu'au "if" correspondant au choix de l'utilisateur
            ⇒ Si choix correspond à une des options du menu, exécute le "if" adéquat
            ⇒ Si choix correspond à la touche ÉCHAP, on arrête la boucle et on quitte la fonction
            ⇒ Sinon, on affiche un message d'erreur et on repropose le menu

    Entrée :
        Aucune
    Sortie :
        Aucune
    """


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
    vide_terminal()
    nbr_joueur = input("Combien de joueur vont-ils jouer à cette partie (de 3 à 8 joueurs): ")
    return nbr_joueur


def afg_creer_joueur_demande_pseudo(no_joueur):
    """
    FONCTION APPELÉE PAR LA FONCTION CREER_JOUEUR DE FONCTIONS.PY

    Principe :
        Demande au joueur un pseudonyme et renvoie sa réponse.
    Entrée :
        Aucune
    Sortie :
        pseudo  [STR]: Pseudonyme du joueur à intégrer dans la partie.
    """
    assert type(no_joueur) == int, "ERREUR >> Le paramètre entrée n'est pas un entier"
    assert 1 <= no_joueur <= 8, "ERREUR >> Numéro de joueur incohérent"
    pseudo = input("Quel est le pseudonyme du joueur n°" + str(no_joueur) + " (12 caractère maximum): ")
    return pseudo


def afg_tapis_de_jeu(manche):
    """
    FONCTION APPELÉE PAR LA FONCTION PARTIE_DE_JEU DE DIAMANTS.PY

    Principe :
        Affiche l'état actuel du jeu
             - Le n° de manche
            - Le banc
            - Le reste du trésor
            - Les joueurs
                → En jeu ou non
                → Diamants dans le coffre chez soi*
                → Pseudonyme

    Entrée :
        - manche    [objet MANCHE] : objet qui contient les informations sur la manche actuelle

    Sortie :
        Aucune
    """
    vide_terminal()
    print("La manche actuelle est la n°", manche.no_manche)
    print("Banc du jeu :", manche.banc)
    print("Reste de diamants dans le trésor :", manche.reste_tresor)
    for joueur in manche.liste_joueurs_dans_la_manche:
        print("Le joueur", joueur.pseudo, "est", joueur.etat, "et possède", joueur.inv_manche,
              "diamant(s) durant cette manche.")
    print("\n>> Ce message reste affiché 1 seconde.\n")
    sleep(1)


def afg_deploie_carte(carte_tiree, manche):
    """
    Affiche :
        - Le nom de la carte
        - Une icône pour le type de carte
    Entrée :
        carte_tiree             [STR] : Carte qui a été tirée
        manche               [MANCHE] : Objet qui représente la manche actuelle
    Sortie :
        Aucune
    """

    assert type(manche) == Manche
    assert carte_tiree in manche.deck.keys()

    vide_terminal()

    if carte_tiree in [1, 2, 3, 4, 5, 7, 9, 11, 13, 14, 15, 17]:
        print("💎 >> La carte tirée est une carte trésor de", carte_tiree, "diamants !")

    elif carte_tiree in ["araignées", "serpents", "laves", "boulets", "béliers"]:
        print("☠ >> La carte tirée est la carte danger", carte_tiree, "!")

    elif carte_tiree == "relique":
        print("🗿 >> La carte tirée est une relique !")

    else:
        afg_erreur()

    print("\n>> Ce message reste affiché 3 secondes.")
    sleep(3)




def afg_decision_joueur(joueur, decision):
    assert type(joueur) == Joueurs, "ERREUR GRAPHIQUE >> Paramètre 1 n'est pas un objet joueur."
    print(str(joueur.pseudo), "est", str(decision))
    sleep(0.5)


def afg_demande_decision_joueur(joueur, manche):
    assert type(joueur) == Joueurs, "ERREUR GRAPHIQUE >> Paramètre 1 n'est pas un objet de type Joueurs."
    assert type(manche) == Manche, "ERREUR GRAPHIQUE >> Paramètre 1 n'est pas un objet de type Manche."

    afg_tapis_de_jeu(manche)
    return input(
        joueur.pseudo + " vous avez " + str(
            joueur.inv_manche) + " diamants cette manche, voulez vous continuer l'exploration ou rentrer au camp ?\nAppuyez sur C pour continuer, R pour rentrer.\n> ")


def afg_accident_danger_fin_manche(carte_danger, pseudo_joueur_victime, somme_total):
    """
    Entrée :
        carte_danger                [STR] : Carte danger qui a provoqué l'accident.
        pseudo_joueur_victime       [STR] : Un joueur victime sévèrement de l'accident selon l'histoire.
        somme_total                 [INT] : Somme total de tous les diamants qu'avait les joueurs au moment de l'accident.
    """
    # Accident provoquant la fin de la manche

    assert carte_danger in ["araignées", "serpents", "laves", "boulets",
                            "béliers"], "ERREUR >> PARAMÈTRE 1 (carte_danger) INVALIDE ! Ce n'est pas une carte danger."

    # Pycharm nous demandait d'initialiser ici ces deux variables. Alors nous avons mis des valeurs par défaut.
    # Ces textes n'apparaîtront jamais dans le jeu.
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

    # ☠
    vide_terminal()
    print("===================================================")
    print(titre + "\n")
    print("☠ Avide de gloire et de fortune, vous vous êtes beaucoup trop enfoncé dans la grotte. ☠")
    print("Vous n'avez pas cru les paroles de ce villageois il y a quelques temps:")
    print(
        "\"Attention jeunes aventuriers et aventurières ! De multiple dangers dont " + pronom + " " + carte_danger + " s'y trouve !\"\n")
    print("Pris de peur, " + pseudo_joueur_victime + " a fait un malaise.")
    print("Vous avez réussit à le sauver, et juste au moment où " + evenement2 + "... Vous vous êtes enfuis.")
    input("\n>> Appuyez sur ENTRÉE pour poursuivre.")
    vide_terminal()
    print("Par la panique, vous avez oublié vos sacs...")
    print("Vous avez perdu au total " + str(somme_total) + " diamants.")
    print("===================================================")
    input("\n>> Appuyez sur ENTRÉE pour poursuivre.")
    vide_terminal()


def afg_tirer_une_carte():
    # Demande juste au joueur d'appuyer pour poursuivre
    vide_terminal()
    input(">> Appuyez sur ENTRÉE pour tirer une carte !")


def afg_lancement_manche(manche):
    # Message annonçant la nouvelle manche

    assert type(manche) == Manche, "ERREUR >> Le paramètre n'est pas un objet de type manche."

    joueur_au_pif = choice(manche.liste_joueurs_dans_la_manche).pseudo

    vide_terminal()

    if manche.no_manche == 1:
        print(
            ">> Manche 1 >> Explorateurs, exploratrices vous venez d'entrer dans l'antre de la grotte du Pindaï.\nVotre première exploration ne fait que de commencer !")
    elif manche.no_manche == 2:
        if manche.liste_manche_reussite_ou_non[0]:
            print(
                ">> Manche 2 >> Après la réussite de la première manche,\nvous décidez de vous avancer d'avantage dans la grotte...")

        else:
            print(
                ">> Manche 2 >> Votre épopée a très mal commencé.\nPar chance, " + joueur_au_pif + " a vu un petit passage durant la première quête.\n\nVous décidez alors de le suivre...")

    elif manche.no_manche == 3:
        if manche.liste_manche_reussite_ou_non.count(True) == 2:
            print(
                ">> Manche 3 >> Comme on le dit dans le milieu, jamais 2 sans 3 !\n Assuré par une certaine confiance, vous prenez cette fois-ci un chemin découvert par...\n" + joueur_au_pif + " !")

        elif manche.liste_manche_reussite_ou_non[1]:
            print(
                ">> Manche 3 >> Malgré la chance que vous avez eu en changeant de chemin, vous avez décidé de prendre son opposé.\n En effet, la grotte du Pindaï cache encore des surprises !")

        else:
            print(
                ">> Manche 3 >> Vous prenez un nouveau chemin tout en réfléchissant à ce villageois que vous détestez tant...\nAh et " + joueur_au_pif + " a faillit oublier la carte pour vous repérer...\n\nQuel tête en l'air...")

    elif manche.no_manche == 4:
        if manche.liste_manche_reussite_ou_non.count(True) == 3:
            print(
                ">> Manche 4 >> Excellent ! Fabuleux !\n Alors que vous vous esclaffer en pensant à votre bulletin et votre chance inouï...\n" + joueur_au_pif + " a oublié les sandwich...")

        elif manche.liste_manche_reussite_ou_non[0] and manche.liste_manche_reussite_ou_non.count(True) == 2:
            print(">> Manche 4 >> Jamais 2 sans 3... Bon...\nDéçus, vous continuer votre quête.")

        elif manche.liste_manche_reussite_ou_non[1]:
            print(">> Manche 4 >> La dernière exploration a été une réussite !\n Grotte du Pindaï nous revoilà !")

        else:
            print(
                ">> Manche 4 >> Après avoir mangé les sandwich préparés par " + joueur_au_pif + " vous continuez votre aventure.")

    elif manche.no_manche == 5:
        joueur_au_pif2 = choice(manche.liste_joueurs_dans_la_manche).pseudo
        while joueur_au_pif == joueur_au_pif2:
            joueur_au_pif2 = choice(manche.liste_joueurs_dans_la_manche).pseudo

        if manche.liste_manche_reussite_ou_non.count(True) == 4:
            print(
                ">> Manche 5 >> Pas le temps de réfléchir. Tout le village attend impatiemment votre retour.\nC'est avec une peur de ne pas revenir totalement vainqueur, que vous poursuivez...\n\nAvec un peu de chance, vous aurez du chocolat chaud à votre retour !")

        if manche.liste_manche_reussite_ou_non.count(True) == 3:
            print(
                ">> Manche 5 >> Bon. Vous avez échoué une fois.\nMais vous y êtes presque !\n" + joueur_au_pif + ", faites attention, " + joueur_au_pif2 + " réfléchi à comment vous piquez vos diamants...")

        if manche.liste_manche_reussite_ou_non.count(True) == 2:
            print(
                ">> Manche 5 >> Aurez vous plus gagné que perdu durant l'aventure ?\nTel est la question...\n\nDes diamants vous attende pour cette dernière quête. Nouveau chemin et z'est partizz !")

        else:
            print(
                ">> Manche 5 >> " + joueur_au_pif + " dessine une cinquième barre. " + joueur_au_pif2 + " pleure.\n Serpents, béliers, boulets... Et la même critique du villageois qui reviens.\n Avant d'abandonné l'aventure, vous reprenez courage et vous poursuivez la quête...\n\nMais par une autre entrée !")

    input("\n>> Appuyez sur ENTRÉE pour poursuivre.")
    vide_terminal()


def afg_fin_jeu_histoire_1(tableau_des_scores, partie_terminer):
    # Affiche une petite histoire pour la fin de la partie

    # tableau_des_scores    [LIST > JOUEURS] : classé du plus mauvais au meilleur joueur
    # partie_terminer               [MANCHE] : Objet manche (n° 6) représentant la partie terminée.

    # Retourne STOP                    [STR] : Dans un cas particulier, si les joueurs ne veulent pas suivre l'histoire.

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

    vainqueur = tableau_des_scores[len(tableau_des_scores)-1]
    vide_terminal()
    print("...")

    continuer = input("\n>> Appuyez sur ENTRÉE pour poursuivre. | Ou tapez STOP juste avant si vous souhaitez passer directement aux statistiques.")

    if continuer.upper() == "STOP":  # Si le joueur ne veut pas afficher l'histoire
        return

    vide_terminal()

    print(J1 + ": On est bientôt arrivé ?\n")
    sleep(1)

    print(J2 + ": Oui !")
    sleep(0.5)
    print((" " * len(J2) + "  Je vois la lueur de l'épicier du coin de ma rue !\n"))
    sleep(2)

    print("Villageois: Alors, vous avez eu combien de problème au total ? hé hé hé\n")
    sleep(2)

    print(J3 + ": " + str(partie_terminer.liste_manche_reussite_ou_non.count(False)) + "\n")
    sleep(2)

    if partie_terminer.liste_manche_reussite_ou_non.count(False) == 0:
        print("Villageois: Comment est-ce possible, seriez-vous les élus ?\n")
    elif partie_terminer.liste_manche_reussite_ou_non.count(False) == len(partie_terminer.liste_manche_reussite_ou_non):
        print("Villageois: Félicitation ah ah ah !")
        print("            J'étais sûr que vous n'y arriverez pas.\n")
    else:
        print("Villageois: Je vous avais prévenu 😈 ! Niark niark niark\n")
    sleep(2)

    print(eleve_classe+": Comment allez-vous, alors qui a ramené le plus de diamant ?\n")
    sleep(2)

    if J1 == vainqueur.pseudo:  # Cas où celui qui parle est celui qui a remporté la partie
        print(J1+": C'est...", end =" ")
        sleep(0.5)
        print("MOI !")
        sleep(1)
        print(" " * len(J1) +"  Avec "+str(vainqueur.inv_partie)+" diamants !\n")
    else:
        print(J1+": C'est...", end =" ")
        sleep(0.5)
        print(str(tableau_des_scores[0].pseudo)+" !")
        sleep(1)
        print(" " * len(J1) +"  Avec "+str(vainqueur.inv_partie)+" diamants !\n")
    sleep(2)

    if vainqueur.inv_partie == 0:
        print(eleve_classe + ": Dommage...")
    else:
        print(eleve_classe+": Bravo !")
    sleep(0.5)
    print(" " * len(eleve_classe) + "  Vous prendrez un peu de chocolat chaud ?")
    sleep(1)
    print(" " * len(eleve_classe) + "  Tout le village sauf l'autre villageois là vous attend.\n")
    sleep(2)

    print(J2 + ": Volontier !\n")
    sleep(1)

    print(J3 + ": Allons-y !")
    sleep(2)

    input("\n\n>> Appuyez sur ENTRÉE pour poursuivre.")

    vide_terminal()


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

    vide_terminal()
    print("NARRATEUR: Et c'est ainsi que se termine votre épopée dans la grotte du Pindaï...\n\n")
    sleep(2)

    print("NARRATEUR: Au total, votre aventure c'est...")
    sleep(1)

    print("           - " + str(reussites) + " manches de réussites") if reussites > 1 else print("           - "+str(reussites)+" manche de réussite")
    sleep(0.5)
    print("           - " + str(defaites) + " manches d'échouées") if defaites > 1 else print("           - " + str(defaites) + " manche d'échoué")
    sleep(0.5)
    print("           - " + str(total_diams) + " diamants récupérés") if total_diams > 1 else print("           - " + str(total_diams) + " diamant récupéré")
    sleep(0.5)
    print("           - " + str(reliques_sorties) + " reliques qui ont été récupérées") if reliques_sorties > 1 else print("           - " + str(reliques_sorties) + " relique qui a été récupéré")
    sleep(2)

    print("\nNARRATEUR: Mais également...", end = " ")
    sleep(0.5)
    print("des accidents...\n")
    sleep(0.5)

    print("NARRATEUR: Avec:")
    print("           ")

    il_y_a_pas_eu_de_probleme = True
    l_dangers = partie_terminer.dangers_a_retirer
    for danger in l_dangers:
        if danger == "araignées" and l_dangers[danger] > 0:
            print("           "+str(l_dangers[danger])+" fois où des araignées mutantes qui voulaient vous digérer")
            il_y_a_pas_eu_de_probleme = False
            sleep(0.5)
        if danger == "serpents" and l_dangers[danger] > 0:
            print("           "+str(l_dangers[danger])+" fois où des serpents jaune fluo qui voulaient vous aveugler à vie")
            il_y_a_pas_eu_de_probleme = False
            sleep(0.5)
        if danger == "laves" and l_dangers[danger] > 0:
            print("           "+str(l_dangers[danger])+" fois où de la lave à faillit vous carboniser")
            il_y_a_pas_eu_de_probleme = False
            sleep(0.5)
        if danger == "boulets" and l_dangers[danger] > 0:
            print("           "+str(l_dangers[danger])+" fois où des boulets vous ont frôlé")
            il_y_a_pas_eu_de_probleme = False
            sleep(0.5)
        if danger == "béliers" and l_dangers[danger] > 0:
            print("           "+str(l_dangers[danger])+" fois où des béliers déchaînés ont essayés de vous éventrer")
            il_y_a_pas_eu_de_probleme = False
            sleep(0.5)
        sleep(0.5)

    if il_y_a_pas_eu_de_probleme:
        print("           Aucune égratignure, en effet, vous avez échappé au pire !\n\n")

        sleep(1)

        print("Villageois: Briguant, au voleur !", end = " ")
        sleep(0.5)
        print("A l'assassin, au meurtrier !\n\n\n")

        sleep(3)

    print("NARRATEUR: Voici le tableau des scores:")

    for score in range(len(tableau_des_scores)-1,-1,-1):
        score_afficher = len(tableau_des_scores) - score
        print("            ", end = "")
        print("  "+str(score_afficher)+". "+tableau_des_scores[score].pseudo+" avec "+str(tableau_des_scores[score].inv_partie)+" diamants et "+str(tableau_des_scores[score].inv_relique)+" reliques")
        sleep(0.5)

    entree = input("\n\n>> Appuyez sur ENTRÉE pour poursuivre. | Ou tapez STOP juste avant pour retourner directement sur l'écran titre")

    vide_terminal()

    return entree.upper()


def afg_fin_jeu_remerciement_3():
    vide_terminal()

    print("NARRATEUR: Merci d'avoir joué à ce jeu.")
    print("           De jeunes personnes qui sont Matthieu  et Tom  ont fait un travaille acharné dessus.")
    print("           Nous espérons que vous avez passé un excellent moment !\n")

    print("N'hésitez pas à relancer une partie pour une toute nouvelle aventure inédite !\n\n\n")

    sleep(2)
    print("Villageois: Ne vous en fait pas, je serais de retour pour vous faire un mauvais tour !")
    sleep(1)
    print("            Afin de préserver le monde des voleurs")
    sleep(1)
    print("            Afin de rallier tous les escrocs dans la prison du Pindaï")
    sleep(1)
    print("            Afin de d'écraser votre courage et votre brav...")
    sleep(1)

    print("...\n\n")

    sleep(3)
    print("Petite fille : Papy, vient prendre tes médicaments, il se fait tard, tu vas prendre froid !\n\n")

    sleep(2)
    print("Villageois : Bon d'accord...")
    sleep(1)
    print("             Mais rendez-vous tous, ou vous aurez la guerre !")
    sleep(2)

    input("Jeu terminé >> Appuyez sur ENTRÉE pour retourner à l'écran d'accueil.")
    pass

def afg_regles():
    """
    Principe :
        Présente le jeu
    Entrée, Sortie :
        Aucune
    """

    print("Présentation du jeu, tiré du document fourni par l'établissement, pour nous présenter la SAÉ:\n")
    print("Le principe du jeu est simple, se jouant essentiellement avec des cartes et quelques jetons.")
    print("Le mécanisme du jeu est dit de « stop ou encore » :")
    print("A chaque étape, les joueurs doivent décider s’ils sécurisent leur gain, ou s’ils prennent des risques pour\ngagner davantage, au risque de tout perdre !\n")

    print("L’un des joueurs doit piocher une carte, et celle-ci apparaît a l’écran.")
    print("Les joueurs auront ensuite le choix  entre continuer l’aventure, ou retourner au campements.")
    print("S’il n’y a plus de joueur en exploration ou qu’il y a eu un accident juste avant, alors le jeu enchaine vers la prochaine manche\n")

    input("\n>> Appuyez sur ENTRÉE pour retourner sur l'écran titre")