from time import *
from save_op import *
from op import *
from copy import *
import pickle
import pygame
from print_in_screen import *
cote_ecran=500
screen = pygame.display.set_mode((cote_ecran, cote_ecran))
pseudo="Loyam"
file = "sauvegard_" + pseudo + ".pkl"
class Joueur ():
  def __init__(self,save):
    self.carburantT=save["carburantT"]
    self.argent = save["argent"]
    self.Ncarburant=save["Ncarburant"]
    self.amorti=save["amorti"]
    self.Namorti=save["Namorti"]
def display(self):
    self.screen.fill("black")
class Game:
  def __init__(self, screen,):
    self.screen = screen
  #  self.running = True
    self.clock = pygame.time.Clock()
    self.point = 0
pygame.init()
game = Game(screen)

#save=load(file)
#joueur=Joueur(save)
#print(joueur.argent)
#new_save(file,joueur.carburantT,joueur.argent,joueur.Ncarburant,joueur.amorti,joueur.Namorti)