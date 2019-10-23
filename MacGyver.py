#!/usr/bin/python3
# coding: utf-8 
"""
this file contains all the class methods that can animate it and find the output
"""
from labyrinthe import*
from constants import *
from items import Items
		
class Character:
	"""Classe permettant de créer un personnage"""
	def __init__(self, perso):
		#Sprites du personnage
		self.perso= pygame.image.load(MacGyver).convert_alpha()
		#Position du personnage en cells et en pixels
		self.cell_x = 0
		self.cell_y = 0
		self.x = 0
		self.y = 0
		
	
	def move(self, direction):
		"""Methode permettant de déplacer le personnage et de verifier que les coord soit dans le labyrinthe"""
		
		#Déplacement vers la droite
		if direction == 'right':
			#Pour ne pas dépasser l'écran
			if self.cell_x <= (numbre_sprite_side - 1)and [self.cell_y][self.cell_x+1] != "w":
					#Déplacement d'une cell
					self.cell_x += 1
					#Calcul de la position "réelle" en pixel
					self.x = self.cell_x * size_sprite
			#Image dans la bonne direction
			self.direction = self.right
		
		#Déplacement vers la gauche
		if direction == 'left':
			if self.cell_x >= 0 and [self.cell_y][self.cell_x-1] != "w" and self.cell_x -1 >= 0:
					self.cell_x -= 1
					self.x = self.cell_x * size_sprite
			self.direction = self.gauche
		
		#Déplacement vers le haut
		if direction == 'up':
			if self.cell_y >= 0 and [self.cell_y-1][self.cell_x] != "w" and self.cell_y-1 >= 0:
			#rajouté une condition sur le mur 	
					self.cell_y -= 1
					self.y = self.cell_y * size_sprite
			self.direction = self.haut
		
		#Déplacement vers le bas
		if direction == 'down':
			if self.cell_y < (numbre_sprite_side - 1) and [self.cell_y+1][self.cell_x] != "w":    
			#rajouté une condition sur le mur 	
					self.cell_y += 1
					self.y = self.cell_y * size_sprite
			self.direction = self.down
