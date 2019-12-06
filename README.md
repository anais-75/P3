                
					# Aidez MacGyver à s’échapper

# Présentation
        MacGyver est enfermé dans un labyrinthe, pour s'échapper il doit ramasser trois objets   
et endormir le gardien qui protège la sortie.
les trois objets sont déposés aléatoirement, MacGyver doit ramasser l’objet en se déplaçant sur la case contenant ce dernier, les objets changent de place à chaque fois que l'utilisateur relance le jeu.
Si MacGyver ramasse les trois objets et se présente devant le gardien, l’utilisateur gagne ; sinon s’il n'a pas ramassé les trois objets et qu'il se présente devant le garde, il perd la partie.
la structure  du jeu est enregistrée dans un fichier texte  pour faciliter la modification.
la fenêtre est un carré de 15 sprites sur laquelle Macgyver se déplace à l’aide des touches directionnelles du clavier.

# Pré-requis
    • Programme développer sous Debian 10 
    • Installer python3
    • Installer l’IDE Geany 
    • Ajouter le module flake8 à Geany pour respecter la PEP8 
    • Installer pygame, contrainte imposer pour le projet.
    • Versionner le code avec Git et le distribuer sur Github.

# Installation
    • pour l’installation de l’environnement virtuel 
		 Exécuter :`pip3 install Virtualenv`
    • pour créer l’environnement 
		 Exécuter : `virtualenv -p python3 env`
    • pour activer l’environnement  
	   Exécuter : `source env/bin/activate`
    puis Lancer le programme
    Exécuter : python launch.py depuis la console

# Paramétrage

        Le labyrinthe est généré à partir d’un fichier sous format .txt , il contient 15 lignes et 15 colonnes de caractères: "w" = Wall,  "o" = Open,  "d" = Departure,  "a" = Arrival.
    • La méthode create_table() de la classe Labyrinthe génère une liste à partir de la lecture du fichier maze.txt  qu’elle retourne.
    •  On affiche la photo du gardien sur la case "a" .
    •  On affiche la photo de MacGyver sur la case “d”, 
    on initialise la position de MacGyver sur cette case,  puis il se déplace sur les cases vide du fichier .txt à l’aide des touches du clavier. 
    • Les trois objets sont placées aléatoirement avec la méthode obj_rand()  
    et  sont ramassés de façon conditionnelle. On compare les coordonnées de Macgyver avec celle de l’objet, 
    si aux coordonnées de MacGyver il y a l’objet, le compteur est incrémenté et le score est affiché ;
    l’objet est ensuite retiré de la fenêtre de jeu.
    • Le fond du labyrinthe est initialisé avec la méthode init_background dans la classe Application().
    • L’image du mur est chargée sur les caractères "w" de manière fixe et elle est superposée sur l’image de fond. 

