import pygame
from spritesheet import Spritesheet

class Block(pygame.sprite.Sprite):
  def __init__(self, x, y, file):
    super().__init__()
    WIDTH = 16
    HEIGHT = 16
    block_sprite = Spritesheet(file) # file must be single block
    self.image = block_sprite.sprite_at(0, 0, 16, 16)
    self.rect = self.image.get_rect(midbottom = (x, y))
