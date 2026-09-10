from itertools import repeat
from time import sleep
from print_in_screen import *
import pygame
import random
cote_ecran=500
historique_ball =[]

class Entities:
  def __init__(self, x, y, longueur, largueur, color, velocity):
    self.rect = pygame.Rect(x, y, longueur, largueur)
    self.speed = 5
    self.velocity = velocity
    self.color = color

  def move(self):
    self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

  def draw(self, screen):
    pygame.draw.rect(screen,self.color,self.rect)

class Player (Entities):
  def __init__(self, x, y, longueur, largueur, color, velocity):
    super().__init__(x, y, longueur, largueur, color, velocity)

class Ball (Entities):
  def __init__(self, x, y, longueur, largueur, color, velocity):
    super().__init__(x, y, longueur, largueur, color, velocity)
  def rebond (self):
    return  -random.randint(int(self.velocity[1]*10)-5,int(self.velocity[1]*10)+5)/10


class Game:
  def __init__(self, screen,):
    self.screen = screen
    self.running = True
    self.clock = pygame.time.Clock()
    self.point = 0


    historique_ball.append(Ball(cote_ecran // 2, cote_ecran // (1 / 0.4875), cote_ecran // 40, cote_ecran // 40, "red",[1, random.randint(-5, 5) / 10]))
    self.ball = historique_ball[-1]
    self.player = Player(cote_ecran//80, cote_ecran//(1/0.4375), 20, cote_ecran//8, "white", [0, 0])

  def handling_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
      self.player.velocity[1] = -1
    elif keys[pygame.K_DOWN]:
      self.player.velocity[1] = 1
    else:
      self.player.velocity[1] = 0

  def update(self):
    self.player.move()
    self.ball.move()
    if self.ball.rect.colliderect(self.player.rect):
      self.ball.velocity=[-self.ball.velocity[0],self.ball.rebond()]
      self.point+=1
    elif self.ball.rect.left <= 5 :
      self.ball.velocity=[0,0]
      for i in range(0,4):
        self.ball.color="blue"
        self.display()
        pygame.display.flip()
        sleep(0.25)
        self.ball.color = "red"
        self.display()
        pygame.display.flip()
        sleep(0.25)
      historique_ball.append(Ball(cote_ecran // 2, cote_ecran // (1 / 0.4875), cote_ecran // 40, cote_ecran // 40, "red",[1, random.randint(-5, 5) / 10]))
      self.ball = historique_ball[-1]
      self.player = Player(cote_ecran // 80, cote_ecran // (1 / 0.4375), 20, cote_ecran // 8, "white", [0, 0])
    elif self.ball.rect.right >= cote_ecran :
      self.ball.velocity=[-self.ball.velocity[0],self.ball.rebond()]
    elif self.ball.rect.top <= 0 :
      self.ball.velocity=[self.ball.velocity[0],self.ball.rebond()]
    elif self.ball.rect.bottom >= cote_ecran :
      self.ball.velocity=[self.ball.velocity[0],self.ball.rebond()]

  def display(self):
    self.screen.fill("black")
  #  self.ball.draw(self.screen)
    for e in historique_ball:
      e.draw(self.screen)
    self.player.draw(self.screen)
    print_in_screen(screen,f"{self.point}",[0, 0],color="red")
    pygame.display.flip()

  def run(self):
    while self.running:
      self.handling_events()
      self.update()
      self.display()
      self.clock.tick(60)


pygame.init()
screen = pygame.display.set_mode((cote_ecran, cote_ecran))
game = Game(screen)
game.run()

pygame.quit()