import pygame

class Inventory(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.slot_size = 48
    self.items = pygame.sprite.Group()

    self.font = pygame.font.SysFont('Comic Sans MS', 30)

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
  
  def draw_text(self, text, screen, x, y):
    text = self.font.render(text, False, (0, 0, 0))
    screen.blit(text, (x, y))
  
  def draw_item(self, item):
    item.rect.topleft = self.slot_positions[len(self.items) - 1]

  def use_slot(self, slot, hero):
    for item in self.items:
      if item.rect.topleft == self.slot_positions[slot - 1]:
        if item.name == 'potion_green' and hero.speed < 8: 
          hero.speed += 1
          self.items.remove(item)
        elif item.name == 'potion_red' and hero.strength < 10: 
          hero.strength += 1
          self.items.remove(item)
        elif item.name == 'potion_yellow' and hero.healing < 10: 
          hero.healing += 1
          self.items.remove(item)

  def render(self, screen):
    # Slot backgrounds
    for i in range(8):
      pygame.draw.rect(screen, (60, 60, 60), pygame.Rect(self.slot_positions[i][0], self.slot_positions[i][1], 48, 48))
      self.draw_text(f'{i + 1}', screen, self.slot_positions[i][0] + 15, self.slot_positions[i][1])

      # Slots containing an item shouldn't render number
      for item in self.items:
        if item.rect.topleft == self.slot_positions[i]:
          pygame.draw.rect(screen, (60, 60, 60), pygame.Rect(self.slot_positions[i][0], self.slot_positions[i][1], 48, 48))
    
    self.items.draw(screen)
