import pygame
def print_in_screen (screen,text,coordinates,size=30,color="white"):
  pygame.init()
  font = pygame.font.Font(None,size)
  screen.blit(font.render(text, True, color),coordinates)