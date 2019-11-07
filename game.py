#!/usr/bin/python3
# coding: utf-8 

"""
MacGyver maze game, MacGyver has to pick up all the objects, lull the guardian and get out of the maze to win.
script 
fils: labyrinthe_Mc.py, classes.py, constantes.py, in constants there are all the images of the game.

"""
import random 
from MacGyver import*
from items import Items
from constants import*
from labyrinthe import*
import pygame
from items import Items

class application:
	
	def __init__(self):
		
		self.window = pygame.display.set_mode((450, 450))
		pygame.display.set_caption("MacGyver")
		
	def init_background(self):
		background = pygame.image.load("Background.jpg").convert()
		self.window.blit(background, (0,0)) #le fond est empilé sur la fenetre 
		pygame.display.update() 
		return pygame.display.flip()

	#Placement du Gardien
	def gardien(self): 
		image_Guardian = pygame.image.load("Gardien.png").convert_alpha()
		image_Guardian = pygame.transform.scale(image_Guardian, (30,30))
		self.window.blit(image_Guardian, (420,420))
		return pygame.display.flip()
	#Placement des murs
	def wall (self):
		l = labyrinthe()
		for key, value in (l.maze.items()):
			if value == 'w':
				image_Wall = pygame.image.load("wall.png").convert_alpha()
				image_Wall = pygame.transform.scale(image_Wall,(30,30))
				self.window.blit(image_Wall, ((key[1]*30),(key[0]*30)))  
				
		return image_Wall


	#placement des objets
	def set_items(self):
		l = labyrinthe()
		# on boucle 3 fois, une fois par objet à placer
		for items in ITEMS:
			# récupérer des coordonnées pour y placer un objet
			x = random.choice(l.free_cells)

			# vérifier si la case sélectionnée aléatoirement n'a pas déjà été prise
			# par une boucle précédente.
			for cell in l.free_cells:
				if cell == x:
					l.free_cells.remove(cell)

			# mettre un objet dans la case des coordonnées trouvées aléatoirement
			l.maze[x] = pygame.image.load((items)).convert_alpha()
		


	def obj_rand(self):
		l = labyrinthe()
		
		for key, value in  (l.maze.items()):
			if value == ITEMS[0]:
				Needle = pygame.image.load("Needle.png").convert_alpha()
				Needle = pygame.transform.scale(Needle,(30,30))
				self.window.blit(Needle, ((key[1]*30),(key[0]*30)))
			if value == ITEMS[1]:
				Ether = pygame.image.load("Ether.png").convert_alpha()
				Ether = pygame.transform.scale(Ether,(30,30))
				self.window.blit(Ether, ((key[1]*30),(key[0]*30)))	
			if value == ITEMS[2]:
				Tube = pygame.image.load("Tube.png").convert_alpha()
				Tube = pygame.transform.scale(Tube,(30,30))
				self.window.blit(Tube, ((key[1]*30),(key[0]*30)))				
		pygame.display.flip() 	
				
		
	
if __name__ == "__main__":	
	

# Boucle principale

	pygame.init()
	g = application()
	g.init_background()
	g.gardien()
	g.wall()
	g.set_items()
	g.obj_rand()
#Pour la fluidité du déplacement
	pygame.key.set_repeat(400, 30)
	image_Macgyver = pygame.image.load("MacGyver.png").convert_alpha()
	image_Macgyver = pygame.transform.scale(image_Macgyver, (30,30))
	Mac = image_Macgyver.get_rect()
	Mac=Mac.move(0,0)
	g.window.blit(image_Macgyver, Mac)

	pygame.display.flip() 	#Rafraîchissement
			 
	McG_depl= Move()
	l_test = McG_depl.l.maze  
	
	key1=(0,0)
	
	continuer = 1
	while continuer:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				continuer = 0
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					key2=McG_depl.deplacement(key1,l_test, "bottom")
					if key1 == key2 or (key2[0]<0) or (key2[0]>14) or key2[1]<0 or key2[1]>14:
						pass
					else:
						Mac = Mac.move((0),(30))
												
				if event.key == pygame.K_LEFT:
					key2=McG_depl.deplacement(key1,l_test,"left")
					if key1 == key2:
						pass
					else:
						Mac = Mac.move((-30),(0))

				if event.key == pygame.K_UP:
					key2=McG_depl.deplacement(key1,l_test,"top")
					if key1 == key2:
						pass
					else:
						Mac = Mac.move((0),(-30))
			
				if event.key == pygame.K_RIGHT:
					print ("key1 avant",key1)
					key2=McG_depl.deplacement(key1,l_test,"right")
					if key1 == key2:
						pass
					else:
						Mac = Mac.move((30),(0))

				key1=key2
				g.window.blit(image_Macgyver, Mac)
				g.init_background()
				g.gardien()
				g.wall()
				pygame.display.flip()

	pygame.quit()
	

