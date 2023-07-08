import pygame
from hero import Hero
from block import Block

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
    self.block = pygame.sprite.GroupSingle()
    self.block.add(Block(200, 400, 'assets/tiles/floor/floor_1.png'))

  def run(self):
    while self.running:
      self.check_events() 
      self.update_screen()

  def check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
  
  def update_screen(self):
    self.hero.draw(self.screen)
    self.hero.update()
    self.block.draw(self.screen)
    pygame.display.flip()
    self.clock.tick(60)

game = Game()
game.run()	
