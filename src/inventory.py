import pygame

class Inventory(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.slot_size = 48
    self.items = pygame.sprite.Group()

  def render(self, screen):
    # x pos + (2*i) to get spacing, + 408 to center
    for i in range(8):
      pygame.draw.rect(screen, (40, 40, 40), pygame.Rect(i * self.slot_size + (2*i) + 408, 700, 48, 48))

    for i, item in enumerate(self.items):
      screen.blit(item.image, (i * self.slot_size + (2*i) + 408, 700))
