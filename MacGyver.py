#!/usr/bin/python3
# coding: utf-8
import random 
#import DeplacementMc
import random
import sys
from items import Items
from constants import*
from labyrinthe import*

class Move:
	
	def __init__(self):
		self.mc = Items(CHAR[0]) 
		self.laby = labyrinthe()
		self.liste_objet=[]
		self.count_objet=0
	
	# method of moving in the labyrinth	
	def deplacement(self, coord, grid, direction):
		new_coordinates = self.laby.find_path(coord[0], coord[1], direction)

		# check the availability of new coordinate and that we are in the labyrinth
		# check that it's not a wall 
		if new_coordinates[0] not in range(0, 15) or new_coordinates[1] not in range(0, 15) or grid[new_coordinates] == 'w':
			return coord

		grid[new_coordinates] = self.mc
		grid[coord] = 'o'

		if isinstance (grid[new_coordinates], Items):
			self.count_objet += 1
			self.liste_objet=grid[new_coordinates]
		else:						
			new_coordinates = coord
			if (self.laby.check_cell(new_coordinates[0], new_coordinates[1])):
				new_coordinates = self.l.find_path(coord[0], coord[1], direction)
				print(l2)
		return new_coordinates
	

# main program

if __name__ == "__main__":
	
	'''begenning of the part, we initialize macgyver in position (0,0)'''

	McG_depl= Move()
	l_test = McG_depl.laby.maze
	key=(0,0)
	
	while key!=(14,14):
		direction = input("chose a direction : ")
		key = (McG_depl.deplacement(key,l_test,direction))
