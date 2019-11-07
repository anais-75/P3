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
		self.l = labyrinthe()
		self.liste_objet=[]
		self.count_objet=0
	
	#Methode de deplacment 	
	def deplacement(self, coord, liste, direction):
		
		t, l2 = coord, liste
		direction = direction
		t1 = self.l.find_path(coord[0], coord[1], direction)
		print (t1)
		if isinstance (l2[t1], Items):
			self.count_objet += 1
			print ("mon compteur d'objet compte",self.count_objet)
			self.liste_objet=l2[t1]
			print ("le contenu de la liste d'objet est:", self.liste_objet)
			l2 [t1] = self.mc
			l2 [t] = 'o'
			print (t1)
			return t1
		else:						
			if (self.l.check_cell(t1[0], t1[1])):
				t1 = self.l.find_path(coord[0], coord[1], direction)
				l2 [t1] = self.mc
				l2 [t] = 'o'
				#print(l2)
				#print (type (l2))
				print (t1)
			else:
				t1=t
		return t1

#programme principal

if __name__ == "__main__":
	
# DEBUT DE LA PARTIE, ON INITIALISE McGiver en position (0,0)

	McG_depl= Move()
	l_test = McG_depl.l.maze
	key=(0,0)
	
	while key!=(14,14):
		direction = input("Choisissez la direction : ")
		key = (McG_depl.deplacement(key,l_test,direction))
		
		
