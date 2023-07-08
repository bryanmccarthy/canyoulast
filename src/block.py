import pygame
from spritesheet import Spritesheet

class Block():
  def __init__(self, width, height, file):
    block_sprite = Spritesheet(file) # file must be single block
    self.image = block_sprite.sprite_at(0, 0, width, height)
    self.image = pygame.transform.scale(self.image, (64, 64))
