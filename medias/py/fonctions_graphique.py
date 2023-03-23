# Ce fichier contient des fonctions graphiques qui seront utilisées pour l'affichage.

from medias.py.tkiteasy import *
from medias.py.initialisation import Joueurs

DIMENSION_X_FEN, DIMENSION_Y_FEN = 1750, 900

def boite_de_dialogue(g, texte, personne=None, message_long = 0):
    global DIMENSION_X_FEN, DIMENSION_Y_FEN
    """
    Principe :
        Ouvre une boîte de dialogue, affiche le texte demandé puis referme la boîte.
    Entrée :
        g                             : Fenêtre de jeu
        texte                   [STR] : Texte qui sera affiché dans la boîte de dialogue
        personne        [STR/JOUEURS] : Personne qui parle
                                            → Soit un joueur (JOUEURS)
                                            → Soit un personnage fictif, le narrateur, ou le journal (STR)
        message_long            [INT] : 0 → C'est un message pouvant se tenir sur une seule boîte de dialogue
                                        1 → C'est la première parti d'un message long (contraire de 0)
                                        2 → C'est la partie du milieu du message long
                                        3 → C'est la fin de ce message long
    Sortie :
        Aucune
    """
    assert type(g) == Canevas, "ERREUR >> PARAMÈTRE 1 n'est pas un objet Canvas"
    assert type(texte) == str, "ERREUR >> PARAMÈTRE 2 n'est pas un texte au format str"
    assert type(personne) == Joueurs or type(personne) == str or personne is None, "ERREUR >> PARAMÈTRE 3 n'est pas valide"

    TAILLE_FOND = [1225,255]  # X, Y
    POS_X_FD = DIMENSION_X_FEN // 2 - TAILLE_FOND[0] // 2
    POS_Y_FD = DIMENSION_Y_FEN - TAILLE_FOND[1] - 20

    image = "unknowb"
    if personne == "joueur1":
        image = "Perso2"
    elif personne == "joueur2":
        image = "Perso5"
    elif personne == "joueur3":
        image = "Perso3"
    elif personne == "journal":
        image = "journal"
    elif personne == "narration":
        image = "grotteb"
    elif personne == "papy":
        image = "Perso6"
    elif personne == "papy_paroles":
        image = "Perso6b"
    elif personne == "fillette":
        image = "Perso7"
    elif personne == "villageois":
        image = "Perso4"
    elif personne == "inconnu":
        image = "Perso1"



    elements_boite_dialogue = []
    elements_boite_dialogue.append(g.afficherImage(0, 0, "medias/img/effet_bas_noir_transparent.png"))
    elements_boite_dialogue.append(g.afficherImage(300, 300, "medias/img/"+image+".png"))
    elements_boite_dialogue.append(g.afficherImage(POS_X_FD, POS_Y_FD, "medias/img/fond_dialogue.png"))


    #32 cara max // 52 en minuscule
    elements_boite_dialogue.append(g.afficherTextePlus(texte, DIMENSION_X_FEN // 2, POS_Y_FD + 130,
                        "black", 25, "Papyrus", "bold"))


    g.actualiser()

    clic = g.recupererClic()
    touche = g.recupererTouche()
    temps = 0

    while clic is None and touche is None:  # Tant que le joueur n'appui pas sur un bouton ou une touche
        clic = g.recupererClic()
        touche = g.recupererTouche()

        if message_long == 1 or message_long == 2:  # Si on doit indiquer qu'il y a une nouvelle boîte de dialogue qui suit celle-ci, pour le même paragraphe.
            temps += 1
            if temps > 20:
                for i in elements_boite_dialogue:  # On supprime tout l'affichage
                    g.supprimer(i)

                # On le remet (pour écraser la flèche)
                elements_boite_dialogue = []
                elements_boite_dialogue.append(g.afficherImage(0, 0, "medias/img/effet_bas_noir_transparent.png"))
                elements_boite_dialogue.append(g.afficherImage(300, 300, "medias/img/" + image + ".png"))
                elements_boite_dialogue.append(g.afficherImage(POS_X_FD, POS_Y_FD, "medias/img/fond_dialogue.png"))

                # On affiche le texte
                elements_boite_dialogue.append(g.afficherTextePlus(texte, DIMENSION_X_FEN // 2, POS_Y_FD + 130,
                                                                   "black", 25, "Papyrus", "bold"))

                # On supprime la flèche
                g.supprimer(fleche)
            else:
                fleche = g.afficherImage(POS_X_FD + 1150,POS_Y_FD + 190, "medias/img/fleche_suivant.png")       # On place la flèche

            if temps > 30:  # Pour éviter de stocker une valeur trop élever, on la reset régulièrement
                temps = 0






    for i in elements_boite_dialogue:
       g.supprimer(i)




def decoupage_texte(texte):
    """
    Principe :
    On réajuste
    Le paragraphe à la boîte de dialogue.
    Si une phrase est trop grande, alors on la coupe.

    Le découpage est basé sur le nombre de caractères W et w qu'on peut mettre
    avant de déplacer la boîte de dialogue.
    W et w étant les caractères prenant le plus de place à l'affichage de l'alphabet

    Entrée :
        texte               [STR] : Texte à découper
    Sortie :
        texte_decouper     [LIST] : Liste contenant les extraits du texte
    """

    texte_decouper = []
    point_debut_txt = 0


    taille_ligne = 0
    pos_dernier_espace = -1
    for caractere in range(len(texte)):
        if texte[caractere].isupper():
            taille_ligne += 1.625  # Place que prend une lettre majuscule sur le dialogue
        else:
            taille_ligne += 0.95  # Place que prend une lettre minuscule sur le dialogue

        if texte[caractere] == " ":
            pos_dernier_espace = caractere

        if taille_ligne > 52:
            if pos_dernier_espace != -1:
                taille_ligne = 0

                texte_decouper.append(texte[point_debut_txt:pos_dernier_espace])
                point_debut_txt = pos_dernier_espace+1
            else:
                taille_ligne = 0
                texte_decouper.append(texte[point_debut_txt:caractere])
                point_debut_txt = caractere

    texte_decouper.append(texte[point_debut_txt:len(texte)])
    return texte_decouper


def affiche_ligne_dans_boite_dialogue(g, ensemble_texte_brouillon, personne=None):
    """
    Principe :
        Regroupe les phrases (éléments de la liste ensemble_texte) pour un affichage
        dans la boîte de dialogue.
    Entrée :
        g                             : Fenêtre de jeu
        ensemble_texte_brouillon    [LIST > STR] : Liste qui contient des textes
        personne            [STR/JOUEURS] : Personne qui parle
                                                → Soit un joueur (JOUEURS)
                                                → Soit un personnage fictif, le narrateur, ou le journal (STR)
    Sortie :
    """

    ensemble_texte = []


    for ligne in ensemble_texte_brouillon:
        ensemble_texte += decoupage_texte(ligne)

    if len(ensemble_texte) > 3:
        message_long = 1

    for ligne in range(0,len(ensemble_texte),3):
        if ligne < len(ensemble_texte) - 2:
            if ligne+4 > len(ensemble_texte):
                message_long = 0
            boite_de_dialogue(g, ensemble_texte[ligne] + "\n" + ensemble_texte[ligne+1] + "\n" + ensemble_texte[ligne+2], personne, message_long)

        elif ligne < len(ensemble_texte) - 1:
            message_long = 0
            boite_de_dialogue(g, ensemble_texte[ligne] + "\n" + ensemble_texte[ligne+1], personne, message_long)

        else:
            message_long = 0
            boite_de_dialogue(g, ensemble_texte[ligne], personne, message_long)
        if message_long == 1:
            message_long += 1



    print(ensemble_texte)
    return ensemble_texte
    #for ligne in ensemble_texte
