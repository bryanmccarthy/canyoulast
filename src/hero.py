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
    idle_frame_1 = pygame.transform.scale_by(idle_frame_1, 4)
    idle_frame_2 = pygame.transform.scale_by(idle_frame_2, 4)
    idle_frame_3 = pygame.transform.scale_by(idle_frame_3, 4)
    idle_frame_4 = pygame.transform.scale_by(idle_frame_4, 4)
    idle_frame_5 = pygame.transform.scale_by(idle_frame_5, 4)
    idle_frame_6 = pygame.transform.scale_by(idle_frame_6, 4)

    run_sprite_sheet = Spritesheet('assets/heroes/knight/knight_run_spritesheet.png')
    run_frame_1 = run_sprite_sheet.sprite_at(0, 0, 16, 16)
    run_frame_2 = run_sprite_sheet.sprite_at(16, 0, 16, 16)
    run_frame_3 = run_sprite_sheet.sprite_at(32, 0, 16, 16)
    run_frame_4 = run_sprite_sheet.sprite_at(48, 0, 16, 16)
    run_frame_5 = run_sprite_sheet.sprite_at(64, 0, 16, 16)
    run_frame_6 = run_sprite_sheet.sprite_at(80, 0, 16, 16)
    # scale idle frames
    run_frame_1 = pygame.transform.scale_by(run_frame_1, 4)
    run_frame_2 = pygame.transform.scale_by(run_frame_2, 4)
    run_frame_3 = pygame.transform.scale_by(run_frame_3, 4)
    run_frame_4 = pygame.transform.scale_by(run_frame_4, 4)
    run_frame_5 = pygame.transform.scale_by(run_frame_5, 4)
    run_frame_6 = pygame.transform.scale_by(run_frame_6, 4)

    self.idle_idx = 0
    self.idle = [idle_frame_1, idle_frame_2, idle_frame_3, idle_frame_4, idle_frame_5, idle_frame_6]

    self.run_idx = 0
    self.run = [run_frame_1, run_frame_2, run_frame_3, run_frame_4, run_frame_5, run_frame_6]

    self.image = self.idle[self.idle_idx]
    self.rect = self.image.get_rect(midbottom = (200, 200))
  
  def user_input(self, keys):
    if keys[pygame.K_w]:
      self.rect.y -= 6
    if keys[pygame.K_a]:
      self.rect.x -= 6
    if keys[pygame.K_s]:
      self.rect.y += 6
    if keys[pygame.K_d]:
      self.rect.x += 6

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

  def update(self):
    keys = pygame.key.get_pressed()
    self.user_input(keys)
    if not keys[pygame.K_w] and not keys[pygame.K_a] and not keys[pygame.K_s] and not keys[pygame.K_d]:
      self.idle_animation()
    else:
      self.run_animation()


