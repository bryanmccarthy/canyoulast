import random
import pygame
from hero import Hero
from slime import Slime
from world import World
from chest import Chest

class Game:
  def __init__(self):
    WIDTH = 1280
    HEIGHT = 768
    pygame.init()
    pygame.font.init()
    self.font = pygame.font.SysFont('Comic Sans MS', 30)
    self.clock = pygame.time.Clock()
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    self.running = True
    self.in_menu = True
    self.in_pause_menu = False
    self.hero = pygame.sprite.GroupSingle(Hero())
    self.enemies = pygame.sprite.Group()
    self.world = World()
    self.chest_group = pygame.sprite.Group(Chest(100,100), Chest(300,100), Chest(500, 100), Chest(700, 100), Chest(900, 100))

    for _ in range(5):
      self.enemies.add(Slime())

  def run(self):
    while self.running:
      self.update_screen()
      self.check_events()
  
  def draw_pause_menu(self):
    self.screen.fill((0, 0, 0))
    title = self.font.render("PAUSED", False, (200, 255, 255))
    self.screen.blit(title, (560, 100))

    resume = self.font.render("ESC to resume", False, (200, 255, 255))
    self.screen.blit(resume, (535, 350))

    quit = self.font.render("Q to quit", False, (200, 255, 255))
    self.screen.blit(quit, (560, 400))
  
  def open_chest(self, chest):
    chest.open = True
  
  def check_open_chests(self):
    for chest in self.chest_group:
      if chest.open:
        chest.items.draw(self.screen)
    
  def pick_up_item(self, item, chest):
    if len(self.hero.sprite.inventory.items) == 8: return
    self.hero.sprite.inventory.items.add(item)
    self.hero.sprite.inventory.draw_item(item)
    chest.items.remove(item)
  
  def handle_interactions(self):
    for chest in self.chest_group:
      if chest.open:
        collided_items = pygame.sprite.spritecollide(self.hero.sprite, chest.items, False)
        if collided_items:
          self.pick_up_item(collided_items[0], chest)

    collided_chests = pygame.sprite.spritecollide(self.hero.sprite, self.chest_group, False) 
    if collided_chests: self.open_chest(collided_chests[0])
  
  def attack(self, bool):
    self.hero.sprite.attacking = bool
  
  def draw_menu(self):
    self.screen.fill((0, 0, 0))
    title = self.font.render("can you last", False, (200, 255, 255))
    self.screen.blit(title, (560, 100))

    start = self.font.render("SPACE to start", False, (200, 255, 255))
    self.screen.blit(start, (535, 350))
        
  def check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_e:
          self.handle_interactions()
        if event.key == pygame.K_SPACE and self.in_menu:
          self.in_menu = False
        if event.key == pygame.K_ESCAPE:
          self.in_pause_menu = not self.in_pause_menu
        if event.key == pygame.K_q and self.in_pause_menu:
          pygame.quit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        self.attack(True)
      if event.type == pygame.MOUSEBUTTONUP:
        self.attack(False)

  def update_screen(self):
    if self.in_menu:
      self.draw_menu()
    elif self.in_pause_menu:
      self.draw_pause_menu()
    else:
      self.world.render(self.screen)
      self.chest_group.draw(self.screen)
      self.chest_group.update()
      self.check_open_chests()
      self.hero.draw(self.screen)
      self.hero.update(self.screen)
      self.hero.sprite.inventory.render(self.screen)
      self.enemies.draw(self.screen)
      self.enemies.update()

    pygame.display.flip()
    self.clock.tick(60)

game = Game()
game.run()	
