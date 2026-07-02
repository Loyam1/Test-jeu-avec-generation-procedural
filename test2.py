import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Display Text in Pygame")

font = pygame.font.Font(None, 74)
text = font.render("Hello, Pygame!", False, (255, 255, 255))
text2 = font.render("Hello, Pygame!", True, (255, 255, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    screen.blit(text, (250, 200))
    screen.blit(text2, (250, 300))
    pygame.display.flip()