#!/usr/bin/python3
# coding: utf-8 

"""
MacGyver maze game, MacGyver has to pick up all the objects, lull the guardian and get out of the maze to win.
script 
fils: MacGyver.py labyrinthe_Mc.py, classes.py, constantes.py, in constants there are all the pictures of the game.

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
		background = pygame.image.load("pictures/Background.jpg").convert()
		self.window.blit(background, (0,0)) 

	# placing guardian 
	def gardien(self): 
		image_Guardian = pygame.image.load("pictures/Gardien.png").convert_alpha()
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
				image_Wall = pygame.image.load("pictures/wall.png").convert_alpha()
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
		score_font = pygame.font.SysFont('comicsansms', 25, True, True)
		pygame.font.Font.set_bold
		couleur_font = (255, 255, 255)
		score_surface = score_font.render("Score : {:2d} points".format(count), 1, couleur_font)
		score_rect = score_surface.get_rect()
		score_rect.move_ip(280,0)
		self.window.blit(score_surface, score_rect)
		#refresh the display
		pygame.display.flip()
		return pygame.display.flip()

		
if __name__ == "__main__":	
	application()	
