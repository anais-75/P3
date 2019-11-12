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
from pygame.locals import *
from items import Items

class application:
	
	def __init__(self):
		
		self.window = pygame.display.set_mode((450, 450))
		pygame.display.set_caption("MacGyver")
		
	def init_background(self):
		background = pygame.image.load("Background.jpg").convert()
		self.window.blit(background, (0,0)) #le fond est empilé sur la fenetre 

	#Placement du Gardien
	def gardien(self): 
		image_Guardian = pygame.image.load("Gardien.png").convert_alpha()
		image_Guardian = pygame.transform.scale(image_Guardian, (30,30))
		self.window.blit(image_Guardian, (420,420))
	
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
		rectangle = {}
		for key, value in  (l.maze.items()):
			for i in (ITEMS):
				if value == i:
					obj= pygame.image.load((i)).convert_alpha()
					obj = pygame.transform.scale(obj,(30,30))
					self.window.blit(obj, ((key[1]*30),(key[0]*30)))
					pygame.display.flip()
					rectangle [i] = ((key[1]*30),(key[0]*30))		
		return rectangle
		
	def score_display(self, counter): 	
		#création d'une fonte pour l'affichage du score
		score = pygame.font.Font(None, 30)
		couleur_score = (255, 255, 255) #couleur de la fonte 
		#surface de score
		score_surface = score.render("Score : {:6d}".format(count), 1, couleur_score)
		#rectangle de positionnement de la surface du score
		score_rect = score_surface.get_rect()
		#blit de la surface de score sur l'écran d'affichage
		g.window.blit(score_surface, score_rect)
		#mise à jour de l'affichage 
		pygame.display.flip()
		return pygame.display.flip()
	
if __name__ == "__main__":	
	
	pygame.init()
	FPS = 10000
	fpsClock = pygame.time.Clock()
	g = application()
	g.init_background()
	g.gardien()
	g.wall()
	count = 0 
	
	for key, value in g.obj_rand().items():
		if key == "Ether.png":
			image_Ether = pygame.image.load(key).convert_alpha()
			image_Ether = pygame.transform.scale(image_Ether, (30,30))
			rect_Ether = image_Ether.get_rect()
			rect_Ether = rect_Ether.move(value)	
								
		if key == "Tube.png":
			image_Tube = pygame.image.load(key).convert_alpha()
			image_Tube = pygame.transform.scale(image_Tube, (30,30))
			rect_Tube = image_Tube.get_rect()
			rect_Tube = rect_Tube.move(value)
			
		if key == "Needle.png":
			image_Needle = pygame.image.load("Needle.png").convert_alpha()
			image_Needle = pygame.transform.scale(image_Needle, (30,30))
			rect_Needle = image_Needle.get_rect()
			rect_Needle = rect_Needle.move(value)
						
#Pour la fluidité du déplacement
	
	image_Macgyver = pygame.image.load("MacGyver.png").convert_alpha()
	image_Macgyver = pygame.transform.scale(image_Macgyver, (30,30))
	Mac = image_Macgyver.get_rect()
	Mac=Mac.move(0,0)
	g.window.blit(image_Macgyver, Mac)
	pygame.display.flip() 	#Rafraîchissement		 
	McG_depl= Move()
	l_test = McG_depl.laby.maze  	
	key1=(0,0)
	pygame.key.set_repeat(400, 30)
	continuer = 1

# Boucle principale	
	while continuer:
		for event in pygame.event.get():			
			if event.type == pygame.QUIT:
				continuer = 0
			if event.type == pygame.KEYDOWN:
				g.init_background()
				if event.key ==K_DOWN:
					key2=McG_depl.deplacement(key1,l_test, "bottom")
					if key1 == key2 or (key2[0]<0) or (key2[0]>14) or key2[1]<0 or key2[1]>14:
						pass
					else:
						Mac = Mac.move((0),(30))
						g.window.blit(image_Macgyver, Mac)
												
				if event.key == K_LEFT:
					key2=McG_depl.deplacement(key1,l_test,"left")
					if key1 == key2:
						pass
					else:
						Mac = Mac.move((-30),(0))
						g.window.blit(image_Macgyver, Mac)

				if event.key == K_UP:
					key2=McG_depl.deplacement(key1,l_test,"top")
					if key1 == key2:
						pass
					else:
						Mac = Mac.move((0),(-30))
						g.window.blit(image_Macgyver, Mac)
			
				if event.key == K_RIGHT:
					key2=McG_depl.deplacement(key1,l_test,"right")
					if key1 == key2:
						pass
					else:
						Mac = Mac.move((30),(0))
						g.window.blit(image_Macgyver, Mac)
						
				if (Mac == rect_Ether):
					count +=1
					rect_Ether = rect_Ether.move(450,450)
					
				if (Mac == rect_Tube):
					count +=1
					rect_Tube = rect_Tube.move(450,450)
					
				if (Mac == rect_Needle):
					count +=1
					rect_Needle = rect_Needle.move(450,450)
										
				#print ("postion Mac objet mcgiver",Mac)
				key1=key2
				g.wall()
				g.gardien()
				g.window.blit(image_Macgyver, Mac)
				g.window.blit(image_Ether, rect_Ether)					
				g.window.blit(image_Tube, rect_Tube)
				g.window.blit(image_Needle, rect_Needle)				
				g.score_display (count)

		fpsClock.tick(FPS)	
			
	pygame.quit()
