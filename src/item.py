import pygame
import random
from spritesheet import Spritesheet

class Item(pygame.sprite.Sprite):
  def __init__(self, image, name, x, y):
    super().__init__()
    self.image = image
    self.image = pygame.transform.scale(self.image, (48, 48))
    self.name = name
    self.x = x + random.randint(-50, 50)
    self.y = y + 35
    self.rect = self.image.get_rect(midbottom = (self.x, self.y))
