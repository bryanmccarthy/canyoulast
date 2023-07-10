import pygame
from hero import Hero
from world import World
from chest import Chest

class Game:
  def __init__(self):
    WIDTH = 1280
    HEIGHT = 768
    pygame.init()
    self.clock = pygame.time.Clock()
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    self.running = True
    self.hero = pygame.sprite.GroupSingle(Hero())
    self.world = World()
    self.chest_group = pygame.sprite.Group(Chest(100,100), Chest(450,350), Chest(1100, 200), Chest(800, 700))

  def run(self):
    while self.running:
      self.check_events() 
      self.update_screen()
  
  def check_chest_collisions(self):
    collided_chests = pygame.sprite.spritecollide(self.hero.sprite, self.chest_group, False)
    for chest in collided_chests:
      chest.open = True
  
  def check_open_chests(self):
    for chest in self.chest_group:
      if chest.open == True:
        chest.items.draw(self.screen)

  def check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          self.check_chest_collisions()

  def update_screen(self):
    self.world.render(self.screen)
    self.chest_group.draw(self.screen)
    self.chest_group.update()
    self.check_open_chests()
    self.hero.draw(self.screen)
    self.hero.update()
    pygame.display.flip()
    self.clock.tick(60)

game = Game()
game.run()	
