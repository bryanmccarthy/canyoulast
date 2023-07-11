import random
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
  
  def open_chest(self, chest):
    chest.open = True
  
  def check_open_chests(self):
    for chest in self.chest_group:
      if chest.open:
        chest.items.draw(self.screen)
    
  def pick_up_item(self, item, chest):
    if not chest.open: return
    self.hero.sprite.inventory.items.add(item)
    chest.items.remove(item)
  
  def handle_interactions(self):
    for chest in self.chest_group:
      collided_items = pygame.sprite.spritecollide(self.hero.sprite, chest.items, False)
      if collided_items:
        self.pick_up_item(collided_items[0], chest)

    collided_chests = pygame.sprite.spritecollide(self.hero.sprite, self.chest_group, False) 
    if collided_chests: self.open_chest(collided_chests[0])
        
  def check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_e:
          self.handle_interactions()

  def update_screen(self):
    self.world.render(self.screen)
    self.chest_group.draw(self.screen)
    self.chest_group.update()
    self.check_open_chests()
    self.hero.draw(self.screen)
    self.hero.update()
    self.hero.sprite.inventory.render(self.screen)
    pygame.display.flip()
    self.clock.tick(60)

game = Game()
game.run()	
