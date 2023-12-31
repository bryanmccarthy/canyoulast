import pygame
import random
from spritesheet import Spritesheet
from item import Item

class Chest(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.font = pygame.font.SysFont('Comic Sans MS', 20)

    chest_closed_sprite_sheet = Spritesheet('assets/props_itens/chest_spritesheet.png')
    chest_closed_frame_1 = chest_closed_sprite_sheet.sprite_at(0, 0, 16, 16)
    chest_closed_frame_2 = chest_closed_sprite_sheet.sprite_at(16, 0, 16, 16)
    chest_closed_frame_3 = chest_closed_sprite_sheet.sprite_at(32, 0, 16, 16)
    chest_closed_frame_4 = chest_closed_sprite_sheet.sprite_at(48, 0, 16, 16)
    chest_closed_frame_5 = chest_closed_sprite_sheet.sprite_at(64, 0, 16, 16)
    chest_closed_frame_6 = chest_closed_sprite_sheet.sprite_at(80, 0, 16, 16)
    chest_closed_frame_7 = chest_closed_sprite_sheet.sprite_at(96, 0, 16, 16)
    chest_closed_frame_8 = chest_closed_sprite_sheet.sprite_at(112, 0, 16, 16)

    chest_closed_frame_1 = pygame.transform.scale(chest_closed_frame_1, (48, 48))
    chest_closed_frame_2 = pygame.transform.scale(chest_closed_frame_2, (48, 48))
    chest_closed_frame_3 = pygame.transform.scale(chest_closed_frame_3, (48, 48))
    chest_closed_frame_4 = pygame.transform.scale(chest_closed_frame_4, (48, 48))
    chest_closed_frame_5 = pygame.transform.scale(chest_closed_frame_5, (48, 48))
    chest_closed_frame_6 = pygame.transform.scale(chest_closed_frame_6, (48, 48))
    chest_closed_frame_7 = pygame.transform.scale(chest_closed_frame_7, (48, 48))
    chest_closed_frame_8 = pygame.transform.scale(chest_closed_frame_8, (48, 48))

    chest_open_sprite_sheet = Spritesheet('assets/props_itens/chest_open.png')
    chest_open = chest_open_sprite_sheet.sprite_at(0, 0, 16, 16)
    self.chest_open = pygame.transform.scale(chest_open, (48, 48))

    self.open = False
    self.closed_idx = 0
    self.closed = [chest_closed_frame_1, chest_closed_frame_2, chest_closed_frame_3, chest_closed_frame_4, chest_closed_frame_5, chest_closed_frame_6, chest_closed_frame_7, chest_closed_frame_8]

    self.x = x
    self.y = y

    potion_green = pygame.image.load('assets/props_itens/potion_green.png')
    potion_red = pygame.image.load('assets/props_itens/potion_red.png')
    potion_yellow = pygame.image.load('assets/props_itens/potion_yellow.png')

    potion_green = pygame.transform.scale(potion_green, (32, 32))
    potion_red = pygame.transform.scale(potion_red, (32, 32))
    potion_yellow = pygame.transform.scale(potion_yellow, (32, 32))

    swords_sprite_sheet = Spritesheet('assets/swords_spritesheet.png')
    fire_sword = swords_sprite_sheet.sprite_at(0, 0, 32, 32)
    ice_sword = swords_sprite_sheet.sprite_at(32, 0, 32, 32)
    earth_sword = swords_sprite_sheet.sprite_at(64, 0, 32, 32)

    potions = [('potion_green', potion_green), ('potion_red', potion_red), ('potion_yellow', potion_yellow)]
    swords = [('weapon', fire_sword), ('weapon', ice_sword), ('weapon', earth_sword)]
    self.items = pygame.sprite.Group()

    # Add a random amount of random potions to the chest
    for _ in range(random.randrange(3, 5)):
      random_idx = random.randrange(0, 3)
      self.items.add(Item(potions[random_idx][1], potions[random_idx][0], self.x, self.y))

    # Add a random sword to the chest
    random_idx = random.randrange(0, 3)
    self.items.add(Item(swords[random_idx][1], swords[random_idx][0], self.x, self.y))

    self.image = self.closed[self.closed_idx]
    self.rect = self.image.get_rect(midbottom = (self.x, self.y))

  def closed_animation(self):
    self.closed_idx += 0.2
    if self.closed_idx >= 0:
      if self.closed_idx >= len(self.closed):
        self.closed_idx = -8 # Hack
      self.image = self.closed[int(self.closed_idx)]

  def draw_open_keybind(self, screen):
    keybind = self.font.render('<e>', False, (255, 255, 255))
    screen.blit(keybind, (self.rect.x + 12, self.rect.y - 30))

  def update(self, screen):
    if self.open:
      self.image = self.chest_open
    else:
      self.closed_animation()
      self.draw_open_keybind(screen)