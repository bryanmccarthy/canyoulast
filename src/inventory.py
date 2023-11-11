import pygame

class Inventory(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.slot_size = 48
    self.items = pygame.sprite.Group()

    self.font = pygame.font.SysFont('Comic Sans MS', 30)

    self.slot_positions = [
      (448, 700),
      (496, 700),
      (544, 700),
      (592, 700),
      (640, 700),
      (688, 700),
      (736, 700),
      (784, 700)
    ]
  
  def draw_text(self, text, screen, x, y):
    text = self.font.render(text, False, (0, 0, 0))
    screen.blit(text, (x, y))
  
  def draw_item(self, item):
    for slot_pos in self.slot_positions:
      used = False
      for item in self.items:
        if item.rect.topleft == slot_pos:
          used = True
      if not used:
        item.rect.topleft = slot_pos
        break

  def use_slot(self, slot, hero):
    for item in self.items:
      if item.rect.topleft == self.slot_positions[slot - 1]:
        if item.name == 'potion_green' and hero.speed < hero.max_speed: 
          hero.speed += 0.2
          self.items.remove(item)
        elif item.name == 'potion_red' and hero.strength < hero.max_strength: 
          hero.strength += 0.2
          self.items.remove(item)
        elif item.name == 'potion_yellow' and hero.healing < hero.max_healing: 
          hero.healing += 0.2
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

      # Line breaks
      if i != 0: pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.slot_positions[i][0], self.slot_positions[i][1], 2, 48))
    
    self.items.draw(screen)
