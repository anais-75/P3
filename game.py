#!/usr/bin/python3
# coding: utf-8 

"""
MacGyver maze game, MacGyver has to pick up all the objects, lull the guardian and get out of the maze to win.
script 
fils: labyrinthe_Mc.py, classes.py, constantes.py, in constants there are all the images of the game.

"""

import pygame
#from MacGyver import*
from items import Items

pygame.init()

#creation of the window Pygame 
	
window = pygame.display.set_mode((450, 450))
#Title
pygame.display.set_caption("MacGyver")

# loading and sticking the background
background = pygame.image.load("Background.jpg").convert()
window.blit(background, (0,0)) #le fond est empilé sur la fenetre 
pygame.display.update() 
pygame.display.flip()

#chargement des photos des objets
Object_N = pygame.image.load("Needle.png").convert()

Object_E  = pygame.image.load("Ether.png").convert()
Object_T = pygame.image.load("Tube.png").convert()
pygame.display.flip()


pygame.display.flip()

class application:
	
	def __init__(self):
		self		
	#Placement du Gardien
	def gardien(self, screen):
		image_Guardian = pygame.image.load("Gardien.png").convert_alpha()
		screen.blit(self.Guardian, gar_character)

	# création et déplacement de MacGyver 
	def macgyver(self):
		image_Macgyver = pygame.image.load(MacGyver).convert_alpha()
		Mac = image_Macgyver.get_rect() 
		window.blit(image_Macgyver, Mac)	
		
	def event(self, event):
		pygame.time.Clock().tick(30)
		pygame.key.set_repeat(400, 30) #le temps entre chaque déplacement
		for event in pygame.event.get():  
		#On parcours la liste de tous les événements reçus
			if event.type == KEYDOWN:  
				if event.key == K_RIGHT:
					self.macgyver.Move('right')
				elif event.key == K_LEFT:
					self.macgyver.Move('lefth')
				elif event.key == K_UP:
					self.macgyver.Move('up')
				elif event.key == K_DOWN:
					self.macgyver.Move('down')	
		#screen refreshment
		pygame.display.flip()	
	
	
	
		
if __name__ == "__main__":	
	
###################
# Boucle principale
###################
	g = application()
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			else: 
				g
	pygame.display.flip()
	pygame.quit()			


