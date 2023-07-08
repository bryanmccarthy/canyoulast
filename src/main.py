import pygame
from hero import Hero
from ground import Ground

class Game:
  def __init__(self):
    WIDTH = 1200
    HEIGHT = 800
    pygame.init()
    self.clock = pygame.time.Clock()
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    self.running = True
    self.hero = pygame.sprite.GroupSingle()
    self.hero.add(Hero())
    self.ground = Ground()

  def run(self):
    while self.running:
      self.check_collisions()
      self.check_events() 
      self.update_screen()

  def check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          self.hero.sprite.y_vel = self.hero.sprite.JUMP_VEL
  
  def check_collisions(self):
    collided = pygame.sprite.spritecollide(self.hero.sprite, self.ground.blocks, False)
    if collided: 
      self.hero.sprite.y_vel = 0
  
  def update_screen(self):
    self.screen.fill((0, 0, 0))
    self.hero.draw(self.screen)
    self.hero.update()
    self.ground.blocks.draw(self.screen)
    pygame.display.flip()
    self.clock.tick(60)

game = Game()
game.run()	
