from Session import *
from Joueur import *
#class Menu(Session,Joueur):
class Menu():
  def __init__(self,joueur,session):
   # super().__init__()
   self.joueur=joueur
   self.session=session
  def display_menu(self, clear=True, middle=False):
    if clear:
      self.screen.fill("black")
      pygame.draw.rect(self.screen,"red", pygame.Rect(0,self.hauteur_ecran//2-(self.hauteur_ecran//20),self.longueur_ecran, self.hauteur_ecran//10))
    if middle:
      pygame.draw.rect(self.screen, "black", pygame.Rect(0, 0, self.move_animation * 2, self.hauteur_ecran))
      pygame.draw.rect(self.screen, "red", pygame.Rect(0, self.hauteur_ecran // 2 - (self.hauteur_ecran // 20), self.move_animation * 2, self.hauteur_ecran // 10))

    pygame.draw.rect(self.screen, "black", pygame.Rect((self.longueur_ecran - (self.longueur_ecran//4)) + (self.move_animation - self.animation), round(self.hauteur_ecran / 100 * 3), self.longueur_ecran // 4, self.hauteur_ecran // 10))
    print_in_screen(self.screen, f"{self.argent}@", [(self.longueur_ecran - (self.longueur_ecran//4)) + (self.move_animation - self.animation), round(self.hauteur_ecran / 100 * 3)], size=self.hauteur_ecran // 10)
    print_in_screen(self.screen, "stop", [(self.longueur_ecran // 2 - (self.longueur_ecran//30)) + (self.move_animation - self.animation), self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((2 + self.position_bouton_menu) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)
    print_in_screen(self.screen, "paramètre", [(self.longueur_ecran // 2 - (self.longueur_ecran//30)) + (self.move_animation - self.animation), self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((1 + self.position_bouton_menu) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)
    print_in_screen(self.screen,"jouer", [(self.longueur_ecran//2-(self.longueur_ecran//30)) + (self.move_animation - self.animation), self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - (self.position_bouton_menu * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)
    print_in_screen(self.screen, "magasin", [(self.longueur_ecran // 2 -(self.longueur_ecran//30)) + (self.move_animation - self.animation), self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((-1 + self.position_bouton_menu) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)

  def display_magasin(self):
    pygame.draw.rect(self.screen, "black", pygame.Rect((self.longueur_ecran // 2 - (self.longueur_ecran//6)) + self.move_animation, 0, self.longueur_ecran, self.hauteur_ecran))
    pygame.draw.rect(self.screen, "red", pygame.Rect((self.longueur_ecran // 2 - (self.longueur_ecran//6)) + self.move_animation, self.hauteur_ecran // 2 - (self.hauteur_ecran // 20), self.longueur_ecran, self.hauteur_ecran // 10))
    print_in_screen(self.screen, f"amortie          {self.Pamorti}@", [(self.longueur_ecran // 2 - (self.longueur_ecran//30)) + self.move_animation, self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((1 + self.position_bouton_magasin) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)
    print_in_screen(self.screen, f"carburant      {self.Pcarburant}@", [(self.longueur_ecran // 2 - (self.longueur_ecran//30)) + self.move_animation, self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - (self.position_bouton_magasin * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)
    print_in_screen(self.screen, f"tu veux gagner 100@? clique ici!", [(self.longueur_ecran // 2 - (self.longueur_ecran // 6)) + self.move_animation, self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((-15 + self.position_bouton_magasin) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)

  def display_parametre(self):
    pygame.draw.rect(self.screen, "black", pygame.Rect((self.longueur_ecran // 2 - (self.longueur_ecran // 6)) + self.move_animation, 0, self.longueur_ecran, self.hauteur_ecran))
    pygame.draw.rect(self.screen, "red", pygame.Rect((self.longueur_ecran // 2 - (self.longueur_ecran // 6)) + self.move_animation, self.hauteur_ecran // 2 - (self.hauteur_ecran // 20), self.longueur_ecran, self.hauteur_ecran // 10))
    print_in_screen(self.screen, "sauvgarder les paramètres écran", [(self.longueur_ecran // 2 - (self.longueur_ecran // 6)) + self.move_animation, self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((2 + self.position_bouton_parametre) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)
    print_in_screen(self.screen, f"longueur de l'écran: {self.changement_longueur_ecran}", [(self.longueur_ecran // 2 - (self.longueur_ecran // 10)) + self.move_animation, self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((1 + self.position_bouton_parametre) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)
    print_in_screen(self.screen, f"hauteur de l'écran:   {self.changement_hauteur_ecran}", [(self.longueur_ecran // 2 - (self.longueur_ecran // 10)) + self.move_animation, self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - (self.position_bouton_parametre * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)

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
        self.position_bouton_parametre+=self.move_interface
        self.display_parametre()
      pygame.display.flip()
    if take_key_and_actualise(pygame.K_RETURN):
      if self.interface_actuelle=="menu":
        if  self.position_bouton_menu==-2:
          save_game(self.file, self.carburantT, self.argent, self.Ncarburant, self.amorti,self.Namorti,self.saved_hauteur_ecran,self.saved_longueur_ecran)
          self.running=False
        elif self.position_bouton_menu==-1:
          for i in range(-self.animation, -100, 2):
            self.move_animation=-i
            self.display_menu()
            self.display_parametre()
            pygame.display.flip()
          self.interface_actuelle="paramètre"
        elif self.position_bouton_menu==0:
          print("jouer")
        elif self.position_bouton_menu==1:
          for i in range(-self.animation, -100, 2):
            self.move_animation=-i
            self.display_menu()
            self.display_magasin()
            pygame.display.flip()
          self.interface_actuelle="magasin"
      elif self.interface_actuelle=="magasin":
        if self.position_bouton_magasin == -1 and self.Pamorti<= self.argent:
          self.argent = round(self.argent-self.Pamorti,1)
          self.Namorti += 1
          self.amorti += 1
          self.Pamorti=round(self.Pamorti*1.4,1)
          self.display_magasin()
          self.display_menu(clear=False,middle=True)
          pygame.display.flip()
        elif self.position_bouton_magasin == 0:
          self.argent = round(self.argent - self.Pcarburant, 1)
          self.Ncarburant += 1
          self.carburantT *= 1.5
          self.Pcarburant = round(self.Pcarburant * 1.5, 1)
          self.display_magasin()
          self.display_menu(clear=False, middle=True)
          pygame.display.flip()
        elif self.position_bouton_magasin == 15:
          self.argent+=100
          self.display_menu(clear=False,middle=True)
          pygame.display.flip()
      elif self.interface_actuelle=='paramètre':
        if self.position_bouton_parametre==0:
          self.changement_hauteur_ecran = 0
          self.display_parametre()
          pygame.display.flip()
          escape = False
          while not take_key_and_actualise(pygame.K_RETURN) and not escape:
            self.changement_hauteur_ecran = write(self.changement_hauteur_ecran, letre=False, symbole=False)
            self.display_parametre()
            pygame.display.flip()
            if pygame.key.get_pressed()[pygame.K_z] and (
                pygame.key.get_pressed()[pygame.K_RCTRL] or pygame.key.get_pressed()[pygame.K_LCTRL]):
              escape = True
              self.changement_hauteur_ecran = self.changement_hauteur_ecran
          self.changement_hauteur_ecran = self.changement_hauteur_ecran
          self.screen = pygame.display.set_mode((self.longueur_ecran, self.hauteur_ecran))
          self.display_menu()
          self.display_parametre()
          pygame.display.flip()
        elif self.position_bouton_parametre==-1:
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
              self.changement_hauteur_ecran = self.longueur_ecran
          self.longueur_ecran = self.changement_longueur_ecran
          self.screen = pygame.display.set_mode((self.longueur_ecran, self.hauteur_ecran))
          self.display_menu()
          self.display_parametre()
          pygame.display.flip()
        elif self.position_bouton_parametre==-2:
          self.saved_hauteur_ecran=self.hauteur_ecran
          self.saved_longueur_ecran=self.longueur_ecran
    if take_key_and_actualise(pygame.K_LEFT) and (self.interface_actuelle=="magasin"or self.interface_actuelle=="paramètre"):
      for i in range(100, self.animation, 2):
        self.move_animation = i
        self.display_menu(clear=False, middle=True)
        pygame.display.flip()
      self.interface_actuelle="menu"