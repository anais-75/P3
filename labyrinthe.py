#!/usr/bin/python3
#coding: utf-8 
import random
import pygame
from items import Items
from constants import*

#Opening and processing the file labyrinth.txt

class labyrinthe:

	count = 0
	def __init__(self):
		self.__class__.count += 1
		# we create the dictionary labyrinthe
		self.maze = self.create_table()
		# we create an attribute to save the coordinates "free cell" ("o")
		# we look for empty boxes 
		self.free_cells = self.free_coords()
		# We want to place the objects
		
		self.set_items()
		self.gar_character()
		self.mc_character()
		
	# Method which generate the structure from the maze.txt 
	# and that creates the dictionary representing the labyrinth
	def create_table(self):
	
		N = 15
		FileLabyrinth = open('maze.txt', 'r') # instanciation de l'objet Fichier 
		lignes, colonnes = 15, 15

		liste = [ 0 for i  in range(0)]  

		# we create an empty list 
		index, i, j = 0, 0, 0
		for i in range(N):
			for j in range(N):
				lab = FileLabyrinth.read()
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
		return liste2
	
	# Method to check if the box is a path or not		
	def check_cell(self, x, y):
		""" Check wether the new coordinates are free to walk on or not """

		# verification of the existence of coordinates
		if (x, y) not in self.maze:
			# la case n'existe pas
			return False

		# checking the availability of the box
		if self.maze[(x, y)] == 'o':
			# Returns true if the new coordinates correspond to a path
			return True
		# Return false otherwise
		return False

	# Method that calculates the coordinates of a box according
	# to the coordinates of a starting box and a direction
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

	# method that returns a list of all the coordinates of the boxes where you can walk
	def free_coords(self):
		# we create an empty list to store the coordinates of empty boxes
		fc = []
		# we check the coordinates one by one
		for i in self.maze:
			if self.maze[i] == 'o':  
				# save the empty cell in the "fc" list
				
				fc.append(i)
		return fc

	# we try to find 3 empty boxes to put objects
	def set_items(self):
		liste_obj=[]
		for items in ITEMS:
			# retrieve coordinates to place an object
			x = random.choice(self.free_cells)

			# check if the randomly selected box has not already been taken by a previous loop.
			for cell in self.free_cells:
				if cell == x:
					self.free_cells.remove(cell)
			# put an object in the box of coordinates found randomly
					self.maze[x] = Items(items)
				
	# we place the guardien 
	def gar_character(self):
		for i in self.maze:
			if self.maze[i] == 'a':
				self.maze[i] = Items(CHAR[1])
	# we place the macgyver 
	def mc_character(self):
		for i in self.maze:
			if self.maze[i] == 'd':
				self.maze[i] = Items(CHAR[0])      	
				
	# we create 4 méthods to move macgyver 
	def move_left(self):
		return "left"
		
	def move_right(self):
		return "right"
		
	def move_top(self):
		return "top"
		
	def move_bottom(self):
		return "bottom"
		
        
	# Count the number of objects picked up
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
 
	
	
	
	



