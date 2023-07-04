import pygame
from hero import Hero
from floor import Floor

class Game:
  def __init__(self):
    pygame.init()
    self.WIDTH = 1280
    self.HEIGHT = 800
    self.clock = pygame.time.Clock()
    self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
    self.running = True
    self.floor = Floor()
    self.hero = pygame.sprite.GroupSingle()
    self.hero.add(Hero())

  def run(self):
    while self.running:
      self.check_events() 
      self.update_screen()

  def check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
  
  def update_screen(self):
    self.floor.render(self.screen)
    self.hero.draw(self.screen)
    self.hero.update()
    pygame.display.flip()
    self.clock.tick(60)

game = Game()
game.run()	
