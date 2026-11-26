import pygame
class Start:
  def __init__(self):
    self.running = True
    self.clock = pygame.time.Clock()
    self.longueur_ecran =1200
    self.hauteur_ecran =600
    self.started_screen = pygame.display.set_mode((self.longueur_ecran, self.hauteur_ecran))

    pygame.mouse.set_visible(False)
