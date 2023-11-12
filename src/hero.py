import pygame
from spritesheet import Spritesheet
from inventory import Inventory
from world import World

class Hero(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.font = pygame.font.SysFont('Comic Sans MS', 30)

    idle_sprite_sheet = Spritesheet('assets/heroes/knight/knight_idle_spritesheet.png')
    idle_frame_1 = idle_sprite_sheet.sprite_at(0, 0, 16, 16)
    idle_frame_2 = idle_sprite_sheet.sprite_at(16, 0, 16, 16)
    idle_frame_3 = idle_sprite_sheet.sprite_at(32, 0, 16, 16)
    idle_frame_4 = idle_sprite_sheet.sprite_at(48, 0, 16, 16)
    idle_frame_5 = idle_sprite_sheet.sprite_at(64, 0, 16, 16)
    idle_frame_6 = idle_sprite_sheet.sprite_at(80, 0, 16, 16)
    # Scale idle frames
    idle_frame_1 = pygame.transform.scale(idle_frame_1, (64, 64))
    idle_frame_2 = pygame.transform.scale(idle_frame_2, (64, 64))
    idle_frame_3 = pygame.transform.scale(idle_frame_3, (64, 64))
    idle_frame_4 = pygame.transform.scale(idle_frame_4, (64, 64))
    idle_frame_5 = pygame.transform.scale(idle_frame_5, (64, 64))
    idle_frame_6 = pygame.transform.scale(idle_frame_6, (64, 64))

    run_sprite_sheet = Spritesheet('assets/heroes/knight/knight_run_spritesheet.png')
    run_frame_1 = run_sprite_sheet.sprite_at(0, 0, 16, 16)
    run_frame_2 = run_sprite_sheet.sprite_at(16, 0, 16, 16)
    run_frame_3 = run_sprite_sheet.sprite_at(32, 0, 16, 16)
    run_frame_4 = run_sprite_sheet.sprite_at(48, 0, 16, 16)
    run_frame_5 = run_sprite_sheet.sprite_at(64, 0, 16, 16)
    run_frame_6 = run_sprite_sheet.sprite_at(80, 0, 16, 16)
    # Scale idle frames
    run_frame_1 = pygame.transform.scale(run_frame_1, (64, 64))
    run_frame_2 = pygame.transform.scale(run_frame_2, (64, 64))
    run_frame_3 = pygame.transform.scale(run_frame_3, (64, 64))
    run_frame_4 = pygame.transform.scale(run_frame_4, (64, 64))
    run_frame_5 = pygame.transform.scale(run_frame_5, (64, 64))
    run_frame_6 = pygame.transform.scale(run_frame_6, (64, 64))

    attack_sprite_sheet = Spritesheet('assets/effects/slash_effect_anim_spritesheet.png')
    attack_frame_1 = attack_sprite_sheet.sprite_at(0, 0, 16, 16)
    attack_frame_2 = attack_sprite_sheet.sprite_at(16, 0, 16, 16)
    attack_frame_3 = attack_sprite_sheet.sprite_at(32, 0, 16, 16)
    # Scale attack frames
    attack_frame_1 = pygame.transform.scale(attack_frame_1, (32, 32))
    attack_frame_2 = pygame.transform.scale(attack_frame_2, (32, 32))
    attack_frame_3 = pygame.transform.scale(attack_frame_3, (32, 32))

    self.attack_idx = 0
    self.attack = [attack_frame_1, attack_frame_2, attack_frame_3]
    self.attacking = False

    # Stats
    self.speed = 5
    self.strength = 5
    self.healing = 5

    # Stat caps
    self.max_speed = 8
    self.max_strength = 8
    self.max_healing = 8

    self.health = 100
    self.direction = 'R'

    self.idle_idx = 0
    self.idle = [idle_frame_1, idle_frame_2, idle_frame_3, idle_frame_4, idle_frame_5, idle_frame_6]

    self.run_idx = 0
    self.run = [run_frame_1, run_frame_2, run_frame_3, run_frame_4, run_frame_5, run_frame_6]

    self.inventory = Inventory()
    self.world = World()

    self.image = self.idle[self.idle_idx]
    self.rect = self.image.get_rect(midbottom = (640, 384))
  
  def user_input(self, keys):
    if keys[pygame.K_ESCAPE]:
      # TODO: Add pause menu
      pygame.quit()
      quit()

    if keys[pygame.K_w]:
      self.world.shift_world('u')

    if keys[pygame.K_a]:
      if self.direction == 'R': self.flip_images()
      self.direction = 'L'
      self.world.shift_world('l')

    if keys[pygame.K_s]:
      self.world.shift_world('d')

    if keys[pygame.K_d]:
      if self.direction == 'L': self.flip_images()
      self.direction = 'R'
      self.world.shift_world('r')

    if keys[pygame.K_1]:
      self.inventory.use_slot(1, self)
    if keys[pygame.K_2]:
      self.inventory.use_slot(2, self)
    if keys[pygame.K_3]:
      self.inventory.use_slot(3, self)
    if keys[pygame.K_4]:
      self.inventory.use_slot(4, self)
    if keys[pygame.K_5]:
      self.inventory.use_slot(5, self)
    if keys[pygame.K_6]:
      self.inventory.use_slot(6, self)
    if keys[pygame.K_7]:
      self.inventory.use_slot(7, self)
    if keys[pygame.K_8]:
      self.inventory.use_slot(8, self)
  
  def flip_images(self):
    for i in range(len(self.idle)):
      self.idle[i] = pygame.transform.flip(self.idle[i], True, False)
    for i in range(len(self.run)):
      self.run[i] = pygame.transform.flip(self.run[i], True, False)
    for i in range(len(self.attack)):
      self.attack[i] = pygame.transform.flip(self.attack[i], True, False)

  def idle_animation(self):
    self.idle_idx += 0.2
    if self.idle_idx >= len(self.idle):
      self.idle_idx = 0
    self.image = self.idle[int(self.idle_idx)]

  def run_animation(self):
    self.run_idx += 0.2
    if self.run_idx >= len(self.run):
      self.run_idx = 0
    self.image = self.run[int(self.run_idx)]
  
  def attack_animation(self, screen):
    self.attack_idx += 0.2
    if self.attack_idx >= len(self.attack):
      self.attack_idx = 0
    if self.direction == 'R':
      screen.blit(self.attack[int(self.attack_idx)], (self.rect.x + 55 + (2 * self.attack_idx), self.rect.y + 16))
    else:
      screen.blit(self.attack[int(self.attack_idx)], (self.rect.x - 25 - (2 * self.attack_idx), self.rect.y + 16))

  def draw_health(self, screen):
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(590, 660, 100, 25))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(590, 660, self.health, 25))
    health = pygame.transform.scale_by(self.font.render(f'{self.health}', False, (0, 0, 0)), 0.7)
    screen.blit(health, (623, 656))
  
  def draw_stats(self, screen):
    display_speed = int(((self.speed % 5) / 0.2) + 5)
    display_strength = int(((self.strength % 5) / 0.2) + 5)
    display_healing = int(((self.healing % 5) / 0.2) + 5)

    speed_text = pygame.transform.scale_by(self.font.render(f"spd {display_speed}", False, (200, 255, 255)), 0.8)
    screen.blit(speed_text, (840, 700))
    strength_text = pygame.transform.scale_by(self.font.render(f"atk {display_strength}", False, (200, 255, 255)), 0.8)
    screen.blit(strength_text, (920, 700))
    healing_text = pygame.transform.scale_by(self.font.render(f"vit {display_healing}", False, (200, 255, 255)), 0.8)
    screen.blit(healing_text, (1000, 700))

  def update(self, screen):
    keys = pygame.key.get_pressed()
    self.user_input(keys)
    if not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_w] and not keys[pygame.K_s]:
      self.idle_animation()
      if self.attacking: self.attack_animation(screen)
    else:
      self.run_animation()
      if self.attacking: self.attack_animation(screen)
      
    self.draw_health(screen)
    self.draw_stats(screen)
