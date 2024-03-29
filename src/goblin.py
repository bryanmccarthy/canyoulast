import pygame
from spritesheet import Spritesheet
import random

class Goblin(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()

    self.health = 50
    self.damage = 20
    self.damage_cooldown = 0

    run_sprite_sheet = Spritesheet('assets/enemies/goblin/goblin_run_spritesheet.png')
    run_frame_1 = run_sprite_sheet.sprite_at(0, 0, 16, 16)
    run_frame_2 = run_sprite_sheet.sprite_at(16, 0, 16, 16)
    run_frame_3 = run_sprite_sheet.sprite_at(32, 0, 16, 16)
    run_frame_4 = run_sprite_sheet.sprite_at(48, 0, 16, 16)
    run_frame_5 = run_sprite_sheet.sprite_at(64, 0, 16, 16)
    run_frame_6 = run_sprite_sheet.sprite_at(80, 0, 16, 16)
    # Scale run frames
    run_frame_1 = pygame.transform.scale(run_frame_1, (48, 48))
    run_frame_2 = pygame.transform.scale(run_frame_2, (48, 48))
    run_frame_3 = pygame.transform.scale(run_frame_3, (48, 48))
    run_frame_4 = pygame.transform.scale(run_frame_4, (48, 48))
    run_frame_5 = pygame.transform.scale(run_frame_5, (48, 48))
    run_frame_6 = pygame.transform.scale(run_frame_6, (48, 48))

    self.run_idx = 0
    self.run = [run_frame_1, run_frame_2, run_frame_3, run_frame_4, run_frame_5, run_frame_6]

    self.image = self.run[self.run_idx]

    random_x_pos = random.randint(0, 1280)
    random_y_pos = random.choice([random.randint(-300, 0), random.randint(768, 1068)])
    self.rect = self.image.get_rect(midbottom = (random_x_pos, random_y_pos))

  def run_animation(self):
    self.run_idx += 0.2
    if self.run_idx >= len(self.run):
      self.run_idx = 0
    self.image = self.run[int(self.run_idx)]

  def move_toward_hero(self, hero_x, hero_y):
    if self.rect.x < hero_x + 16:
      self.rect.x += 1
    elif self.rect.x > hero_x + 16:
      self.rect.x -= 1
    
    if self.rect.y < hero_y + 16:
      self.rect.y += 1
    elif self.rect.y > hero_y + 16:
      self.rect.y -= 1

  def hit(self, damage):
    self.health -= damage
    if self.health <= 0:
      self.kill()

  def draw_health(self, screen):
    health_bar_width = 48
    health_bar_height = 5
    health_bar_x = self.rect.x
    health_bar_y = self.rect.y - 1
    health_bar_fill = health_bar_width * (self.health / 50)
    health_bar_outline = pygame.Rect(health_bar_x, health_bar_y, health_bar_width, health_bar_height)
    health_bar_fill = pygame.Rect(health_bar_x, health_bar_y, health_bar_fill, health_bar_height)
    pygame.draw.rect(screen, (255, 0, 0), health_bar_outline)
    pygame.draw.rect(screen, (0, 255, 0), health_bar_fill)
  
  def update(self, hero_x, hero_y, screen):
    self.move_toward_hero(hero_x, hero_y)
    self.run_animation()
    self.draw_health(screen)
