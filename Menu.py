import pygame
from print_in_screen import print_in_screen
from take_key_and_actualise import take_key_and_actualise
from Save import save_game
from write import write
#class Menu(Session,Joueur):
class Menu():
  def __init__(self,joueur,session):
   # super().__init__()
   self.joueur=joueur
   self.session=session
  def display_menu(self, clear=True, middle=False):
    if clear:
      self.session.screen.fill("black")
      pygame.draw.rect(self.session.screen,"red", pygame.Rect(0,self.session.hauteur_ecran//2-(self.session.hauteur_ecran//20),self.session.longueur_ecran, self.session.hauteur_ecran//10))
    if middle:
      pygame.draw.rect(self.session.screen, "black", pygame.Rect(0, 0, self.move_animation * 2, self.session.hauteur_ecran))
      pygame.draw.rect(self.session.screen, "red", pygame.Rect(0, self.session.hauteur_ecran // 2 - (self.session.hauteur_ecran // 20), self.move_animation * 2, self.session.hauteur_ecran // 10))

    pygame.draw.rect(self.session.screen, "black", pygame.Rect((self.session.longueur_ecran - (self.session.longueur_ecran//4)) + (self.move_animation - self.session.animation), round(self.session.hauteur_ecran / 100 * 3), self.session.longueur_ecran // 4, self.session.hauteur_ecran // 10))
    print_in_screen(self.session.screen, f"{self.joueur.argent}@", [(self.session.longueur_ecran - (self.session.longueur_ecran//4)) + (self.move_animation - self.session.animation), round(self.session.hauteur_ecran / 100 * 3)], size=self.session.hauteur_ecran // 10)
    print_in_screen(self.session.screen, "stop", [(self.session.longueur_ecran // 2 - (self.session.longueur_ecran//30)) + (self.move_animation - self.session.animation), self.session.hauteur_ecran // 2 - round(self.session.hauteur_ecran / 100 * 3) - ((2 + self.session.position_bouton_menu) * self.session.hauteur_ecran // 10)], size=self.session.hauteur_ecran // 10)
    print_in_screen(self.session.screen, "paramètre", [(self.session.longueur_ecran // 2 - (self.session.longueur_ecran//30)) + (self.move_animation - self.session.animation), self.session.hauteur_ecran // 2 - round(self.session.hauteur_ecran / 100 * 3) - ((1 + self.session.position_bouton_menu) * self.session.hauteur_ecran // 10)], size=self.session.hauteur_ecran // 10)
    print_in_screen(self.session.screen,"jouer", [(self.session.longueur_ecran//2-(self.session.longueur_ecran//30)) + (self.move_animation - self.session.animation), self.session.hauteur_ecran // 2 - round(self.session.hauteur_ecran / 100 * 3) - (self.session.position_bouton_menu * self.session.hauteur_ecran // 10)], size=self.session.hauteur_ecran // 10)
    print_in_screen(self.session.screen, "magasin", [(self.session.longueur_ecran // 2 -(self.session.longueur_ecran//30)) + (self.move_animation - self.session.animation), self.session.hauteur_ecran // 2 - round(self.session.hauteur_ecran / 100 * 3) - ((-1 + self.session.position_bouton_menu) * self.session.hauteur_ecran // 10)], size=self.session.hauteur_ecran // 10)

  def display_magasin(self):
    pygame.draw.rect(self.session.screen, "black", pygame.Rect((self.session.longueur_ecran // 2 - (self.session.longueur_ecran//6)) + self.move_animation, 0, self.session.longueur_ecran, self.session.hauteur_ecran))
    pygame.draw.rect(self.session.screen, "red", pygame.Rect((self.session.longueur_ecran // 2 - (self.session.longueur_ecran//6)) + self.move_animation, self.session.hauteur_ecran // 2 - (self.session.hauteur_ecran // 20), self.session.longueur_ecran, self.session.hauteur_ecran // 10))
    print_in_screen(self.session.screen, f"amortie          {self.joueur.Pamorti}@", [(self.session.longueur_ecran // 2 - (self.session.longueur_ecran//30)) + self.move_animation, self.session.hauteur_ecran // 2 - round(self.session.hauteur_ecran / 100 * 3) - ((1 + self.session.position_bouton_magasin) * self.session.hauteur_ecran // 10)], size=self.session.hauteur_ecran // 10)
    print_in_screen(self.session.screen, f"carburant      {self.joueur.Pcarburant}@", [(self.session.longueur_ecran // 2 - (self.session.longueur_ecran//30)) + self.move_animation, self.session.hauteur_ecran // 2 - round(self.session.hauteur_ecran / 100 * 3) - (self.session.position_bouton_magasin * self.session.hauteur_ecran // 10)], size=self.session.hauteur_ecran // 10)
    print_in_screen(self.session.screen, f"tu veux gagner 100@? clique ici!", [(self.session.longueur_ecran // 2 - (self.session.longueur_ecran // 6)) + self.move_animation, self.session.hauteur_ecran // 2 - round(self.session.hauteur_ecran / 100 * 3) - ((-15 + self.session.position_bouton_magasin) * self.session.hauteur_ecran // 10)], size=self.session.hauteur_ecran // 10)

  def display_parametre(self):
    pygame.draw.rect(self.session.screen, "black", pygame.Rect((self.session.longueur_ecran // 2 - (self.session.longueur_ecran // 6)) + self.move_animation, 0, self.session.longueur_ecran, self.session.hauteur_ecran))
    pygame.draw.rect(self.session.screen, "red", pygame.Rect((self.session.longueur_ecran // 2 - (self.session.longueur_ecran // 6)) + self.move_animation, self.session.hauteur_ecran // 2 - (self.session.hauteur_ecran // 20), self.session.longueur_ecran, self.session.hauteur_ecran // 10))
    print_in_screen(self.session.screen, "sauvgarder les paramètres écran", [(self.session.longueur_ecran // 2 - (self.session.longueur_ecran // 6)) + self.move_animation, self.session.hauteur_ecran // 2 - round(self.session.hauteur_ecran / 100 * 3) - ((2 + self.session.position_bouton_parametre) * self.session.hauteur_ecran // 10)], size=self.session.hauteur_ecran // 10)
    print_in_screen(self.session.screen, f"longueur de l'écran: {self.changement_longueur_ecran}", [(self.session.longueur_ecran // 2 - (self.session.longueur_ecran // 10)) + self.move_animation, self.session.hauteur_ecran // 2 - round(self.session.hauteur_ecran / 100 * 3) - ((1 + self.session.position_bouton_parametre) * self.session.hauteur_ecran // 10)], size=self.session.hauteur_ecran // 10)
    print_in_screen(self.session.screen, f"hauteur de l'écran:   {self.changement_hauteur_ecran}", [(self.session.longueur_ecran // 2 - (self.session.longueur_ecran // 10)) + self.move_animation, self.session.hauteur_ecran // 2 - round(self.session.hauteur_ecran / 100 * 3) - (self.session.position_bouton_parametre * self.session.hauteur_ecran // 10)], size=self.session.hauteur_ecran // 10)

  def handling_events_menu(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.session.running = False
    def up_or_down():
      if take_key_and_actualise(pygame.K_UP) or take_key_and_actualise(pygame.K_z):
        return 1
      elif take_key_and_actualise(pygame.K_DOWN) or take_key_and_actualise(pygame.K_s):
        return -1
      else:
        return 0
    self.move_interface=up_or_down()
    if self.move_interface!= 0:
      if self.session.interface_actuelle=="menu":
        self.session.position_bouton_menu+=self.move_interface
        self.display_menu()
      elif self.session.interface_actuelle == "magasin":
        self.session.position_bouton_magasin += self.move_interface
        self.display_magasin()
      elif self.session.interface_actuelle=="paramètre":
        self.session.position_bouton_parametre+=self.move_interface
        self.display_parametre()
      pygame.display.flip()
    if take_key_and_actualise(pygame.K_RETURN):
      if self.session.interface_actuelle=="menu":
        if  self.session.position_bouton_menu==-2:
          save_game(self.session.file, self.joueur.carburantT, self.joueur.argent, self.joueur.Ncarburant, self.joueur.amorti,self.joueur.Namorti,self.saved_hauteur_ecran,self.saved_longueur_ecran)
          self.session.running=False
        elif self.session.position_bouton_menu==-1:
          for i in range(-self.session.animation, -100, 2):
            self.move_animation=-i
            self.display_menu()
            self.display_parametre()
            pygame.display.flip()
          self.session.interface_actuelle="paramètre"
        elif self.session.position_bouton_menu==0:
          print("jouer")
        elif self.session.position_bouton_menu==1:
          for i in range(-self.session.animation, -100, 2):
            self.move_animation=-i
            self.display_menu()
            self.display_magasin()
            pygame.display.flip()
          self.session.interface_actuelle="magasin"
      elif self.session.interface_actuelle=="magasin":
        if self.session.position_bouton_magasin == -1 and self.joueur.Pamorti<= self.joueur.argent:
          self.joueur.argent = round(self.joueur.argent-self.joueur.Pamorti,1)
          self.joueur.Namorti += 1
          self.joueur.amorti += 1
          self.joueur.Pamorti=round(self.joueur.Pamorti*1.4,1)
          self.display_magasin()
          self.display_menu(clear=False,middle=True)
          pygame.display.flip()
        elif self.session.position_bouton_magasin == 0:
          self.joueur.argent = round(self.joueur.argent - self.joueur.Pcarburant, 1)
          self.joueur.Ncarburant += 1
          self.joueur.carburantT *= 1.5
          self.joueur.Pcarburant = round(self.joueur.Pcarburant * 1.5, 1)
          self.display_magasin()
          self.display_menu(clear=False, middle=True)
          pygame.display.flip()
        elif self.session.position_bouton_magasin == 15:
          self.joueur.argent+=100
          self.display_menu(clear=False,middle=True)
          pygame.display.flip()
      elif self.session.interface_actuelle=='paramètre':
        if self.session.position_bouton_parametre==0:
          self.display_parametre()
          pygame.display.flip()
          escape = False
          while not take_key_and_actualise(pygame.K_RETURN) and not escape:
            self.changement_hauteur_ecran = write(self.changement_hauteur_ecran, letre=False, symbole=False)
            self.display_parametre()
            self.changement_hauteur_ecran = 0
            pygame.display.flip()
            if pygame.key.get_pressed()[pygame.K_z] and (
                pygame.key.get_pressed()[pygame.K_RCTRL] or pygame.key.get_pressed()[pygame.K_LCTRL]):
              escape = True
              self.changement_hauteur_ecran = self.changement_hauteur_ecran
          self.changement_hauteur_ecran = self.changement_hauteur_ecran
          self.session.screen = pygame.display.set_mode((self.session.longueur_ecran, self.session.hauteur_ecran))
          self.display_menu()
          self.display_parametre()
          pygame.display.flip()
        elif self.session.position_bouton_parametre==-1:
          self.changement_longueur_ecran = 0
          self.display_parametre()
          pygame.display.flip()
          escape = False
          while not take_key_and_actualise(pygame.K_RETURN) and not escape:
            self.changement_longueur_ecran=write(self.changement_longueur_ecran,letre=False,symbole=False)
            self.display_parametre()
            pygame.display.flip()
            if pygame.key.get_pressed()[pygame.K_z]and (pygame.key.get_pressed()[pygame.K_RCTRL] or pygame.key.get_pressed()[pygame.K_LCTRL]):
              escape = True
              self.changement_hauteur_ecran = self.session.longueur_ecran
          self.session.longueur_ecran = self.changement_longueur_ecran
          self.session.screen = pygame.display.set_mode((self.session.longueur_ecran, self.session.hauteur_ecran))
          self.display_menu()
          self.display_parametre()
          pygame.display.flip()
        elif self.session.position_bouton_parametre==-2:
          self.saved_hauteur_ecran=self.session.hauteur_ecran
          self.saved_longueur_ecran=self.session.longueur_ecran
    if take_key_and_actualise(pygame.K_LEFT) and (self.session.interface_actuelle=="magasin"or self.session.interface_actuelle=="paramètre"):
      for i in range(100, self.session.animation, 2):
        self.move_animation = i
        self.display_menu(clear=False, middle=True)
        pygame.display.flip()
      self.session.interface_actuelle="menu"