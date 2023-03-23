"""
Ce fichier contient les variables et objets initialisés pour le jeu.
Les variables/objets peuvent être modifiés au cours de la partie.

Il est utilisé par le fichier Diamants.py et fonctions.py.
"""
from random import *

print("Chargement des composants 1/2 du jeu...")

# Si True, affiche les informations de débogage des classes Joueurs et Manche
debug: bool = False


class Joueurs:
    """
    Chaque objet représente un joueur.
    Ses informations, mais également son état.
    """

    def __init__(self, no_joueur, pseudonyme):
        assert type(no_joueur) == int, "ERREUR >> Le premier paramètre doit être un entier !"
        assert type(pseudonyme) == str, "ERREUR >> Le deuxième paramètre doit être un texte !"
        assert no_joueur >= 0, "ERREUR >> Le numéro de joueur n'est pas valide."

        self.__no_joueur = no_joueur  # N° associé au joueur
        self.__pseudonyme = pseudonyme  # Pseudo du joueur
        self.__inv_manche = 0  # Le nombre de diamants récupérer durant la manche
        self.__inv_partie = 0  # Le nombre de diamants protéger dans son repaire
        self.__etat = "En_Jeu"  # L'état du joueur dans la partie : [En_jeu/Partie]
        self.__inv_relique = 0  # Le nombre de reliques récupérés par le joueur

        if debug:
            print('DEBUG >> Objet "' + str(pseudonyme) + '" a été crée')

    # Méthodes uniquement pour le débogage :  --------------------------------------------------------------------------
    def debogage(self):
        # Affiche les informations sur l'objet. Indique que le mode debug est inactif, si désactivé.
        if debug:
            print("DEBUG >>", str(self.__no_joueur), str(self.__pseudonyme), str(self.__inv_manche),
                  str(self.__inv_partie), str(self.__etat))
        else:
            print("DEBUG >> Le mode n'est pas activé !")

    def set_enleve_inv_partie_DEBUG(self, nb_diamants=1):
        """
        Principe :
            Retire à l'inventaire permanent des diamants (coffre du joueur) UNIQUEMENT EN MODE DEBUG
        Entrée :
            nb_diamants     [INT] : Nombre de diamants à retirer
        Sortie :
            Aucune
        """

        if not debug:
            print("DEBUG >> Le mode n'est pas activé !")
            return

        assert type(nb_diamants) == int, "ERREUR >> Le paramètre n'est pas valide."
        assert nb_diamants >= 0, "ERREUR >> La valeur doit être supérieur ou égal à 0."
        assert nb_diamants <= self.__inv_partie, "ERREUR >> Le joueur ne possède pas autant de diamants !"

        self.__inv_partie -= nb_diamants

        if debug:
            print("DEBUG >> Diamants enlevés au coffre de " + str(self.pseudo) + ": " + str(nb_diamants))

    # Les getters ------------------------------------------------------------------------------------------------------
    # On récupère les valeurs des attributs.

    @property
    def no_joueur(self):
        return self.__no_joueur

    @property
    def pseudo(self):
        return self.__pseudonyme

    @property
    def inv_manche(self):
        return self.__inv_manche

    @property
    def inv_partie(self):
        return self.__inv_partie

    @property
    def etat(self):
        return self.__etat

    @property
    def inv_relique(self):
        return self.__inv_relique

    # Les setters ------------------------------------------------------------------------------------------------------
    # Ces méthodes manipulent le plus simplement possible les attributs.
    # Si on souhaite modifier les attributs par une autre méthode ou par une fonction, il faudra obligatoirement passer par là.
    # Elles contiennent les tests basiques permettant à ce que l'utilisation des attributs soit cohérente.

    def set_ajout_inv_manche(self, nb_diamants=1):
        """
        Principe :
            Ajoute à l'inventaire éphémère des diamants
        Entrée :
            nb_diamants     [INT] : Nombre de diamants à ajouter
        Sortie :
            Aucune(
        """
        assert type(nb_diamants) == int, "ERREUR >> Le paramètre n'est pas valide."
        assert nb_diamants >= 0, "ERREUR >> La valeur doit être supérieur ou égal à 0."
        self.__inv_manche += nb_diamants

        if debug:
            print("DEBUG >> Diamants ajoutés au sac de " + str(self.pseudo) + ": " + str(nb_diamants))

    def set_reset_inv_manche(self):
        """
        Principe :
            Réinitialise l'inventaire éphémère du joueur
        Entrée et Sortie :
            Aucune
        """
        self.__inv_manche = 0
        if debug:
            print("DEBUG >> L'inventaire de manche de " + str(self.pseudo) + " a été reset.")

    def set_ajout_inv_partie(self, nb_diamants=1):
        """
        Principe :
            Ajoute à l'inventaire permanent des diamants (coffre du joueur)
        Entrée :
            nb_diamants     [INT] : Nombre de diamants à ajouter
        Sortie :
            Aucune
        """
        assert type(nb_diamants) == int, "ERREUR >> Le paramètre n'est pas valide."
        assert nb_diamants >= 0, "ERREUR >> La valeur doit être supérieur ou égal à 0."
        self.__inv_partie += nb_diamants

        if debug:
            print("DEBUG >> Diamants ajoutés au coffre de " + str(self.pseudo) + ": " + str(nb_diamants))

    def set_etat(self, nouvel_etat):
        """
        Principe :
            Modifie l'état du joueur dans la partie.
            S'il est encore en jeu → En_Jeu
            S'il est partie → Partie

            ATTENTION : Cette modification ne concerne uniquement que le profil du joueur.
                        Elle n'agit donc pas sur une autre partie du jeu.
        Entrée :
            nouvel_etat     [STR] : Indique le nouvel état du joueur En_Jeu/Sortie
        Sortie :
            Aucune
        """
        assert nouvel_etat in ("En_Jeu", "Sortie"), "ERREUR >> Le paramètre doit être: En_Jeu (OU) Sortie."
        assert nouvel_etat != self.__etat, "ERREUR >> Le joueur est déjà dans cet état !"

        self.__etat = nouvel_etat

        if debug:
            print("DEBUG >> Le joueur " + str(self.pseudo) + " est désormais " + str(self.__etat) + ".")
            print("         RAPPEL: la méthode ne vérifie pas la cohérence entre le jeu et la modification.")

    def set_ajout_inv_relique(self):
        """
        Principe :
            Ajoute à l'inventaire permanent une relique
        Entrée :
            Aucune
        Sortie :
            Aucune
        """

        self.__inv_relique += 1

    # Les méthodes -----------------------------------------------------------------------------------------------------
    # Attention !
    # Les méthodes ne sont que complémentaire aux fonctions.
    # Elles s’occupent des actions concernant l’objet.
    # Elles ne s’occupent donc pas de l’état du jeu.

    def preparatif_nouvelle_manche(self, manche_remporter, change_etat_oui_non=True):
        """
        Principe :
            Prépare l'objet joueur pour la nouvelle manche.

            En fonction de si le joueur a remporté la manche (s'il a quitté volontairement, ou s'il a été mis K.O. par un danger),
            il garde ou non le trésor dans son sac qu'il a récupéré durant la manche.

            Puis, la méthode réinitialise son état à En_Jeu, et réinitialise son sac.
        Entrée :
            manche_remporter        [BOOL] :    True  → Le joueur a remporté la manche, il l'a quitté volontairement.
                                                False → Le joueur a été mis K.O. par un danger
            change_etat_oui_non     [BOOL] :    True  → On met l'état du joueur à En_Jeu (par défaut)
                                                False → On ne change pas l'état du joueur
                                                ► Dans le cas où les joueurs retourne au campement volontairement,
                                                  pour éviter de les remettre involontairement à "En_Jeu.
        Sortie :
            Aucune
        """
        assert type(
            manche_remporter) == bool, "ERREUR >> PARAMÈTRE 1 (manche_remporter) invalide ! Ca doit être un booléen (True (OU) False)"
        assert type(
            manche_remporter) == bool, "ERREUR >> PARAMÈTRE 2 (change_etat_oui_non) invalide ! Ca doit être un booléen (True (OU) False)"

        if manche_remporter:
            if debug:
                print("DEBUG PNM >> Extraction de l'inventaire manche (sac) vers l'inventaire de la partie (coffre)")
            self.set_ajout_inv_partie(self.inv_manche)

        self.set_reset_inv_manche()
        if debug:
            print("DEBUG PNM >> Reset de l'inventaire manche (sac)")

        if self.etat != "En_Jeu" and change_etat_oui_non == True:
            self.set_etat("En_Jeu")
            if debug:
                print("DEBUG PNM >> Changement de l'état du joueur en En_Jeu")

        elif debug:
            print("DEBUG PNM >> L'état du joueur reste " + str(self.etat))

        if change_etat_oui_non:  # Normalement cette vérification est inutile. Mais au cas où.
            assert self.etat == "En_Jeu", "ERREUR >> Le joueur n'a pas été remis en jeu !"

        if debug:
            print("DEBUG PNM >> Exécution avec succès --------")


class Manche:
    """
    Chaque objet représente une manche.
    La plupart des données de l'objet sont éphémères, mais important pour le fonctionnement du jeu
    """

    def __init__(self, deck, liste_joueurs, no_manche=1, nb_relique_sortie=0, dangers_a_retirer=None, liste_manche_reussite_ou_non=[]):
        if dangers_a_retirer is None:
            dangers_a_retirer = {"araignées": 0, "serpents": 0, "laves": 0, "boulets": 0, "béliers": 0}
        assert type(deck) == dict, "ERREUR >> PARAMÈTRE 1 (DECK) EST INVALIDE. -> Doit être un dictionnaire"
        assert type(liste_joueurs) == list, "ERREUR >> PARAMÈTRE 2 (LISTE_JOUEURS) EST INVALIDE. -> Doit être une liste"
        assert type(no_manche) == int, "ERREUR >> PARAMÈTRE 3 (NO_MANCHE) EST INVALIDE. -> Doit être un entier"
        assert type(
            nb_relique_sortie) == int, "ERREUR >> PARAMÈTRE 4 (NB_RELIQUE_SORTIE) EST INVALIDE. -> Doit être un entier"
        assert type(
            dangers_a_retirer) == dict, "ERREUR >> PARAMÈTRE 5 (DANGERS_A_RETIRER) EST INVALIDE -> Doit être un dictionnaire"
        self.__verif_validiter_liste_joueurs(
            liste_joueurs)  # Vérifie que la liste des joueurs contient que des objets joueurs.
        self.__verif_validiter_dangers_a_retirer(
            dangers_a_retirer)  # Vérifie que les éléments du dictionnaire sont bien valides.
        assert 1 <= no_manche <= 6, "ERREUR >> PARAMÈTRE 3 (no manche) doit être compris entre 1 et 5 inclus."
        assert 0 <= nb_relique_sortie <= 5, "ERREUR >> PARAMÈTRE 4 (NB_RELIQUE_SORTIE) doit être compris entre 0 et 5 inclus"

        self.__no_manche = no_manche  # N° de manche.
        self.__liste_joueurs = liste_joueurs  # Liste des objets joueurs.
        self.__etat_joueurs_dans_la_manche = ["En_Jeu"] * len(
            self.__liste_joueurs)  # Liste l'état des joueurs (En_Jeu/Partie).
        self.__banc = []  # Cartes sorties.
        self.__deck = deck  # Deck de carte qui peuvent être pioché.
        self.__reste_tresor = 0  # Le reste des trésors qui n'ont pas été distribué.
        self.__liste_valeur_relique_banc = [5, 5, 5, 10, 10]  # Liste de manière globale les valeurs des reliques.
        self.__nb_relique_sortie = nb_relique_sortie  # Indicateur du nombre de reliques sorties durant le jeu.
        self.__dangers_a_retirer = dangers_a_retirer  # Liste chaque exemplaire de carte danger qui ont provoqué la fin d'une manche.
        self.__manche_en_cours = True  # Indique si la manche est en cours d'utilisation (si elle n'est pas terminée).
        self.__liste_manche_reussite_ou_non = liste_manche_reussite_ou_non  # Contiendra True à la position X si la manche X-1 a été un succès, False sinon.

    # Méthodes uniquement pour le débogage :  --------------------------------------------------------------------------

    def debogage(self):
        # Affiche les informations sur l'objet. Indique que le mode debug est inactif, si désactivé.
        if debug:
            print("DEBUG >>", str(self.no_manche), str(self.etat_joueurs_dans_la_manche), str(self.banc),
                  str(self.reste_tresor), str(self.liste_valeur_relique_banc),
                  str(self.nb_relique_sortie), str(self.deck))
        else:
            print("DEBUG >> Le mode n'est pas activé !")

    # Les getters ------------------------------------------------------------------------------------------------------
    # On récupère les valeurs des attributs.

    @property
    def no_manche(self):
        return self.__no_manche

    @property
    def banc(self):
        return self.__banc

    @property
    def deck(self):
        return self.__deck

    @property
    def reste_tresor(self):
        return self.__reste_tresor

    @property
    def liste_valeur_relique_banc(self):
        return self.__liste_valeur_relique_banc

    @property
    def nb_relique_sortie(self):
        return self.__nb_relique_sortie

    @property
    def etat_joueurs_dans_la_manche(self):
        return self.__etat_joueurs_dans_la_manche

    @property
    def liste_joueurs_dans_la_manche(self):
        return self.__liste_joueurs

    @property
    def nb_joueur_actif(self):
        return self.etat_joueurs_dans_la_manche.count("En_Jeu")

    @property
    def dangers_a_retirer(self):
        return self.__dangers_a_retirer

    @property
    def manche_en_cours(self):
        return self.__manche_en_cours

    @property
    def liste_manche_reussite_ou_non(self):
        return self.__liste_manche_reussite_ou_non

    # Les setters ------------------------------------------------------------------------------------------------------
    # Ces méthodes manipulent le plus simplement possible les attributs.
    # Si on souhaite modifier les attributs par une autre méthode ou par une fonction, il faudra obligatoirement passer par là.
    # Elles contiennent les tests basiques permettant à ce que l'utilisation des attributs soit cohérente.

    def set_ajoute_carte_banc(self, nom_carte):
        """
        Principe :
            Ajoute une carte au banc
        Entrée :
            nom_carte   [STR] : nom de la carte à ajouter parmi une sélection de carte (dangers et reliques)
        Sortie :
            Aucune
        """
        assert nom_carte in ("araignées", "serpents", "laves", "boulets", "béliers", "relique"), "ERREUR >> Carte " \
                                                                                                 "invalide ! "
        self.__banc.append(nom_carte)

        if debug:
            print("DEBUG >> Carte " + str(nom_carte) + " a été ajoutée au banc.")

    def set_enleve_carte_banc(self, nom_carte, nombre):
        """
        Principe :
            Retire une carte au banc
        Entrée :
            nom_carte   [STR] : nom de la carte à retirer du banc parmi une sélection de carte (dangers et reliques)
            nombre      [INT] : Nombre d'exemplaires de carte à retirer du banc
        Sortie :
            Aucune
        """
        assert nom_carte in (
            "araignées", "serpents", "laves", "boulets", "béliers", "relique"), "ERREUR >> Carte invalide !"

        assert nom_carte in self.banc, "ERREUR >> La carte à enlever n'est pas dans le banc !"
        assert nombre >= 1, "ERREUR, Vous devez enlever au moins une carte !"
        assert nombre <= self.banc.count(nom_carte), "ERREUR >> Il n'y a pas assez d'exemplaire' dans le banc !"

        # On supprime une à une chaque exemplaire de la carte
        for i in range(nombre):
            self.__banc.remove(nom_carte)

        if debug:
            print("DEBUG >> " + str(nombre) + " carte(s) " + str(nom_carte) + " a/ont été enlevée(s) du banc.")

    def set_enleve_carte_deck(self, nom_carte):
        """
        Principe :
            Retire une carte au deck
        Entrée :
            nom_carte   [STR] : nom de la carte à retirer du deck
        Sortie :
            Aucune
        """
        # On change le format de nom_carte (STR en INT) si c'est une carte trésor.
        # Pour les cartes trésor, la méthode ne peut pas travailler si c'est du texte.
        if type(nom_carte) == str:
            if nom_carte.isdigit():
                nom_carte = int(nom_carte)  # Si en réalité, c'est un entier, alors ont convertie.

        assert nom_carte in self.__deck, "ERREUR >> Carte invalide"
        assert self.deck[nom_carte] >= 1, "ERREUR >> Il n'y plus cette carte dans le deck."
        self.__deck[nom_carte] -= 1

        if debug:
            print("DEBUG >> Carte " + str(nom_carte) + " a été retirée du deck")

    def set_ajoute_diamant_tresor(self, nombre=0):
        """
        Principe :
            Ajoute des diamants au trésor (diamants qui n'ont pas pu être distribué)
        Entrée :
            nombre      [INT] : Nombre de diamants à rajouter.
        Sortie :
            Aucune
        """
        assert type(nombre) == int, "ERREUR >> Le paramètre doit être un entier !"
        assert nombre >= 0, "ERREUR >> Le paramètre doit être supérieur ou égal à 0 !"

        self.__reste_tresor += nombre

        if debug:
            print("DEBUG >> " + str(nombre) + " diamants ont été ajoutés au trésor.")

    def set_enleve_diamant_tresor(self, nombre=1):
        """
        Principe :
            Retire des diamants au trésor
        Entrée :
            nombre      [INT] : Nombre de diamants à retirer.
        Sortie :
            Aucune
        """
        assert type(nombre) == int, "ERREUR >> Le paramètre doit être un entier !"
        assert nombre >= 0, "ERREUR >> Le paramètre doit être supérieur ou égal à 0 !"
        assert nombre <= self.reste_tresor, "ERREUR >> Il n'y a pas assez de diamants dans le trésor !"

        self.__reste_tresor -= nombre

        if debug:
            print("DEBUG >> " + str(nombre) + " diamants ont été retirés du trésor.")

    def set_ajoute_relique_sortie(self, nombre=1):
        """
        Principe :
            Ajoute le nombre de reliques supplémentaire qui sont retirées de la partie.
            Entre autre, car elles ont été distribuées aux joueurs.
        Entrée :
            nombre      [INT] : Nombre de reliques à retirer du jeu
        Sortie :
            Aucune
        """

        assert type(nombre) == int, "ERREUR >> Le paramètre doit être un entier !"
        assert nombre >= 1, "ERREUR >> Le paramètre doit être supérieur ou égal à 1 !"

        nb_relique_encore_en_jeu = len(self.__liste_valeur_relique_banc) - self.__nb_relique_sortie

        assert nombre <= nb_relique_encore_en_jeu, "Il n'est pas possible de retirer autant de relique !"

        self.__nb_relique_sortie += nombre

        if debug:
            print("DEBUG >> " + str(nombre) + " relique(s) a/ont été retiré(s) du jeu. Il en reste " + str(
                nb_relique_encore_en_jeu - nombre) + ".")

    def set_etat_joueur_dans_la_manche(self, no_joueur, etat="Sortie"):
        """
        Principe :
            Modifie la présence du joueur au sein de la manche.
            S'il est encore présent (En_Jeu) ou partie (Sortie).

        Entrée :
            no_joueur       [INT] : Numéro du joueur dont on va modifier son état
            etat            [STR] : Le nouvel état du joueur (En_Jeu ou Sortie)
        Sortie :
            Aucune
        """

        assert type(no_joueur) == int, "ERREUR >> Le paramètre 1 doit être un entier !"
        assert no_joueur >= 0, "Le joueur n'existe pas !"
        assert no_joueur < len(self.etat_joueurs_dans_la_manche), "Le joueur n'existe pas !"
        assert type(etat) == str, "ERREUR >> Le paramètre 2 doit être un texte !"
        assert etat in ("En_Jeu", "Sortie"), "ERREUR >> La paramètre 2 doit être En_Jeu (OU) Sortie."
        assert etat != self.etat_joueurs_dans_la_manche[no_joueur], "ERREUR >> Le joueur est déjà dans cet état."

        self.__etat_joueurs_dans_la_manche[no_joueur] = etat
        self.__liste_joueurs[no_joueur].set_etat(etat)

        if debug:
            print("DEBUG >> Le joueur n°" + str(no_joueur) + " est désormais " + str(etat) + ".")

    def set_ajoute_dangers_a_retirer(self, danger_a_enlever):
        """
        Principe :
            Ajoute un exemplaire du danger qui doit être retiré du deck du jeu (toutes les manches)
            Met à jour le dictionnaire dangers_a_retirer
        Entrée :
            danger_a_enlever        [STR] : Exemplaire du danger à retirer du jeu
        Sortie :
            Aucune
        """

        assert danger_a_enlever in ["araignées", "serpents", "laves", "boulets", "béliers"], "ERREUR >> Carte invalide"
        assert self.dangers_a_retirer[
                   danger_a_enlever] < 2, "ERREUR >> Erreur au sein de la partie, on enlève un 3ème exemplaire de ce type de danger, ce qui ne devrait pas être possible !"

        self.__dangers_a_retirer[danger_a_enlever] += 1

    def set_manche_termine(self):
        """
        Principe :
            Place la variable manche_en_cours à False afin de provoquer la fin de la manche.
        Entrée :
            Aucune
        Sortie :
            Aucune
        """

        self.__manche_en_cours = False

        if debug:
            print("DEBUG SMT >> La manche est terminée. Arrêt en cours de celle-ci...")

    def set_ajout_liste_manche_reussite_ou_non(self, reussit):
        """
        Principe :
            Ajoute à la liste qui indique si les manches ont été réussite ou non, True ou False.

            True → Elle a été réussite
            False → Elle a été échouée
        Entrée :
            reussit     [BOOL] : True ou False comme expliqué plus tôt
        Sortie :
            Aucune
        """
        assert type(reussit) == bool, "ERREUR >> Le paramètre n'est pas un booléen"

        self.__liste_manche_reussite_ou_non.append(reussit)

        if debug:
            print("DEBUG SALMRON >> Etat de la liste des manches réussite ou non:",
                  str(self.__liste_manche_reussite_ou_non))

    # Les méthodes -----------------------------------------------------------------------------------------------------
    # Attention !
    # Les méthodes ne sont que complémentaire aux fonctions.
    # Elles s’occupent des actions concernant l’objet.
    # Elles ne s’occupent donc pas de l’état du jeu.

    @staticmethod
    def __verif_validiter_liste_joueurs(liste_joueur):
        """
        METHODE PRIVÉE

        Principe :
            Vérifie que la liste de joueur comporte que des objets de type JOUEURS
            Méthode uniquement utilisé à la création d'un objet de type MANCHE.
        Entrée :
            liste_joueur        [LIST] : Liste comportant les objets de type JOUEURS
        Sortie :
            Aucune
        """

        for joueur in liste_joueur:
            assert type(
                joueur) == Joueurs, "ERREUR >> PARAMÈTRE 2 EST INVALIDE -> Ses éléments doivent être du type JOUEURS."

    @staticmethod
    def __verif_validiter_dangers_a_retirer(dangers_a_retirer):
        assert len(
            dangers_a_retirer) == 5, "ERREUR >> PARAMÈTRE 5 INVALIDE -> Nombre inapproprié d'élément dans le dictionnaire"
        for danger in dangers_a_retirer.keys():
            assert danger in ["araignées", "serpents", "laves", "boulets",
                              "béliers"], "ERREUR > PARAMÈTRE 5 INVALIDE -> Éléments invalide dans le dictionnaire"
            assert 0 <= dangers_a_retirer[
                danger] <= 2, "ERREUR >> PARAMÈTRE 5 INVALIDE -> Nombre de carte à retiré incohérent au jeu"

    def tirage_de_carte(self, carte_tiree=None):
        """
        Principe :
            Retire une carte du deck et l'ajoute au banc.

            Soit, il fait un choix aléatoire (si carte_tiree est None).
            Sinon, il tire la carte demandée.
        Entrée :
            carte_tiree      [STR / INT / None] : Nom de la carte
                                                - None : tirage aléatoire
                                                - STR : carte dangers, reliques
                                                - INT/STR : carte trésor
        Sortie :
            carte_tiree             [STR / INT] : nom de la carte
        """

        # Convertie en INT les noms des cartes trésor au format STR.
        if type(carte_tiree) == str:
            if carte_tiree.isdigit():
                carte_tiree = int(carte_tiree)  # Si en réalité, c'est un entier, alors ont convertie.

        assert carte_tiree in self.__deck.keys() or carte_tiree is None, "ERREUR >> Carte invalide."

        if carte_tiree is None:
            # Si carte_tiree est None, alors on tire aléatoirement une carte.

            # Carte_tiree_est_valide indique si la carte tirée est bien valide. Si elle est toujours disponible
            # dans le deck. Vu qu'on ne connait pas encore la carte. On part du principe que c'est faux.
            carte_tiree_est_valide = False

            while not carte_tiree_est_valide:  # Tant qu'on n'a pas choisi de carte valide.
                carte_tiree = choice(list(self.__deck.keys()))  # Tirage aléatoire
                if self.__deck[carte_tiree] >= 1:
                    # Si la carte tirée est disponible dans le deck, on la valide.
                    carte_tiree_est_valide = True

        # À ce moment-là de la méthode, nous sommes sûrs d'avoir l'heureuse élue !

        if debug:
            print("TIRAGE DEBUG >> Carte tirée: " + str(carte_tiree) + ".")

        self.set_enleve_carte_deck(carte_tiree)

        if type(carte_tiree) == str:
            self.set_ajoute_carte_banc(carte_tiree)
            if debug:
                print("TIRAGE DEBUG >> Carte retirée du deck, et ajoutée au banc.")
        elif debug:
            print("TIRAGE DEBUG >> Carte UNIQUEMENT Retirée du deck. Type: " + str(type(carte_tiree)) + ".")

        return carte_tiree

    def distribution_du_reste_tresor(self, joueurs_partant):
        """
        Principe :
            On distribue à part égal le reste du trésor eux joueurs partant.
            On garde ce qui n'a pas pu être distribué.
        Entrée :
            joueurs_partant         [LIST > JOUEURS] : Liste des joueurs voulant quitter la manche.
        Sortie :
            Aucune
        """

        assert type(joueurs_partant) == list, "ERREUR >> Paramètre invalide"

        for objet in joueurs_partant:
            assert type(
                objet) == Joueurs, "ERREUR >> Paramètre invalide. La liste contient des éléments ne venant pas de la classe Joueur."

        assert joueurs_partant != [], "ERREUR >> Liste vide en paramètre !"

        assert len(
            joueurs_partant) <= self.nb_joueur_actif, "ERREUR >> Trop de départ par rapport au nombre de joueurs précédemment en jeu."

        # Répartition du trésor
        diamants_a_distribuer = self.__reste_tresor // len(joueurs_partant)

        # On retire la somme du trésor
        self.set_enleve_diamant_tresor(diamants_a_distribuer * len(joueurs_partant))

        for joueur in joueurs_partant:
            joueur.set_ajout_inv_manche(diamants_a_distribuer)

        if debug:
            print("DEBUG >> Diamants distribués par joueurs: " + str(diamants_a_distribuer) + ", reste: " + str(
                self.__reste_tresor % len(joueurs_partant)) + ".")

        return

    def il_a_til_deux_dangers(self):
        """
        Principe :
            Vérifie si deux dangers égaux sont présents sur le banc.
        Entrée :
            Aucune
        Sortie :
            [BOOL] : - True s'il y a deux dangers égaux sur le banc
                     - False sinon
        """
        dangers = ("araignées", "serpents", "laves", "boulets", "béliers")

        for danger in dangers:
            if self.banc.count(danger) >= 2:
                if debug:
                    print("DEBUG >> Deux dangers égaux présent sur le banc")
                return True

        if debug:
            print("DEBUG >> Il n'y a pas deux dangers égaux sur le banc")
        return False

    def distribution_relique(self, joueur):
        """
        Principe :
            Calcul le total des valeurs des reliques distribués au joueur.
            Retire aussi les reliques du banc.
        Entrée :
            joueur              [JOUEURS] : Objet joueur qui va recevoir les reliques (ou l'unique) et leur valeur en diamants
        Sortie :
            Aucune
        """

        nb_relique_sur_banc = self.banc.count("relique")  # Nombre de reliques sur le banc.
        premiere_relique = self.nb_relique_sortie  # Position de la première relique dans la liste des valeurs.
        derniere_relique = premiere_relique + nb_relique_sur_banc  # Position de la relique suivant la dernière.
        valeur_total_reliques = 0

        if nb_relique_sur_banc == 0:
            if debug:
                print("DEBUG >> Valeur de toute les reliques du banc: 0")
            return valeur_total_reliques

        for relique in range(premiere_relique, derniere_relique):  # On parcourt les valeurs des reliques à distribuer.
            valeur_total_reliques += self.liste_valeur_relique_banc[relique]
            joueur.set_ajout_inv_relique()  # On l'ajoute dans l'inventaire du joueur



        self.set_enleve_carte_banc("relique", nb_relique_sur_banc)  # On retire du banc les reliques
        self.set_ajoute_relique_sortie(nb_relique_sur_banc)  # On les indique comme retirées

        if debug:
            print("DEBUG >> Valeur de toute les reliques du banc: " + str(valeur_total_reliques))

        joueur.set_ajout_inv_manche(valeur_total_reliques)

