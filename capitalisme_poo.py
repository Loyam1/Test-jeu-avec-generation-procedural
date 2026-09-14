from xml.sax.saxutils import escape

from save_op import *
from op import *
from copy import *
import pickle
import pygame
from print_in_screen import *
from take_key_and_actualise import *
hauteur_ecran=600
longueur_ecran=1200
pseudo="test"
file = "sauvegard_" + pseudo + ".pkl"
position_bouton_menu=0
position_bouton_paramètre = 0
position_bouton_magasin=0
animation= longueur_ecran // 2 + (longueur_ecran // 30)
key_of_chifre={pygame.K_0:0,pygame.K_1:1,pygame.K_2:2,pygame.K_3:3,pygame.K_4:4,pygame.K_4:4,pygame.K_5:5,pygame.K_6:6,pygame.K_7:7,pygame.K_8:8,pygame.K_9:9}

class Joueur ():
  def __init__(self,save):
    self.carburantT=save["carburantT"]
    self.argent = save["argent"]
    self.Ncarburant=save["Ncarburant"]
    self.amorti=save["amorti"]
    self.Namorti=save["Namorti"]
    self.Pcarburant = 16 / 3
    self.Pamorti = 30 / 7
    for i in range(0, self.Ncarburant):
      self.Pcarburant = round(self.Pcarburant * 1.5, 1)
    for i in range(0, self.Namorti):
      self.Pamorti = round(self.Pamorti * 1.4, 1)
class Start:
  def __init__(self, pseudo):
    self.pseudo=pseudo
    self.running = True
    self.clock = pygame.time.Clock()
    self.joueur = Joueur(load(file))
    pygame.mouse.set_visible(False)

class Menu(Start):
  def __init__(self):
    super().__init__(self)
    self.animation = animation
    self.position_bouton_menu = position_bouton_menu
    self.position_bouton_paramètre = position_bouton_paramètre
    self.position_bouton_magasin=position_bouton_magasin
    self.longueur_ecran = longueur_ecran
    self.hauteur_ecran = hauteur_ecran
    self.changement_longueur_ecran=self.longueur_ecran
    self.changement_hauteur_ecran=self.hauteur_ecran
    self.longueur_ecran=longueur_ecran
    self.hauteur_ecran=self.hauteur_ecran
    self.screen = pygame.display.set_mode((self.longueur_ecran, self.hauteur_ecran))
    self.interface_actuelle = "menu"
  def display_menu(self, clear=True, middle=False):
    if clear:
      self.screen.fill("black")
      pygame.draw.rect(self.screen,"red", pygame.Rect(0,self.hauteur_ecran//2-(self.hauteur_ecran//20),self.longueur_ecran, self.hauteur_ecran//10))
    if middle:
      pygame.draw.rect(self.screen, "black", pygame.Rect(0, 0, self.animation * 2, self.hauteur_ecran))
      pygame.draw.rect(self.screen, "red", pygame.Rect(0, self.hauteur_ecran // 2 - (self.hauteur_ecran // 20), self.animation * 2, self.hauteur_ecran // 10))

    pygame.draw.rect(self.screen, "black", pygame.Rect((self.longueur_ecran - (self.longueur_ecran//4)) + (self.animation - animation), round(self.hauteur_ecran / 100 * 3), self.longueur_ecran // 4, self.hauteur_ecran // 10))
    print_in_screen(self.screen, f"{self.joueur.argent}@", [(self.longueur_ecran - (self.longueur_ecran//4)) + (self.animation - animation), round(self.hauteur_ecran / 100 * 3)], size=self.hauteur_ecran // 10)
    print_in_screen(self.screen, "stop", [(self.longueur_ecran // 2 - (self.longueur_ecran//30)) + (self.animation - animation), self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((2 + self.position_bouton_menu) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)
    print_in_screen(self.screen, "paramètre", [(self.longueur_ecran // 2 - (self.longueur_ecran//30)) + (self.animation - animation), self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((1 + self.position_bouton_menu) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)
    print_in_screen(self.screen,"jouer", [(self.longueur_ecran//2-(self.longueur_ecran//30)) + (self.animation - animation), self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((self.position_bouton_menu) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)
    print_in_screen(self.screen, "magasin", [(self.longueur_ecran // 2 -(self.longueur_ecran//30)) + (self.animation - animation), self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((-1 + self.position_bouton_menu) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)

  def display_magasin(self):
    pygame.draw.rect(self.screen, "black", pygame.Rect((self.longueur_ecran // 2 - (self.longueur_ecran//6)) + self.animation, 0, self.longueur_ecran, self.hauteur_ecran))
    pygame.draw.rect(self.screen, "red", pygame.Rect((self.longueur_ecran // 2 - (self.longueur_ecran//6)) + self.animation, self.hauteur_ecran // 2 - (self.hauteur_ecran // 20), self.longueur_ecran, self.hauteur_ecran // 10))
    print_in_screen(self.screen, f"amortie          {self.joueur.Pamorti}@", [(self.longueur_ecran // 2 - (self.longueur_ecran//30)) + self.animation, self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((1 + self.position_bouton_magasin) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)
    print_in_screen(self.screen, f"carburant      {self.joueur.Pcarburant}@", [(self.longueur_ecran // 2 - (self.longueur_ecran//30)) + self.animation, self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((self.position_bouton_magasin) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)
    print_in_screen(self.screen, f"tu veux gagner 100@? clique ici!", [(self.longueur_ecran // 2 - (self.longueur_ecran // 6)) + self.animation, self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((-15 + self.position_bouton_magasin) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)

  def display_paramètre(self):
    pygame.draw.rect(self.screen, "black", pygame.Rect((self.longueur_ecran // 2 - (self.longueur_ecran // 6)) + self.animation, 0, self.longueur_ecran, self.hauteur_ecran))
    pygame.draw.rect(self.screen, "red", pygame.Rect((self.longueur_ecran // 2 - (self.longueur_ecran // 6)) + self.animation, self.hauteur_ecran // 2 - (self.hauteur_ecran // 20), self.longueur_ecran, self.hauteur_ecran // 10))
    print_in_screen(self.screen, f"longueur de l'écrant: {self.changement_longueur_ecran}", [(self.longueur_ecran // 2 - (self.longueur_ecran // 15)) + self.animation, self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((1 + self.position_bouton_paramètre) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)
    print_in_screen(self.screen, f"hauteur de l'écrant:   {self.changement_hauteur_ecran}", [(self.longueur_ecran // 2 - (self.longueur_ecran // 15)) + self.animation, self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((self.position_bouton_paramètre) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)
 #   print_in_screen(self.screen, f"tu veux gagner 100@? clique ici!",[(longueur_ecran // 2 - (longueur_ecran // 6)) + self.animation_magasin,hauteur_ecran // 2 - round(hauteur_ecran / 100 * 3) - ((-15 + self.position_bouton_paramètre) * hauteur_ecran // 10)], size=hauteur_ecran // 10)
  def handling_events_menu(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False
    def up_or_down():
      if take_key_and_actualise(pygame.K_UP) or take_key_and_actualise(pygame.K_z):
        return 1
      elif take_key_and_actualise(pygame.K_DOWN) or take_key_and_actualise(pygame.K_s):
        return -1
      else:
        return 0
    self.move_interface=up_or_down()
    if self.move_interface!= 0:
      if self.interface_actuelle=="menu":
        self.position_bouton_menu+=self.move_interface
        self.display_menu()
      elif self.interface_actuelle == "magasin":
        self.position_bouton_magasin += self.move_interface
        self.display_magasin()
      elif self.interface_actuelle=="paramètre":
        self.position_bouton_paramètre+=self.move_interface
        self.display_paramètre()
      pygame.display.flip()
    if take_key_and_actualise(pygame.K_RETURN):
      if self.interface_actuelle=="menu":
        if  self.position_bouton_menu==-2:
          save_game(file, self.joueur.carburantT, self.joueur.argent, self.joueur.Ncarburant, self.joueur.amorti,self.joueur.Namorti)
          self.running=False
        elif self.position_bouton_menu==-1:
          for i in range(-animation, -100, 2):
            self.animation=-i
            self.display_menu()
            self.display_paramètre()
            pygame.display.flip()
          self.interface_actuelle="paramètre"
        elif self.position_bouton_menu==0:
          print("jouer")
        elif self.position_bouton_menu==1:
          for i in range(-animation, -100,2):
            self.animation=-i
            self.display_menu()
            self.display_magasin()
            pygame.display.flip()
          self.interface_actuelle="magasin"
      elif self.interface_actuelle=="magasin":
        if self.position_bouton_magasin == -1 and self.joueur.Pamorti<= self.joueur.argent:
          self.joueur.argent = round(self.joueur.argent-self.joueur.Pamorti,1)
          self.joueur.Namorti += 1
          self.joueur.amorti += 1
          self.joueur.Pamorti=round(self.joueur.Pamorti*1.4,1)
          self.display_magasin()
          self.display_menu(clear=False,middle=True)
          pygame.display.flip()
        elif self.position_bouton_magasin == 0:
          self.joueur.argent = round(self.joueur.argent - self.joueur.Pcarburant, 1)
          self.joueur.Ncarburant += 1
          self.joueur.carburantT *= 1.5
          self.joueur.Pcarburant = round(self.joueur.Pcarburant * 1.5, 1)
          self.display_magasin()
          self.display_menu(clear=False, middle=True)
          pygame.display.flip()
        elif self.position_bouton_magasin == 15:
          self.joueur.argent+=100
          self.display_menu(clear=False,middle=True)
          pygame.display.flip()
      elif self.interface_actuelle=='paramètre':
        if self.position_bouton_paramètre==0:
          self.changement_hauteur_ecran = 0
          self.display_paramètre()
          pygame.display.flip()
          escape=False
          while not take_key_and_actualise(pygame.K_RETURN) or escape:
            for i in key_of_chifre:
              pygame.event.get()
              if take_key_and_actualise(i):
                self.changement_hauteur_ecran=self.changement_hauteur_ecran*10+key_of_chifre[i]
                self.display_paramètre()
                pygame.display.flip()
            if take_key_and_actualise(pygame.K_BACKSPACE):
              self.changement_hauteur_ecran=int(self.changement_hauteur_ecran/10)
              self.display_paramètre()
              pygame.display.flip()
            if take_key_and_actualise(pygame.K_ESCAPE):
              escape=True
              self.changement_hauteur_ecran=self.hauteur_ecran
          self.hauteur_ecran=self.changement_hauteur_ecran
          self.screen = pygame.display.set_mode((self.longueur_ecran, self.hauteur_ecran))
          self.display_menu()
          self.display_paramètre()
          pygame.display.flip()
        elif self.position_bouton_paramètre==-1:
          self.changement_longueur_ecran = 0
          self.display_paramètre()
          pygame.display.flip()
          escape = False
          while not take_key_and_actualise(pygame.K_RETURN) or escape:
            for i in key_of_chifre:
              pygame.event.get()
              if take_key_and_actualise(i):
                self.changement_longueur_ecran = self.changement_longueur_ecran * 10 + key_of_chifre[i]
                self.display_paramètre()
                pygame.display.flip()
            if take_key_and_actualise(pygame.K_BACKSPACE):
              self.changement_longueur_ecran = int(self.changement_longueur_ecran / 10)
              self.display_paramètre()
              pygame.display.flip()
            if take_key_and_actualise(pygame.K_ESCAPE):
              escape = True
              self.changement_hauteur_ecran = self.longueur_ecran
          self.longueur_ecran = self.changement_longueur_ecran
          self.screen = pygame.display.set_mode((self.longueur_ecran, self.hauteur_ecran))
          self.display_menu()
          self.display_paramètre()
          pygame.display.flip()

    if take_key_and_actualise(pygame.K_LEFT) and (self.interface_actuelle=="magasin"or"paramètre"):
      for i in range(100, animation,2):
        self.animation = i
        self.display_menu(clear=False, middle=True)
        pygame.display.flip()
      self.interface_actuelle="menu"

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
take_key_and_actualise_stop()
