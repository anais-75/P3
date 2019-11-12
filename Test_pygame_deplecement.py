#Importatinon et initialisation de la bibliothèque Pygame
#!/usr/bin/python3
# coding: utf-8 
import pygame
from pygame.locals import *
pygame.init()
 
#Affichage des images
fenetre = pygame.display.set_mode((640, 480))
 
fond = pygame.image.load("Background.jpg").convert()
fenetre.blit(fond, (0,0))
 
perso = pygame.image.load("MacGyver.png").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)
 
pygame.display.flip()
 
#Rafraîchissement
pygame.display.flip()
 
#Pour la fluidité du déplacement
pygame.key.set_repeat(400, 30)
 
#Boucle Infinie
continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                position_perso = position_perso.move(0,30)
            if event.key == K_LEFT:
                position_perso = position_perso.move(-30,0)
            if event.key == K_UP:
                position_perso = position_perso.move(0,-30)
            if event.key == K_RIGHT:
                position_perso = position_perso.move(30,0)
         
 
#Re-collage
    fenetre.blit(fond, (0,0))
    fenetre.blit(perso, position_perso)
 
#Rafeaîchissement
    pygame.display.flip()
