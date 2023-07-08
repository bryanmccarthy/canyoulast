import pygame
from hero import Hero
from world import World 

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
    self.world = World()

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
    pass

  def update_screen(self):
    self.screen.fill((0, 0, 0))
    self.world.render(self.screen)
    self.hero.draw(self.screen)
    self.hero.update()
    pygame.display.flip()
    self.clock.tick(60)

game = Game()
game.run()	
