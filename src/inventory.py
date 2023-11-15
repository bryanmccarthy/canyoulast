import pygame
from item import Item

class Inventory(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.slot_size = 48
    self.items = pygame.sprite.Group()
    self.weapon = pygame.sprite.GroupSingle()

    iron_sword_image = pygame.image.load('assets/heroes/knight/iron_sword.png')
    iron_sword = Item(iron_sword_image, 'weapon', 0, 0)
    self.weapon.add(iron_sword)
    self.weapon.sprite.rect.topleft = (380, 700)

    self.font = pygame.font.SysFont('Comic Sans MS', 30)

    self.weapon_slot_position = (380, 700)
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
        if item.name == 'potion_green' and hero.speed < hero.speed_cap: 
          hero.speed += 0.2
          self.items.remove(item)
        elif item.name == 'potion_red' and hero.strength < hero.strength_cap: 
          hero.strength += 0.2
          self.items.remove(item)
        elif item.name == 'potion_yellow' and hero.healing < hero.healing_cap: 
          hero.healing += 0.2
          self.items.remove(item)
        elif item.name == 'weapon':
          # Swap weapon
          curr_weapon = self.weapon.sprite
          if curr_weapon: curr_weapon.rect.topleft = self.slot_positions[slot - 1]
          self.weapon.empty()
          self.weapon.add(item)
          self.items.remove(item)
          if curr_weapon: self.items.add(curr_weapon)
          self.weapon.sprite.rect.topleft = self.weapon_slot_position

  def render(self, screen):
    # Draw weapon slot
    pygame.draw.rect(screen, (60, 60, 60), pygame.Rect(self.weapon_slot_position[0], self.weapon_slot_position[1], 48, 48))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.weapon_slot_position[0], self.weapon_slot_position[1], 48, 48), 2)
    self.weapon.draw(screen)

    # Slot backgrounds
    for i in range(8):
      pygame.draw.rect(screen, (60, 60, 60), pygame.Rect(self.slot_positions[i][0], self.slot_positions[i][1], 48, 48))
      self.draw_text(f'{i + 1}', screen, self.slot_positions[i][0] + 15, self.slot_positions[i][1])

      # Slots containing an item shouldn't render number
      for item in self.items:
        if item.rect.topleft == self.slot_positions[i]:
          pygame.draw.rect(screen, (60, 60, 60), pygame.Rect(self.slot_positions[i][0], self.slot_positions[i][1], 48, 48))

      # Slot borders
      pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.slot_positions[i][0], self.slot_positions[i][1], 48, 48), 2)
    
    self.items.draw(screen)
