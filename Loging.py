from print_in_screen import *
from Save import *
from Start import *
from chiffrement import *
from write import *
class Loging(Start):
  def __init__(self):
    super().__init__()
    self.position_loging=-1
    self.erone=False
    self.new_user=False
    self.identifiant = ""
    self.mot_de_passe = ""
    self.confirmation_mot_de_passe=""
    self.conection = [False, " "]
    self.user_name_to_short=False
    self.password_to_short = False
    self.user_name_allredy_take=False
    self.different_password =False
    self.loging_logique()
  def display_loging(self):
    self.started_screen.fill("black")
    pygame.draw.rect(self.started_screen, "red",pygame.Rect(0, self.hauteur_ecran // 2 - (self.hauteur_ecran // 20), self.longueur_ecran,self.hauteur_ecran // 10))
    print_in_screen(self.started_screen,f"identifiant:  {self.identifiant}",[(self.longueur_ecran // 2 - (self.longueur_ecran // 3)),self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((1 + self.position_loging) * self.hauteur_ecran // 10)],size=self.hauteur_ecran // 10)
    print_in_screen(self.started_screen, f"mot de passe:  {self.mot_de_passe}",[(self.longueur_ecran // 2 - (self.longueur_ecran // 3)),self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - (self.position_loging * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)
    if self.erone:
      print_in_screen(self.started_screen, "nom d'utilisateur ou mot de passe éroné", [(self.longueur_ecran // 2 - (self.longueur_ecran // 3)),self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((2 + self.position_loging) * self.hauteur_ecran // 10)],size=self.hauteur_ecran // 20)
    if self.password_to_short:
        print_in_screen(self.started_screen, "le mot de passe est trop court",[(self.longueur_ecran // 2 - (self.longueur_ecran // 3)),self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((2 + self.position_loging) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 20)
    elif self.different_password:
      print_in_screen(self.started_screen, "les mots de passe sont différent",[(self.longueur_ecran // 2 - (self.longueur_ecran // 3)),self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((2 + self.position_loging) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 20)
    elif self.user_name_to_short:
      print_in_screen(self.started_screen, "nom d'utilisateur trop court",[(self.longueur_ecran // 2 - (self.longueur_ecran // 3)),self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((2 + self.position_loging) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 20)
    elif self.user_name_allredy_take:
      print_in_screen(self.started_screen, "nom d'utilisateur déjà utilisé",[(self.longueur_ecran // 2 - (self.longueur_ecran // 3)),self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((2 + self.position_loging) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 20)
    if self.new_user:
      print_in_screen(self.started_screen, f"confirmation du mot de passe:  {self.confirmation_mot_de_passe}", [(self.longueur_ecran // 2 - (self.longueur_ecran // 3)),self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((-1 + self.position_loging) * self.hauteur_ecran // 10)],size=self.hauteur_ecran // 10)
    else:
      print_in_screen(self.started_screen, "nouvelle utilisateur", [(self.longueur_ecran // 2 - (self.longueur_ecran // 3)),self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((-1 + self.position_loging) * self.hauteur_ecran // 10)],size=self.hauteur_ecran // 10)
  def loging_logique(self):
    pygame.event.get()
    self.display_loging()
    pygame.display.flip()
    while not self.conection[0]:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
      if self.position_loging==-1:
        self.identifiant=write(self.identifiant)
        self.display_loging()
        pygame.display.flip()
        if take_key_and_actualise(pygame.K_RETURN) or take_key_and_actualise(pygame.K_UP):
          self.position_loging=0
      if self.position_loging==0:
        self.mot_de_passe = write(self.mot_de_passe)
        self.display_loging()
        pygame.display.flip()
        if take_key_and_actualise(pygame.K_DOWN):
          self.position_loging = -1
          self.display_loging()
          pygame.display.flip()
        elif take_key_and_actualise(pygame.K_RETURN):
          if not self.new_user:
            if utilisateur(self.identifiant,chiffrement_mot_de_passe(self.mot_de_passe))[1]:
              return

            else:
              self.erone=True
              self.display_loging()
              pygame.display.flip()
          else:
            self.position_loging = 1
            self.display_loging()
            pygame.display.flip()
        elif take_key_and_actualise(pygame.K_UP):
          self.position_loging = 1
          self.display_loging()
          pygame.display.flip()
      if self.position_loging==1:
        if not self.new_user:
          if take_key_and_actualise(pygame.K_RETURN):
            self.new_user = True
            self.erone=False
            self.display_loging()
            pygame.display.flip()
          elif take_key_and_actualise(pygame.K_DOWN):
            self.position_loging = 0
            self.display_loging()
            pygame.display.flip()
        else:
          self.confirmation_mot_de_passe = write(self.confirmation_mot_de_passe)
          self.display_loging()
          pygame.display.flip()
          if take_key_and_actualise(pygame.K_RETURN):
            if len(self.mot_de_passe) > 4:
              self.password_to_short = False
              if self.mot_de_passe==self.confirmation_mot_de_passe:
                self.different_password = False
                if len(self.identifiant) > 2:
                  self.user_name_to_short = False
                  if not utilisateur(self.identifiant,chiffrement_mot_de_passe(self.mot_de_passe))[0]:
                    add_utilisateur(self.identifiant,chiffrement_mot_de_passe(self.mot_de_passe))
                    return

                  else:
                    self.user_name_allredy_take=True
                    self.display_loging()
                    pygame.display.flip()
                else:
                  self.user_name_to_short = True
                  self.display_loging()
                  pygame.display.flip()
              else:
                self.different_password=True
                self.display_loging()
                pygame.display.flip()
            else:
              self.password_to_short = True
              self.display_loging()
              pygame.display.flip()
          elif take_key_and_actualise(pygame.K_DOWN):
            self.position_loging = 0
            self.display_loging()
            pygame.display.flip()
