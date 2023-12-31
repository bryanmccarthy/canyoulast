import pygame
from spritesheet import Spritesheet

class Bullet(pygame.sprite.Sprite):
  def __init__(self, player_x, player_y, target_x, target_y, range, vel):
    super().__init__()

    self.player_x = player_x
    self.player_y = player_y
    self.target_x = target_x
    self.target_y = target_y
    self.range = range
    self.vel = vel

    hit_sprite_sheet = Spritesheet('assets/effects/hit_effect_anim_spritesheet.png')
    bullet_sprite = hit_sprite_sheet.sprite_at(0, 0, 8, 8)
    self.bullet = pygame.transform.scale(bullet_sprite, (32, 32))

    self.image = self.bullet
    self.rect = self.image.get_rect(midbottom = (self.player_x, self.player_y))

  def draw(self, screen):
    screen.blit(self.image, self.rect)

  def update(self):
    # move bullet from player pos to mouse pos
    dx = self.target_x - self.player_x
    dy = self.target_y - self.player_y
    dist = (dx ** 2 + dy ** 2) ** 0.5

    if dist != 0:
      dx = dx / dist
      dy = dy / dist

    self.rect.x += dx * self.vel
    self.rect.y += dy * self.vel

    # remove bullet if it goes out of range
    if self.rect.x > self.player_x + self.range or self.rect.x < self.player_x - self.range:
      self.kill()
    if self.rect.y > self.player_y + self.range or self.rect.y < self.player_y - self.range:
      self.kill()