import pygame
from spritesheet import Spritesheet
from random import randint

class Slime(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    # self.font = pygame.font.SysFont('Comic Sans MS', 30)

    idle_sprite_sheet = Spritesheet('assets/enemies/slime/slime_idle_spritesheet.png')
    idle_frame_1 = idle_sprite_sheet.sprite_at(0, 0, 16, 16)
    idle_frame_2 = idle_sprite_sheet.sprite_at(16, 0, 16, 16)
    idle_frame_3 = idle_sprite_sheet.sprite_at(32, 0, 16, 16)
    idle_frame_4 = idle_sprite_sheet.sprite_at(48, 0, 16, 16)
    idle_frame_5 = idle_sprite_sheet.sprite_at(64, 0, 16, 16)
    idle_frame_6 = idle_sprite_sheet.sprite_at(80, 0, 16, 16)
    # Scale idle frames
    idle_frame_1 = pygame.transform.scale(idle_frame_1, (32, 32))
    idle_frame_2 = pygame.transform.scale(idle_frame_2, (32, 32))
    idle_frame_3 = pygame.transform.scale(idle_frame_3, (32, 32))
    idle_frame_4 = pygame.transform.scale(idle_frame_4, (32, 32))
    idle_frame_5 = pygame.transform.scale(idle_frame_5, (32, 32))
    idle_frame_6 = pygame.transform.scale(idle_frame_6, (32, 32))

    self.idle_idx = 0
    self.idle = [idle_frame_1, idle_frame_2, idle_frame_3, idle_frame_4, idle_frame_5, idle_frame_6]

    self.image = self.idle[self.idle_idx]

    random_x_pos = randint(100, 500)
    random_y_pos = randint(100, 500)
    self.rect = self.image.get_rect(midbottom = (random_x_pos, random_y_pos))
  
  def idle_animation(self):
    self.idle_idx += 0.2
    if self.idle_idx >= len(self.idle):
      self.idle_idx = 0
    self.image = self.idle[int(self.idle_idx)]
  
  def update(self):
    self.idle_animation()
