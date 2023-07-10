import pygame
from spritesheet import Spritesheet

class Hero(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    idle_sprite_sheet = Spritesheet('assets/heroes/knight/knight_idle_spritesheet.png')
    idle_frame_1 = idle_sprite_sheet.sprite_at(0, 0, 16, 16)
    idle_frame_2 = idle_sprite_sheet.sprite_at(16, 0, 16, 16)
    idle_frame_3 = idle_sprite_sheet.sprite_at(32, 0, 16, 16)
    idle_frame_4 = idle_sprite_sheet.sprite_at(48, 0, 16, 16)
    idle_frame_5 = idle_sprite_sheet.sprite_at(64, 0, 16, 16)
    idle_frame_6 = idle_sprite_sheet.sprite_at(80, 0, 16, 16)
    # scale idle frames
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
    # scale idle frames
    run_frame_1 = pygame.transform.scale(run_frame_1, (64, 64))
    run_frame_2 = pygame.transform.scale(run_frame_2, (64, 64))
    run_frame_3 = pygame.transform.scale(run_frame_3, (64, 64))
    run_frame_4 = pygame.transform.scale(run_frame_4, (64, 64))
    run_frame_5 = pygame.transform.scale(run_frame_5, (64, 64))
    run_frame_6 = pygame.transform.scale(run_frame_6, (64, 64))

    self.direction = 'R'

    self.idle_idx = 0
    self.idle = [idle_frame_1, idle_frame_2, idle_frame_3, idle_frame_4, idle_frame_5, idle_frame_6]

    self.run_idx = 0
    self.run = [run_frame_1, run_frame_2, run_frame_3, run_frame_4, run_frame_5, run_frame_6]

    self.items = []

    self.image = self.idle[self.idle_idx]
    self.rect = self.image.get_rect(midbottom = (100, 700))
  
  def user_input(self, keys):
    if keys[pygame.K_w]:
      if self.rect.y > 0: self.rect.y -= 6
    if keys[pygame.K_a]:
      if self.direction == 'R': self.flip_images()
      if self.rect.x > 0: self.rect.x -= 6
      self.direction = 'L'
    if keys[pygame.K_s]:
      if self.rect.y < 700: self.rect.y += 6
    if keys[pygame.K_d]:
      if self.direction == 'L': self.flip_images()
      if self.rect.x < 1220: self.rect.x += 6
      self.direction = 'R'
  
  def flip_images(self):
    for i in range(len(self.idle)):
      self.idle[i] = pygame.transform.flip(self.idle[i], True, False)
    for i in range(len(self.run)):
      self.run[i] = pygame.transform.flip(self.run[i], True, False)

  def idle_animation(self):
    # TODO: invert when running left
    self.idle_idx += 0.2
    if self.idle_idx >= len(self.idle):
      self.idle_idx = 0
    self.image = self.idle[int(self.idle_idx)]

  def run_animation(self):
    # TODO: invert when running left
    self.run_idx += 0.2
    if self.run_idx >= len(self.run):
      self.run_idx = 0
    self.image = self.run[int(self.run_idx)]

  def update(self):
    keys = pygame.key.get_pressed()
    self.user_input(keys)
    if not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_w] and not keys[pygame.K_s]:
      self.idle_animation()
    else:
      self.run_animation()
