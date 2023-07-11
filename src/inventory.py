import pygame

class Inventory(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.slot_size = 48
    self.items = pygame.sprite.Group()

    image = pygame.image.load('assets/heroes/knight/weapon_sword_1.png').convert_alpha()
    self.image = pygame.transform.scale(image, (48, 48))

  def render(self, screen):
    pygame.draw.rect(screen, (40, 40, 40), pygame.Rect(345, 700, 48, 48))
    screen.blit(self.image, (345, 700))

    # x pos + (2*i) to get spacing, + 408 to center
    for i in range(8):
      pygame.draw.rect(screen, (40, 40, 40), pygame.Rect(i * self.slot_size + (2*i) + 408, 700, 48, 48))

    for i, item in enumerate(self.items):
      screen.blit(item.image, (i * self.slot_size + (2*i) + 408, 700))
