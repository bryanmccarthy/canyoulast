import pygame

class Spritesheet:
  def __init__(self, file):
    self.sprite_sheet = pygame.image.load(file).convert()

  def sprite_at(self, x, y, width, height):
    image = pygame.Surface([width, height]).convert()
    image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
    return image
