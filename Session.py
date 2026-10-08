import pygame
from Chargement_sauvegarde import *
class Session(Chargement_sauvegarde):
  def __init__(self,):
    super().__init__()
    self.file=self.save["file"]
    self.longueur_ecran = self.save["longueur_ecran"]
    self.hauteur_ecran = self.save["hauteur_ecran"]
    self.saved_longueur_ecran = self.longueur_ecran
    self.saved_hauteur_ecran = self.hauteur_ecran
    self.changement_longueur_ecran = self.longueur_ecran
    self.changement_hauteur_ecran = self.hauteur_ecran
    self.screen = pygame.display.set_mode((self.longueur_ecran, self.hauteur_ecran))
    self.animation = self.longueur_ecran // 2 + (self.longueur_ecran // 30)
    self.move_animation = self.animation
    self.position_bouton_menu = 0
    self.position_bouton_parametre = 0
    self.position_bouton_magasin = 0
    self.interface_actuelle = "menu"
    self.move_interface=0