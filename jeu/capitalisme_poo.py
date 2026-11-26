if __package__ in (None, ""):
  import sys
  from pathlib import Path

  sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
  __package__ = "jeu"

from .Menu import Menu
import pygame
from .Session import Session
from .Joueur import Joueur
from .Loging import Loging
from .Save import loading_save
#class Logique (Menu):
class Logique() : 
  def __init__(self):
    self.loging = Loging()
    self.save = loading_save(self.loging.identifiant)
    self.session = Session(self.save)
    self.joueur = Joueur(self.session.save)
   
    self.menu = Menu(self.joueur, self.session)

    self.running= True
    self.clock = pygame.time.Clock()
    self.run()
  def run(self):
    self.menu.display_menu()
    pygame.display.flip()
    while self.running:
      self.menu.handling_events_menu()
      self.clock.tick(60)

pygame.init()
game=Logique()

