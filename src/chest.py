import pygame
from spritesheet import Spritesheet

class Chest(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    chest_closed_sprite_sheet = Spritesheet('assets/props_itens/chest_spritesheet.png')
    chest_closed_frame_1 = chest_closed_sprite_sheet.sprite_at(0, 0, 16, 16)
    chest_closed_frame_2 = chest_closed_sprite_sheet.sprite_at(16, 0, 16, 16)
    chest_closed_frame_3 = chest_closed_sprite_sheet.sprite_at(32, 0, 16, 16)
    chest_closed_frame_4 = chest_closed_sprite_sheet.sprite_at(48, 0, 16, 16)
    chest_closed_frame_5 = chest_closed_sprite_sheet.sprite_at(64, 0, 16, 16)
    chest_closed_frame_6 = chest_closed_sprite_sheet.sprite_at(80, 0, 16, 16)
    chest_closed_frame_7 = chest_closed_sprite_sheet.sprite_at(96, 0, 16, 16)
    chest_closed_frame_8 = chest_closed_sprite_sheet.sprite_at(112, 0, 16, 16)

    chest_closed_frame_1 = pygame.transform.scale(chest_closed_frame_1, (32, 32))
    chest_closed_frame_2 = pygame.transform.scale(chest_closed_frame_2, (32, 32))
    chest_closed_frame_3 = pygame.transform.scale(chest_closed_frame_3, (32, 32))
    chest_closed_frame_4 = pygame.transform.scale(chest_closed_frame_4, (32, 32))
    chest_closed_frame_5 = pygame.transform.scale(chest_closed_frame_5, (32, 32))
    chest_closed_frame_6 = pygame.transform.scale(chest_closed_frame_6, (32, 32))
    chest_closed_frame_7 = pygame.transform.scale(chest_closed_frame_7, (32, 32))
    chest_closed_frame_8 = pygame.transform.scale(chest_closed_frame_8, (32, 32))

    chest_open_sprite_sheet = Spritesheet('assets/props_itens/chest_open.png')
    chest_open = chest_open_sprite_sheet.sprite_at(0, 0, 16, 16)
    self.chest_open = pygame.transform.scale(chest_open, (32, 32))

    self.open = False
    self.closed_idx = 0
    self.closed = [chest_closed_frame_1, chest_closed_frame_2, chest_closed_frame_3, chest_closed_frame_4, chest_closed_frame_5, chest_closed_frame_6, chest_closed_frame_7, chest_closed_frame_8]
    self.image = self.closed[self.closed_idx]
    self.rect = self.image.get_rect(midbottom = (x, y))

  def closed_animation(self):
    self.closed_idx += 0.2
    if self.closed_idx >= 0:
      if self.closed_idx >= len(self.closed):
        self.closed_idx = -8 # Hack
      self.image = self.closed[int(self.closed_idx)]

  def update(self):
    if self.open:
      self.image = self.chest_open
    else:
      self.closed_animation()