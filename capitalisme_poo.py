from Menu import *
from Session import Session
from Joueur import Joueur
#class Logique (Menu):
class Logique() : 
  def __init__(self):
    self.joueur= Joueur()
    self.session= Session()    
    self.menu= Menu(self.joueur, self.session)
    self.run()
  def run(self):
    self.menu.display_menu()
    pygame.display.flip()
    while self.session.running:
      self.menu.handling_events_menu()
      self.session.clock.tick(60)

pygame.init()
game=Logique()

