#!/usr/bin/python3
#coding: utf-8 
import random
from items import Items
from constants import*

#Ouverture et traitement du fichier labyrinth.txt

class labyrinthe:
	count = 0
	def __init__(self):
		self.__class__.count += 1
		# on crée le dictionnaire du labyrinthe
		self.maze = self.create_table()
		# on crée un attribut pour enregistrer les coordonnées "vides" ("o")
		# on lance la recherche des cases "vides" dès le début
		self.free_cells = self.free_coords()
		# On veut placer les objets
		self.set_items()
		self.gar_character()
		self.mc_character()
		
	# Méthode qui crée le dictionnaire représentant le labyrinthe
	def create_table(self):
	
		N = 15
		FichierLabyrinth = open('maze2.txt', 'r') # instanciation de l'objet Fichier 
		lignes, colonnes = 15, 15

		liste = [ 0 for i  in range(0)]  

		# On crée une liste vide
		index = 0
		i=0
		j=0
		for i in range(N):
			for j in range(N):
				lab = FichierLabyrinth.read()
				lab = lab.replace('\n','') 
				
				while index < len(lab):
					if index =='\n':
						j+=1
					if index !='\n':
						char = lab[index]
						liste.append(char)
						index +=1
		liste2 ={}
		nb_lin = 15
		nb_col = len(liste) // nb_lin
		mat = [[''] * nb_col for i in range(nb_lin)]
		for pos, elt in enumerate(liste):
			i = pos // nb_lin
			j = pos % nb_lin 
			mat[i][j] = elt
			myTuple = (i, j)
			liste2[myTuple] = mat[i][j]

		#print("maliste2", liste2)
		return liste2
	
	# Méthode qui permet de vérifier si la case est un chemin ou non		
	def check_cell(self, x, y):
		""" Check wether the new coordinates are free to walk on or not """

		# vérification de l'existence des coordonnées
		if (x, y) not in self.maze:
			# la case n'existe pas
			return False

		# vérification de la disponibilité de la case
		if self.maze[(x, y)] == 'o':
			# Renvoie vrai si les nouvelles coordonnées correspondent à un chemin
			return True
		# Renvoie faux sinon
		return False

	# Méthode qui permet de calculer les coordonnées d'une case en fonction
	# des coordonnées d'une case de départ ET d'une direction
	# direction = ["top", "right", "bottom", "left"]
	def find_path(self, x, y, direction):
		""" Find new coordinates with direction """
		if direction== "top":
			return (x-1, y)
		elif direction == "bottom":
			return (x+1, y)
		elif direction == "left":
			return (x, y-1)
		elif direction == "right":
			return (x, y+1)

	# méthode qui te renvoie une liste de toutes les coordonnées des cases où
	# on peut marcher
	def free_coords(self):
		# on crée une liste vide pour y stocker les coordonnées des cases vides
		fc = []
		# on vérifie les coordonnées une par une
		for i in self.maze:
			if self.maze[i] == 'o':  
				# enregistre la cellule vide dans la liste "fc"
				fc.append(i)
		# on retourne la liste contenant les cases vides
		return fc

	# on cherche à trouver 3 cases vides pour y mettre des objets
	def set_items(self):
		# on boucle 3 fois, une fois par objet à placer
		for items in ITEMS:
			# récupérer des coordonnées pour y placer un objet
			x = random.choice(self.free_cells)

			# vérifier si la case sélectionnée aléatoirement n'a pas déjà été prise
			# par une boucle précédente.
			for cell in self.free_cells:
				if cell == x:
					self.free_cells.remove(cell)

			# mettre un objet dans la case des coordonnées trouvées aléatoirement
			self.maze[x] = Items(items)
		return (self.maze)
	
	# 1 - on place le gardien => Mettre une lettre spécifique dans ton fichier lab.txt
	def gar_character(self):
		for i in self.maze:
			if self.maze[i] == 'a':
				self.maze[i] = Items(CHAR[1])
				 
				
				
		
	
	# 2 - on place MacGyver => Mettre une lettre spécifique dans ton fichier lab.txt
	#def mac_character(self):
	def mc_character(self):
		for i in self.maze:
			if self.maze[i] == 'd':
				self.maze[i] = Items(CHAR[0])	
				
	# 3 - déplacements => créer les 4 méthodes
	def move_left(self):
		return "left"
		
	def move_right(self):
		return "right"
		
	def move_top(self):
		return "top"
		
	def move_bottom(self):
		return "bottom"
		
        
	#Compter le nombre d'objets ramassés 
	def count_items(self):
		count = 0
		for valeur in self.maze.values():
			if valeur == ITEMS[0] or valeur == ITEMS[1] or valeur == ITEMS[2]:
				count +=1
		return count
		
	def retourne_value (self,l):
		
		for valeur in self.maze.values():
			if valeur == 'w':
				print (valeur)
		return valeur
		
if __name__ == "__main__":
	l = labyrinthe()
	print (l.set_items())
	
	
	
	
	



