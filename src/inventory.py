import pygame

class Inventory(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.slot_size = 32
    self.items = pygame.sprite.Group()

  def render(self, screen):
    for i, item in enumerate(self.items):
      screen.blit(item.image, (i * self.slot_size, 720))
