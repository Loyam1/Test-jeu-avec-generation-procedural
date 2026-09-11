from time import *

from pygame import K_LEFT

from save_op import *
from op import *
from copy import *
import pickle
import pygame
from print_in_screen import *
hauteur_ecran=600
longueur_ecran=1200
pseudo="test"
file = "sauvegard_" + pseudo + ".pkl"
position_bouton_menu=0
position_bouton_magasin=0
animation_magasin=longueur_ecran//2+40

class Joueur ():
  def __init__(self,save):
    self.carburantT=save["carburantT"]
    self.argent = save["argent"]
    self.Ncarburant=save["Ncarburant"]
    self.amorti=save["amorti"]
    self.Namorti=save["Namorti"]
class Start:
  def __init__(self, pseudo):
    self.pseudo=pseudo
    self.running = True
    self.clock = pygame.time.Clock()
    self.point = 0
    self.joueur = Joueur(load(file))
    pygame.mouse.set_visible(False)
class Menu(Start):
  def __init__(self):
    super().__init__(self)
    self.position_bouton_menu = position_bouton_menu
    self.animation_magasin = animation_magasin
    self.position_bouton_magasin=position_bouton_magasin
    self.screen = pygame.display.set_mode((longueur_ecran, hauteur_ecran))
    self.interface_actuelle = "menu"
  def display_menu(self, clear=True, middle=False):
    if clear:
      self.screen.fill("black")
      pygame.draw.rect(self.screen,"red", pygame.Rect(0,hauteur_ecran//2-(hauteur_ecran//20),longueur_ecran, hauteur_ecran//10))
    if middle:
      pygame.draw.rect(self.screen, "black",pygame.Rect(0, 0, self.animation_magasin*2,hauteur_ecran))
      pygame.draw.rect(self.screen, "red", pygame.Rect(0,hauteur_ecran // 2 - (hauteur_ecran // 20), self.animation_magasin*2,hauteur_ecran // 10))

    print_in_screen(self.screen, "stop", [(longueur_ecran // 2 - 40)+(self.animation_magasin-animation_magasin),hauteur_ecran // 2 - round(hauteur_ecran / 100 * 3) - ((2 + self.position_bouton_menu) * hauteur_ecran // 10)],size=hauteur_ecran // 10)
    print_in_screen(self.screen, "paramètre", [(longueur_ecran // 2 - 40)+(self.animation_magasin-animation_magasin),hauteur_ecran // 2 - round(hauteur_ecran / 100 * 3) - ((1 + self.position_bouton_menu) * hauteur_ecran // 10)],size=hauteur_ecran // 10)
    print_in_screen(self.screen,"jouer",[(longueur_ecran//2-40)+(self.animation_magasin-animation_magasin),hauteur_ecran//2-round(hauteur_ecran/100*3)-((self.position_bouton_menu)*hauteur_ecran//10)],size=hauteur_ecran//10)
    print_in_screen(self.screen, "magasin", [(longueur_ecran // 2 -40)+(self.animation_magasin-animation_magasin), hauteur_ecran // 2 - round(hauteur_ecran/100*3)-((-1+self.position_bouton_menu)*hauteur_ecran//10)], size=hauteur_ecran//10)

  def display_magasin(self):
    pygame.draw.rect(self.screen, "black",pygame.Rect((longueur_ecran // 2 - 40)+self.animation_magasin,0, longueur_ecran,hauteur_ecran))
    pygame.draw.rect(self.screen, "red",pygame.Rect((longueur_ecran // 2 - 40)+self.animation_magasin, hauteur_ecran // 2 - (hauteur_ecran // 20), longueur_ecran, hauteur_ecran // 10))
    print_in_screen(self.screen, "amortie", [(longueur_ecran // 2 - 40)+self.animation_magasin,hauteur_ecran // 2 - round(hauteur_ecran / 100 * 3) - ((1 + self.position_bouton_magasin) * hauteur_ecran // 10)],size=hauteur_ecran // 10)
    print_in_screen(self.screen, "carburant", [(longueur_ecran // 2 - 40)+self.animation_magasin,hauteur_ecran // 2 - round(hauteur_ecran / 100 * 3) - ((self.position_bouton_magasin) * hauteur_ecran // 10)],size=hauteur_ecran // 10)

  def handling_events_menu(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False
    def up_or_down(keys):
      if keys[pygame.K_UP] or keys[pygame.K_z]:
        return 1
      elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        return -1
      else:
        return 0
    self.move_interface=up_or_down(pygame.key.get_pressed())
    if self.move_interface!= 0:
      print(self.interface_actuelle)
      if self.interface_actuelle=="menu":
        self.position_bouton_menu+=self.move_interface
        self.display_menu()
      elif self.interface_actuelle=="magasin":
        self.position_bouton_magasin+=self.move_interface
        self.display_magasin()
      pygame.display.flip()
    if pygame.key.get_pressed()[pygame.K_RETURN]:
      if  self.position_bouton_menu==-2:
        save_game(file, self.joueur.carburantT, self.joueur.argent, self.joueur.Ncarburant, self.joueur.amorti,self.joueur.Namorti)
        self.running=False
      elif self.position_bouton_menu==-1:
        print("paramètre")
      elif self.position_bouton_menu==0:
        print("jouer")
      elif self.position_bouton_menu==1:
        for i in range(-animation_magasin,-100):
          self.animation_magasin=-i
          self.display_menu()
          self.display_magasin()
          pygame.display.flip()
        self.interface_actuelle="magasin"
    if pygame.key.get_pressed()[K_LEFT] and self.interface_actuelle=="magasin":
      for i in range(100,animation_magasin):
        self.animation_magasin = i
        self.display_menu(clear=False, middle=True)
        pygame.display.flip()
      self.interface_actuelle="menu"
    sleep(0.2)

class Logique (Menu):
  def __init__(self):
    super().__init__()
    self.run()
  def run(self):
    self.display_menu()
    pygame.display.flip()
    while self.running:
      self.handling_events_menu()
      self.clock.tick(60)


pygame.init()
game = Logique()
