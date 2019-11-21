#!/usr/bin/python3
# coding: utf-8 

"""
MacGyver maze game, MacGyver has to pick up all the objects, lull the guardian and get out of the maze to win.
script 
fils: MacGyver.py labyrinthe_Mc.py, classes.py, constantes.py, in constants there are all the images of the game.

"""	
import time
import random 
from MacGyver import*
from items import Items
from constants import*
from labyrinthe import*
import pygame
from pygame.locals import *
from items import Items
from images import *

class application:
	
	def __init__(self):	
		count =0
		# set window size and title 
		self.window = pygame.display.set_mode((450, 450))
		pygame.display.set_caption("MacGyver")
		self.init_background()
		self.gardien()
		self.wall()	
		
	def init_background(self):
		background = pygame.image.load("images/Background.jpg").convert()
		self.window.blit(background, (0,0)) 

	# placing guardian 
	def gardien(self): 
		image_Guardian = pygame.image.load("images/Gardien.png").convert_alpha()
		image_Guardian = pygame.transform.scale(image_Guardian, (30,30))
		gardian_rect = image_Guardian.get_rect()
		gardian_rect = gardian_rect.move(420,420)
		print ("gardien_img {}, garduien_rect {}", image_Guardian,gardian_rect)
		return image_Guardian,gardian_rect
	
	#Placing walls
	def wall (self):
		l = labyrinthe()
		for key, value in (l.maze.items()):
			if value == 'w':
				image_Wall = pygame.image.load("images/wall.png").convert_alpha()
				image_Wall = pygame.transform.scale(image_Wall,(30,30))
				self.window.blit(image_Wall, ((key[1]*30),(key[0]*30))) 		
		return image_Wall

	#placement of the items 
	def set_items(self):
		l = labyrinthe()
		# we make 3 loop, once to per object to be placed 
		for items in ITEMS:
			# retrieve coordinates to place object
			x = random.choice(l.free_cells)

			# check if the randomly selected box has not already been taken
			#by a previous loop
			for cell in l.free_cells:
				if cell == x:
					l.free_cells.remove(cell)

			# put an item in the box of coordinates found randomly
			l.maze[x] = pygame.image.load((items)).convert_alpha()
			
	# method that allows you to place objects randomly	
	def obj_rand(self):
		l = labyrinthe()
		rectangle = {}
		for key, value in  (l.maze.items()):
			for i in (ITEMS):
				if value == i:
					obj= pygame.image.load(i).convert_alpha()
					obj = pygame.transform.scale(obj,(30,30))
					self.window.blit(obj, ((key[1]*30),(key[0]*30)))
					pygame.display.flip()
					rectangle [i] = ((key[1]*30),(key[0]*30))		
		return rectangle
	
	# method for score display	
	def score_display  (self, count): 
		score_font = pygame.font.SysFont('comicsansms', 40, True, True)
		pygame.font.Font.set_bold
		couleur_font = (255, 255, 255)
		score_surface = score_font.render("Score : {:6d} points".format(count), 1, couleur_font)
		score_rect = score_surface.get_rect()
		score_rect.move_ip(300,0)
		self.window.blit(score_surface, score_rect)
		#refresh the display
		pygame.display.flip()
		return pygame.display.flip()

		
	''' method for the main game loop'''	
def launch_game():

	# Variable for the infinite loop
	continuer = 1
	g = application()
	while continuer:
		pygame.init()
		FPS = 10000
		fpsClock = pygame.time.Clock()
		g.init_background()
		image_Guardian,gardian_rect = g.gardien()
		g.window.blit(image_Guardian,gardian_rect)
		g.wall()
		
		count = 0 
			
		for key, value in g.obj_rand().items():
			if key == "images/Ether.png":
				image_Ether = pygame.image.load(key).convert_alpha()
				image_Ether = pygame.transform.scale(image_Ether, (30,30))
				rect_Ether = image_Ether.get_rect()
				rect_Ether = rect_Ether.move(value)	
									
			if key == "images/Tube.png":
				image_Tube = pygame.image.load(key).convert_alpha()
				image_Tube = pygame.transform.scale(image_Tube, (30,30))
				rect_Tube = image_Tube.get_rect()
				rect_Tube = rect_Tube.move(value)
				
			if key == "images/Needle.png":
				image_Needle = pygame.image.load(key).convert_alpha()
				image_Needle = pygame.transform.scale(image_Needle, (30,30))
				rect_Needle = image_Needle.get_rect()
				rect_Needle = rect_Needle.move(value)

		
		image_Macgyver = pygame.image.load("images/MacGyver.png").convert_alpha()
		image_Macgyver = pygame.transform.scale(image_Macgyver, (30,30))
		Mac = image_Macgyver.get_rect()
		Mac=Mac.move(0,0)
		g.window.blit(image_Macgyver, Mac)
		pygame.display.flip() 			 
		McG_depl= Move()
		l_test = McG_depl.laby.maze  	
		key1=(0,0)
		key2=(0,0)
		pygame.key.set_repeat(400, 30)
		background = pygame.image.load("images/Background.jpg").convert_alpha()
		g.window.blit(background, (0,0))
		
		font = pygame.font.SysFont('comicsansms', 40, True, False)
		text = font.render("press ENTER to start", 1, (255, 255, 255))
		text1 = font.render("press ESC to quit", 1, (255, 255, 255))
		
		font2 = pygame.font.SysFont('comicsansms', 28, True, False)
		text2 = font2.render("Welcome to the MacGyver Game ", 1, (255,255, 0))
		text3 = font2.render("you must collect all items on the map ", 1, (255, 225, 0))
		text4 = font2.render("and meet the guardian to escape the maze", 1, (255,200, 0))
		textrect2 = text2.get_rect(center=(225,60))
		textrect3 = text3.get_rect(center=(225,120))
		textrect4 = text4.get_rect(center=(225,150))
		
		g.window.blit(text2, textrect2)
		g.window.blit(text3, textrect3)
		g.window.blit(text4, textrect4)
		g.window.blit(text, (50,240))
		g.window.blit(text1, (80,270))
		#g.window.blit(text2, (50,60))
		pygame.display.flip()
		pygame.display.update()

		
		continue_home = 1
		continue_game = 1

	#Boucle continue home 
		while continue_home:
			pygame.init()
			pygame.time.Clock().tick(30)
			
			for event in pygame.event.get():
				if event.type == KEYDOWN and event.key == K_RETURN:				
					continue_game = 1
					continue_home = 0
						
				#Si l'utilisateur quitte, on met les variables 
				#de boucle à 0 pour n'en parcourir aucune et fermer
				if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
					continue_home = 0
					continue_game = 0
					continuer = 0
					pygame.quit()
		
	#Boucle continue jeu 		
		while continue_game:
			#Keyboard touch used to quit game
			for event in pygame.event.get():			
				if event.type == pygame.QUIT:
					continuer = 0
				if event.type == pygame.KEYDOWN:
					g.init_background()
					# Keyboard touch used to moove MacGyver
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
					
					key1=key2
					
					# check if the items have been picked or not		
					if (Mac == rect_Ether):
						count +=1
						rect_Ether = rect_Ether.move(450,450)
						
					if (Mac == rect_Tube):
						count +=1
						rect_Tube = rect_Tube.move(450,450)
						
					if (Mac == rect_Needle):
						count +=1
						rect_Needle = rect_Needle.move(450,450)
						
					# Re-pasting all after the events
					g.wall()
					g.window.blit(image_Guardian,gardian_rect)
					g.window.blit(image_Macgyver, Mac)
					g.window.blit(image_Ether, rect_Ether)					
					g.window.blit(image_Tube, rect_Tube)		
					g.window.blit(image_Needle, rect_Needle)				
					g.score_display(count)
					
					# endgame, game won or loose 

					if (Mac == gardian_rect and count == 3):  
						font = pygame.font.SysFont('comicsansms', 70, True, False)
						text = font.render("You win !", 1, (255, 255, 255)) 
						textrect = text.get_rect()
						textrect.move_ip(65,190)
						g.window.blit(text, textrect)
						pygame.display.flip()
						time.sleep(3)
						continue_home = 1
						continue_game = 0
		
					if (Mac == gardian_rect and count !=3):
						font = pygame.font.SysFont('comicsansms', 60, True, False)
						text = font.render("GAME OVER!", 1, (255, 0, 0)) 
						textrect = text.get_rect()
						textrect.move_ip(60,190)
						g.window.blit(text, textrect)
						pygame.display.flip()		
						time.sleep(3)
						continue_home = 1
						continue_game = 0
							
				fpsClock.tick(FPS)	
		
	pygame.quit()
	
if __name__ == "__main__":	
	launch_game()	
