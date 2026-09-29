from save_op import *
from op import *
from copy import *
import pickle
import pygame
from print_in_screen import *
from take_key_and_actualise import *
from chiffrement import chiffrement_mot_de_passe

position_bouton_menu=0
position_bouton_paramètre = 0
position_bouton_magasin=0
key_of_chifre={pygame.K_0:0,pygame.K_1:1,pygame.K_2:2,pygame.K_3:3,pygame.K_4:4,pygame.K_5:5,pygame.K_6:6,pygame.K_7:7,pygame.K_8:8,pygame.K_9:9}
key_of_letre={pygame.K_a:"a",pygame.K_z:"z",pygame.K_e:"e",pygame.K_r:"r",pygame.K_t:"t",pygame.K_y:"y",pygame.K_u:"u",pygame.K_i:"i",pygame.K_o:"o",pygame.K_p:"p",pygame.K_q:"q",pygame.K_s:"s",pygame.K_d:"d",pygame.K_f:"f",pygame.K_g:"g",pygame.K_h:"h",pygame.K_j:"j",pygame.K_k:"k",pygame.K_l:"l",pygame.K_m:"m",pygame.K_w:"w",pygame.K_x:"x",pygame.K_c:"c",pygame.K_v:"v",pygame.K_b:"b",pygame.K_n:"n"}
key_of_symbole_up={pygame.K_RIGHTPAREN:"°",pygame.K_ASTERISK:"µ",pygame.K_EQUALS:"+",pygame.K_COLON:"/",pygame.K_SEMICOLON:".",pygame.K_LESS:">",pygame.K_COMMA:"?",pygame.K_EXCLAIM:"§",pygame.K_CARET:"¨",pygame.K_DOLLAR:"£"}
key_of_symbole_down={pygame.K_7:"è",pygame.K_8:"_",pygame.K_9:"ç",pygame.K_0:"à",pygame.K_CARET:"^",pygame.K_COMMA:",",pygame.K_2:"é",pygame.K_EXCLAIM:"!",pygame.K_3:"\"",pygame.K_DOLLAR:"$",pygame.K_1:"&",pygame.K_5:"(",pygame.K_RIGHTPAREN:")",pygame.K_ASTERISK:"*",pygame.K_EQUALS:"=",pygame.K_4:"'",pygame.K_6:"-",pygame.K_SEMICOLON:";",pygame.K_COLON:":",pygame.K_LESS:">"}
key_of_symbole_alt={pygame.K_2:"~",pygame.K_3:"#",pygame.K_4:"{",pygame.K_5:"[",pygame.K_6:"|",pygame.K_7:"`",pygame.K_8:"\\",pygame.K_9:"^",pygame.K_0:"@",pygame.K_RIGHTPAREN:"]",pygame.K_EQUALS:"}",pygame.K_DOLLAR:"¤",pygame.K_e:"€"}

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
  def __init__(self):
    self.running = True
    self.clock = pygame.time.Clock()
    self.longueur_ecran =1200
    self.hauteur_ecran =600
    self.saved_longueur_ecran=self.longueur_ecran
    self.saved_hauteur_ecran=self.hauteur_ecran
    self.changement_longueur_ecran=self.longueur_ecran
    self.changement_hauteur_ecran=self.hauteur_ecran
    self.screen = pygame.display.set_mode((self.longueur_ecran, self.hauteur_ecran))
    self.animation = self.longueur_ecran // 2 + (self.longueur_ecran // 30)
    self.move_animation = self.animation
    pygame.mouse.set_visible(False)

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
  def display_loging(self):
    self.screen.fill("black")
    pygame.draw.rect(self.screen, "red",pygame.Rect(0, self.hauteur_ecran // 2 - (self.hauteur_ecran // 20), self.longueur_ecran,self.hauteur_ecran // 10))
    print_in_screen(self.screen,f"identifiant:  {self.identifiant}",[(self.longueur_ecran // 2 - (self.longueur_ecran // 3)),self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((1 + self.position_loging) * self.hauteur_ecran // 10)],size=self.hauteur_ecran // 10)
    print_in_screen(self.screen, f"mot de passe:  {self.mot_de_passe}",[(self.longueur_ecran // 2 - (self.longueur_ecran // 3)),self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((self.position_loging) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)
    if self.erone:
      print_in_screen(self.screen, "nom d'utilisateur ou mot de passe éroné", [(self.longueur_ecran // 2 - (self.longueur_ecran // 3)),self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((2 + self.position_loging) * self.hauteur_ecran // 10)],size=self.hauteur_ecran // 20)
    if self.password_to_short:
        print_in_screen(self.screen, "le mot de passe est trop court",[(self.longueur_ecran // 2 - (self.longueur_ecran // 3)),self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((2 + self.position_loging) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 20)
    elif self.different_password:
      print_in_screen(self.screen, "les mots de passe sont différent",[(self.longueur_ecran // 2 - (self.longueur_ecran // 3)),self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((2 + self.position_loging) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 20)
    elif self.user_name_to_short:
      print_in_screen(self.screen, "nom d'utilisateur trop court",[(self.longueur_ecran // 2 - (self.longueur_ecran // 3)),self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((2 + self.position_loging) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 20)
    elif self.user_name_allredy_take:
      print_in_screen(self.screen, "nom d'utilisateur déjà utilisé",[(self.longueur_ecran // 2 - (self.longueur_ecran // 3)),self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((2 + self.position_loging) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 20)
    if self.new_user:
      print_in_screen(self.screen, f"confirmation du mot de passe:  {self.confirmation_mot_de_passe}", [(self.longueur_ecran // 2 - (self.longueur_ecran // 3)),self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((-1 + self.position_loging) * self.hauteur_ecran // 10)],size=self.hauteur_ecran // 10)
    else:
      print_in_screen(self.screen, "nouvelle utilisateur", [(self.longueur_ecran // 2 - (self.longueur_ecran // 3)),self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((-1 + self.position_loging) * self.hauteur_ecran // 10)],size=self.hauteur_ecran // 10)
  def write (self,text):
    pygame.event.get()
    if not pygame.key.get_pressed()[pygame.K_RALT]:
      for i in key_of_letre:
        if take_key_and_actualise(i):
          if pygame.key.get_pressed()[pygame.K_LSHIFT] or pygame.key.get_pressed()[pygame.K_RSHIFT]:
            text += f"{(chr(ord(key_of_letre[i])-32))}"
            return text
          else:
            text +=f"{(key_of_letre[i])}"
            return text
    if (pygame.key.get_pressed()[pygame.K_LSHIFT] or pygame.key.get_pressed()[pygame.K_RSHIFT]) and not pygame.key.get_pressed()[pygame.K_RALT]:
      for i in key_of_chifre:
        if take_key_and_actualise(i):
          text+=f"{(key_of_chifre[i])}"
          return text
      for i in key_of_symbole_up:
        if take_key_and_actualise(i):
          text+=f"{key_of_symbole_up[i]}"
          return text
    elif not pygame.key.get_pressed()[pygame.K_RALT]:
      for i in key_of_symbole_down:
        if take_key_and_actualise(i):
          text += f"{(key_of_symbole_down[i])}"
          return text
    else:
      for i in key_of_symbole_alt:
        if take_key_and_actualise(i):
          text += f"{(key_of_symbole_alt[i])}"
          return text
    if take_key_and_actualise(pygame.K_BACKSPACE):
      longueur_text=range(len(text)-1)
      text2=""
      for i in longueur_text:
        text2+=text[i]
      text=text2
      return text
    return text
  def info_ecran_joueur(self):
    self.pseudo = self.identifiant
    self.file = ".sauvegard\\sauvegard_" + self.pseudo + ".pkl"
    self.joueur = Joueur(load(self.file))
    self.longueur_ecran = load(self.file)["longueur_ecran"]
    self.hauteur_ecran = load(self.file)["hauteur_ecran"]
    self.saved_longueur_ecran = self.longueur_ecran
    self.saved_hauteur_ecran = self.hauteur_ecran
    self.changement_longueur_ecran = self.longueur_ecran
    self.changement_hauteur_ecran = self.hauteur_ecran
    self.screen = pygame.display.set_mode((self.longueur_ecran, self.hauteur_ecran))
    self.animation = self.longueur_ecran // 2 + (self.longueur_ecran // 30)
    self.move_animation = self.animation
  def loging_logique(self):
    pygame.event.get()
    self.display_loging()
    pygame.display.flip()
    while not self.conection[0]:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
      if self.position_loging==-1:
        self.identifiant=self.write(self.identifiant)
        self.display_loging()
        pygame.display.flip()
        if take_key_and_actualise(pygame.K_RETURN) or take_key_and_actualise(pygame.K_UP):
          self.position_loging=0
      if self.position_loging==0:
        self.mot_de_passe = self.write(self.mot_de_passe)
        self.display_loging()
        pygame.display.flip()
        if take_key_and_actualise(pygame.K_DOWN):
          self.position_loging = -1
          self.display_loging()
          pygame.display.flip()
        elif take_key_and_actualise(pygame.K_RETURN):
          if not self.new_user:
            if utilisateur(self.identifiant,chiffrement_mot_de_passe(self.mot_de_passe))[1]:
              self.info_ecran_joueur()
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
          self.confirmation_mot_de_passe = self.write(self.confirmation_mot_de_passe)
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
                    self.info_ecran_joueur()
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


class Menu(Loging):
  def __init__(self):
    super().__init__()
    self.position_bouton_menu = position_bouton_menu
    self.position_bouton_paramètre = position_bouton_paramètre
    self.position_bouton_magasin=position_bouton_magasin
    self.interface_actuelle = "menu"
  def display_menu(self, clear=True, middle=False):
    if clear:
      self.screen.fill("black")
      pygame.draw.rect(self.screen,"red", pygame.Rect(0,self.hauteur_ecran//2-(self.hauteur_ecran//20),self.longueur_ecran, self.hauteur_ecran//10))
    if middle:
      pygame.draw.rect(self.screen, "black", pygame.Rect(0, 0, self.move_animation * 2, self.hauteur_ecran))
      pygame.draw.rect(self.screen, "red", pygame.Rect(0, self.hauteur_ecran // 2 - (self.hauteur_ecran // 20), self.move_animation * 2, self.hauteur_ecran // 10))

    pygame.draw.rect(self.screen, "black", pygame.Rect((self.longueur_ecran - (self.longueur_ecran//4)) + (self.move_animation - self.animation), round(self.hauteur_ecran / 100 * 3), self.longueur_ecran // 4, self.hauteur_ecran // 10))
    print_in_screen(self.screen, f"{self.joueur.argent}@", [(self.longueur_ecran - (self.longueur_ecran//4)) + (self.move_animation - self.animation), round(self.hauteur_ecran / 100 * 3)], size=self.hauteur_ecran // 10)
    print_in_screen(self.screen, "stop", [(self.longueur_ecran // 2 - (self.longueur_ecran//30)) + (self.move_animation - self.animation), self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((2 + self.position_bouton_menu) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)
    print_in_screen(self.screen, "paramètre", [(self.longueur_ecran // 2 - (self.longueur_ecran//30)) + (self.move_animation - self.animation), self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((1 + self.position_bouton_menu) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)
    print_in_screen(self.screen,"jouer", [(self.longueur_ecran//2-(self.longueur_ecran//30)) + (self.move_animation - self.animation), self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((self.position_bouton_menu) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)
    print_in_screen(self.screen, "magasin", [(self.longueur_ecran // 2 -(self.longueur_ecran//30)) + (self.move_animation - self.animation), self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((-1 + self.position_bouton_menu) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)

  def display_magasin(self):
    pygame.draw.rect(self.screen, "black", pygame.Rect((self.longueur_ecran // 2 - (self.longueur_ecran//6)) + self.move_animation, 0, self.longueur_ecran, self.hauteur_ecran))
    pygame.draw.rect(self.screen, "red", pygame.Rect((self.longueur_ecran // 2 - (self.longueur_ecran//6)) + self.move_animation, self.hauteur_ecran // 2 - (self.hauteur_ecran // 20), self.longueur_ecran, self.hauteur_ecran // 10))
    print_in_screen(self.screen, f"amortie          {self.joueur.Pamorti}@", [(self.longueur_ecran // 2 - (self.longueur_ecran//30)) + self.move_animation, self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((1 + self.position_bouton_magasin) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)
    print_in_screen(self.screen, f"carburant      {self.joueur.Pcarburant}@", [(self.longueur_ecran // 2 - (self.longueur_ecran//30)) + self.move_animation, self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((self.position_bouton_magasin) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)
    print_in_screen(self.screen, f"tu veux gagner 100@? clique ici!", [(self.longueur_ecran // 2 - (self.longueur_ecran // 6)) + self.move_animation, self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((-15 + self.position_bouton_magasin) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)

  def display_paramètre(self):
    pygame.draw.rect(self.screen, "black", pygame.Rect((self.longueur_ecran // 2 - (self.longueur_ecran // 6)) + self.move_animation, 0, self.longueur_ecran, self.hauteur_ecran))
    pygame.draw.rect(self.screen, "red", pygame.Rect((self.longueur_ecran // 2 - (self.longueur_ecran // 6)) + self.move_animation, self.hauteur_ecran // 2 - (self.hauteur_ecran // 20), self.longueur_ecran, self.hauteur_ecran // 10))
    print_in_screen(self.screen, "sauvgarder les paramètres écran", [(self.longueur_ecran // 2 - (self.longueur_ecran // 6)) + self.move_animation, self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((2 + self.position_bouton_paramètre) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)
    print_in_screen(self.screen, f"longueur de l'écran: {self.changement_longueur_ecran}", [(self.longueur_ecran // 2 - (self.longueur_ecran // 10)) + self.move_animation, self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((1 + self.position_bouton_paramètre) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)
    print_in_screen(self.screen, f"hauteur de l'écran:   {self.changement_hauteur_ecran}", [(self.longueur_ecran // 2 - (self.longueur_ecran // 10)) + self.move_animation, self.hauteur_ecran // 2 - round(self.hauteur_ecran / 100 * 3) - ((self.position_bouton_paramètre) * self.hauteur_ecran // 10)], size=self.hauteur_ecran // 10)

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
          save_game(self.file, self.joueur.carburantT, self.joueur.argent, self.joueur.Ncarburant, self.joueur.amorti,self.joueur.Namorti,self.saved_hauteur_ecran,self.saved_longueur_ecran)
          self.running=False
        elif self.position_bouton_menu==-1:
          for i in range(-self.animation, -100, 2):
            self.move_animation=-i
            self.display_menu()
            self.display_paramètre()
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
        elif self.position_bouton_paramètre==-2:
          self.saved_hauteur_ecran=self.hauteur_ecran
          self.saved_longueur_ecran=self.longueur_ecran
    if take_key_and_actualise(pygame.K_LEFT) and (self.interface_actuelle=="magasin"or self.interface_actuelle=="paramètre"):
      for i in range(100, self.animation, 2):
        self.move_animation = i
        self.display_menu(clear=False, middle=True)
        pygame.display.flip()
      self.interface_actuelle="menu"

class Logique (Menu,Loging):
  def __init__(self):
    super().__init__()
    self.run()
  def run(self):
    self.loging_logique()
    self.display_menu()
    pygame.display.flip()
    while self.running:
      self.handling_events_menu()
      self.clock.tick(60)


pygame.init()
game = Logique()
