import pygame
import random


class Entities:
  def __init__(self, x, y, longueur, largueur, color, velocity):
    self.rect = pygame.Rect(x, y, longueur, largueur)
    self.speed = 10
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



class Game:
  def __init__(self, screen):
    self.screen = screen
    self.running = True
    self.clock = pygame.time.Clock()

    self.player = Player(10, 350, 20, 100, "white", [0, 0])
    self.ball = Ball(300, 390, 20, 20,  "red", [1, random.randint(-5,5)/10])


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
      self.ball.velocity=[-self.ball.velocity[0], random.randint(int(self.ball.velocity[1]*10)-5,int(self.ball.velocity[1]*10)+5)/10]
    if self.ball.rect.right >= 800 :
      self.ball.velocity=[-self.ball.velocity[0], random.randint(int(self.ball.velocity[1]*10)-5,int(self.ball.velocity[1]*10)+5)/10]


  def display(self):
    self.screen.fill("black")
    self.ball.draw(self.screen)
    self.player.draw(self.screen)
    pygame.display.flip()

  def run(self):
    while self.running:
      self.handling_events()
      self.update()
      self.display()
      self.clock.tick(60)


pygame.init()
screen = pygame.display.set_mode((800, 800))
game = Game(screen)
game.run()

pygame.quit()