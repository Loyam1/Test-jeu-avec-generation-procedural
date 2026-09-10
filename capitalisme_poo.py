from time import *
from save_op import *
from op import *
from copy import *
import pickle
import pygame
from print_in_screen import *
hauteur_ecran=600
longueur_ecran=1200
position_bouton_menu=-1
pseudo="test"
file = "sauvegard_" + pseudo + ".pkl"
class Joueur ():
  def __init__(self,save):
    self.carburantT=save["carburantT"]
    self.argent = save["argent"]
    self.Ncarburant=save["Ncarburant"]
    self.amorti=save["amorti"]
    self.Namorti=save["Namorti"]
class Start:
  def __init__(self, pseudo):
    self.running = True
    self.pseudo=pseudo
    self.running = True
    self.clock = pygame.time.Clock()
    self.point = 0
    self.joueur = Joueur(load(file))
    save_game(file, self.joueur.carburantT, self.joueur.argent, self.joueur.Ncarburant, self.joueur.amorti, self.joueur.Namorti)
class Menu(Start):
  def __init__(self):
    print(self.running)
    self.display_menu()
  def display_menu(self):
    self.screen = pygame.display.set_mode((longueur_ecran, hauteur_ecran))
    self.screen.fill("black")
    pygame.mouse.set_visible(False)
    pygame.draw.rect(self.screen,"red", pygame.Rect(0,hauteur_ecran//2-20,longueur_ecran, 40))
    print_in_screen(self.screen,"jouer",[longueur_ecran//2-15,hauteur_ecran//2-18-((position_bouton_menu)*50)],size=50)
    print_in_screen(self.screen, "stop", [longueur_ecran // 2 - 15, hauteur_ecran // 2 - 18-((1+position_bouton_menu)*50)], size=50)
    print_in_screen(self.screen, "magasin", [longueur_ecran // 2 - 15, hauteur_ecran // 2 - 18-((-1+position_bouton_menu)*50)], size=50)
    pygame.display.flip()
  def handling_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
      self.player.velocity[1] = -1
    elif keys[pygame.K_DOWN]:
      self.player.velocity[1] = 1
    else:
      self.player.velocity[1] = 0

pygame.init()
game = Start(pseudo)
game = Menu()
while True:
  a=1