from Menu import *
from Session import Session
from Joueur import Joueur
#class Logique (Menu):
class Logique() : 
  def __init__(self):
    self.joueur= Joueur()
    self.session= Session()    
    self.menu= Menu(self.joueur, self.session)
    super().__init__()
    self.run()
  def run(self):
    self.display_menu()
    pygame.display.flip()
    while self.running:
      self.handling_events_menu()
      self.clock.tick(60)

pygame.init()
game=Logique()

