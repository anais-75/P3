#!/usr/bin/python3
# coding: utf-8

"""
MacGyver maze game,he has to pick up all the objects,
lull the guardian and get out of the maze to win.
script
"""

import time
from MacGyver import*
from constants import*
from labyrinthe import*
from game import*
import pygame
from pygame.locals import *

class Game:

	def __init__(self):
		self.launch()

	''' method for the main game loop'''
	def launch(self):

		# Variable for the infinite loop
		continuer = 1
		g = application()
		while continuer:
			pygame.init()
			fps = 10000
			fps_clock = pygame.time.Clock()
			g.init_background()
			image_guardian, gardian_rect = g.gardien()
			g.window.blit(image_guardian, gardian_rect)
			g.wall()
			count = 0

			for key, value in g.obj_rand().items():
				if key == "pictures/Ether.png":
					image_ether = pygame.image.load(key).convert_alpha()
					image_ether = pygame.transform.scale(image_ether, (30, 30))
					rect_ether = image_ether.get_rect()
					rect_ether = rect_ether.move(value)

				if key == "pictures/Tube.png":
					image_tube = pygame.image.load(key).convert_alpha()
					image_tube = pygame.transform.scale(image_tube, (30, 30))
					rect_tube = image_tube.get_rect()
					rect_tube = rect_tube.move(value)

				if key == "pictures/Needle.png":
					image_needle = pygame.image.load(key).convert_alpha()
					image_needle = pygame.transform.scale(image_needle, (30, 30))
					rect_needle = image_needle.get_rect()
					rect_needle = rect_needle.move(value)

			# we load a MacGyver picture  on the window
			image_macgyver = pygame.image.load("pictures/MacGyver.png").convert_alpha()
			image_macgyver = pygame.transform.scale(image_macgyver, (30, 30))
			mac = image_macgyver.get_rect()
			mac = mac.move(0, 0)
			g.window.blit(image_macgyver, mac)
			pygame.display.flip()
			mcg_depl = Move()
			l_test = mcg_depl.laby.maze
			key1 = (0, 0)
			key2 = (0, 0)
			pygame.key.set_repeat(400, 30)
			background = pygame.image.load("pictures/Background.jpg").convert_alpha()
			g.window.blit(background, (0, 0))

			font = pygame.font.SysFont('comicsansms', 40, True, False)
			text = font.render("press ENTER to start", 1, (255, 255, 255))
			text1 = font.render("press ESC to quit", 1, (255, 255, 255))

			font2 = pygame.font.SysFont('comicsansms', 28, True, False)
			text2 = font2.render("Welcome to the macGyver Game ", 1, (255, 255, 0))
			text3 = font2.render("you must collect all items on the map", 1, (255, 225, 0))
			text4 = font2.render("and meet the guardian to escape the maze", 1, (255, 200, 0))
			textrect2 = text2.get_rect(center=(225, 60))
			textrect3 = text3.get_rect(center=(225, 120))
			textrect4 = text4.get_rect(center=(225, 150))
			g.window.blit(text2, textrect2)
			g.window.blit(text3, textrect3)
			g.window.blit(text4, textrect4)
			g.window.blit(text, (50, 240))
			g.window.blit(text1, (80, 270))
			pygame.display.flip()
			pygame.display.update()

			continue_home = 1
			continue_game = 1

		#loop continue home
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

		#loop continue game
			while continue_game:
				#Keyboard touch used to quit game
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						continuer = 0
					if event.type == pygame.KEYDOWN:
						g.init_background()
						# Keyboard touch used to moove macGyver
						if event.key == K_DOWN:
							key2 = mcg_depl.deplacement(key1, l_test, "bottom")
							if key1 == key2 or (key2[0] < 0) or (key2[0] > 14) or key2[1] < 0 or key2[1] > 14:
								pass
							else:
								mac = mac.move((0), (30))
								g.window.blit(image_macgyver, mac)

						if event.key == K_LEFT:
							key2 = mcg_depl.deplacement(key1, l_test, "left")
							if key1 == key2:
								pass
							else:
								mac = mac.move((-30), (0))
								g.window.blit(image_macgyver, mac)

						if event.key == K_UP:
							key2 = mcg_depl.deplacement(key1, l_test, "top")
							if key1 == key2:
								pass
							else:
								mac = mac.move((0), (-30))
								g.window.blit(image_macgyver, mac)

						if event.key == K_RIGHT:
							key2 = mcg_depl.deplacement(key1, l_test, "right")
							if key1 == key2:
								pass
							else:
								mac = mac.move((30), (0))
								g.window.blit(image_macgyver, mac)

						key1 = key2

						# check if the items have been picked or not
						if (mac == rect_ether):
							count += 1
							rect_ether = rect_ether.move(450, 450)

						if (mac == rect_tube):
							count += 1
							rect_tube = rect_tube.move(450, 450)

						if (mac == rect_needle):
							count += 1
							rect_needle = rect_needle.move(450, 450)

						# Re-pasting all after the events
						g.wall()
						g.window.blit(image_guardian, gardian_rect)
						g.window.blit(image_macgyver, mac)
						g.window.blit(image_ether, rect_ether)
						g.window.blit(image_tube, rect_tube)
						g.window.blit(image_needle, rect_needle)
						g.score_display(count)

						# endgame, game won or loose

						if (mac == gardian_rect and count == 3):
							font = pygame.font.SysFont('comicsansms', 70, True, False)
							text = font.render("You win!", 1, (255, 255, 255))
							textrect = text.get_rect()
							textrect.move_ip(80, 190)
							g.window.blit(text, textrect)
							pygame.display.flip()
							time.sleep(3)
							continue_home = 1
							continue_game = 0

						if (mac == gardian_rect and count != 3):
							font = pygame.font.SysFont('comicsansms', 60, True, False)
							text = font.render("GAME OVER!", 1, (255, 0, 0))
							textrect = text.get_rect()
							textrect.move_ip(60, 190)
							g.window.blit(text, textrect)
							pygame.display.flip()
							time.sleep(3)
							continue_home = 1
							continue_game = 0

					fps_clock.tick(fps)

		pygame.quit()

if __name__ == "__main__":
	Game()
