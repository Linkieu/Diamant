[<img style="float: right ;width:25%" src="medias\img\uvsq_velizy.png" alt="Image UVSQ">](https://www.uvsq.fr/)
#### Matthieu et Tom

# <u>Avant de commencer à jouer</u>

## Présentation
Ce projet a été construit par Matthieu et Tom dans le cadre d'une Situation d'Apprentissage et d'Évaluation au cours de la première année de BUT Informatique.

Ce projet Python est construit autour du jeu de société Diamant, aussi appelé Incan Gold.

<u>Présentation du jeu, tiré du document fourni par l'établissement, pour nous présenter la SAÉ:</u><br>
Le principe du jeu est simple, se jouant essentiellement avec des cartes et quelques jetons.
Le mécanisme du jeu est dit de « stop ou encore » : à chaque étape, les joueurs doivent
décider s’ils sécurisent leur gain, ou s’ils prennent des risques pour gagner davantage, au
risque de tout perdre !

## Lancer le jeu
Ouvrez le fichier Diamants.py, et exécutez le script.

Dans le terminal, un petit menu s'affiche dans le terminal. Il vous demande de choisir entre le mode graphique ou continuer avec le mode terminal.<br>
Appuyez sur la touche A si vous souhaitez lancer le jeu en mode graphique.<br>
Ou appuyez sur la touche B si vous souhaitez lancer le jeu en mode terminal.

Une fois avoir sélectionné le mode d’affichage, l’écran de titre apparaît.<br>
Sur l’écran titre, on peut lancer le jeu, mais également le quitter.<br>
Ce qui aura comme effet d’interrompre le programme.<br>
Une fois lancé, le jeu demande le nombre de joueurs et leur pseudonyme avant de lancer la première manche.

## Fonctionnement d'une partie

L’un des joueurs doit piocher une carte, et celle-ci apparaît a l’écran.<br>
Les joueurs auront ensuite le choix  entre continuer l’aventure, ou retourner au campements.<br>
S’il n’y a plus de joueur en exploration ou qu’il y a eu un accident juste avant, alors le jeu enchaine vers la prochaine manche.

Le jeu se termine par un petit récit avant d’afficher les statistiques et de remercier les joueurs.<br>
Il est possible de passer le récit ou le message de remerciement.<br>
Pour cela, en mode CONSOLE il est possible de taper "STOP" avant d'appuyer sur ENTRÉE quand le jeu le propose.<br>
En mode GRAPHIQUE, il suffit de cliquer sur le bouton.

## Configuration

#### Pour pouvoir savourer pleinement votre aventure, veuillez posséder les modules suivants:
<ul>
    <li>Tkiteasy (fournit dans le projet)</li>
    <li>Tkinter</li>
    <li>Pillow (PIL)</li>
</ul>

*Ces modules sont déjà présent sur les ordinateurs de l'IUT de Vélizy*

#### Pour utiliser l'interface graphique
Il est recommandé d'avoir une résolution d'écran de __1920x1080__ (1080p)

#### Le projet comprend les fichiers python:
<ul>
    <li><b>Répertoire principal (/)</b>
        <ul> 
            <li>Diamants.py</li>
        </ul>
    </li>
    <li><b>Répertoire py (/medias/py)</b>
        <ul>
            <li>affichage_console.py</li>
            <li>affichage_graphique.py</li>
            <li>fonctions.py</li>
            <li>initialisation.py</li>
            <li>tkiteasy.py</li>
        </ul>
    </li>
    <li><b>Répertoire tests_fonctions_methodes (/medias/py/tests_fonctions_methodes)</b>
        <ul>
            <li>test_afg_joueur_console.py</li>
            <li>test_class_joueur.py</li>
            <li>test_fonctions.py</li>
        </ul>
    </li>
</ul>

*Tkiteasy est un fichier python fournit par l'IUT de Vélizy*

# <u>Informations concernant le développement</u>

## Travail accompli

Le jeu est fonctionnel et propose une interface console tout comme graphique.<br>

Le projet utilise des images venant d'internet.<br>
Certaines ont été retouchés, afin de former un jeu totalement inédit !