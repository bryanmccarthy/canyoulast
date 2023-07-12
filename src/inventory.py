import pygame

class Inventory(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.slot_size = 48
    self.items = pygame.sprite.Group()

    image = pygame.image.load('assets/heroes/knight/weapon_sword_1.png').convert_alpha()
    self.image = pygame.transform.scale(image, (48, 48))

    self.slot_positions = [
      (400, 700),
      (449, 700),
      (498, 700),
      (547, 700),
      (596, 700),
      (645, 700),
      (694, 700),
      (743, 700)
    ]
  
  def place_item(self, item):
    item.rect.topleft = self.slot_positions[len(self.items) - 1]

  def use_slot(self, slot):
    # TODO: Match slot num to pos (rect) and check item sprite collison with that slot rect
    pass

  def render(self, screen):
    pygame.draw.rect(screen, (40, 40, 40), pygame.Rect(345, 700, 48, 48))
    screen.blit(self.image, (345, 700))

    # Slot backgrounds
    for i in range(8):
      pygame.draw.rect(screen, (40, 40, 40), pygame.Rect(self.slot_positions[i][0], self.slot_positions[i][1], 48, 48))
    
    self.items.draw(screen)
