import pygame
import random
from spritesheet import Spritesheet

class Item(pygame.sprite.Sprite):
  def __init__(self, file, x, y):
    super().__init__()
    self.image = Spritesheet(file)
    self.image = self.image.sprite_at(0, 0, 16, 16)
    self.image = pygame.transform.scale(self.image, (48, 48))
    self.x = x + random.randint(-50, 50)
    self.y = y + 35
    self.rect = self.image.get_rect(midbottom = (self.x, self.y))
