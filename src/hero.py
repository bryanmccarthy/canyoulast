import pygame

class Hero(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    idle_0 = pygame.transform.scale_by(pygame.image.load('assets/heroes/knight/knight_idle_anim_f0.png').convert_alpha(), 4)
    idle_1 = pygame.transform.scale_by(pygame.image.load('assets/heroes/knight/knight_idle_anim_f1.png').convert_alpha(), 4)
    idle_2 = pygame.transform.scale_by(pygame.image.load('assets/heroes/knight/knight_idle_anim_f2.png').convert_alpha(), 4)
    idle_3 = pygame.transform.scale_by(pygame.image.load('assets/heroes/knight/knight_idle_anim_f3.png').convert_alpha(), 4)
    idle_4 = pygame.transform.scale_by(pygame.image.load('assets/heroes/knight/knight_idle_anim_f4.png').convert_alpha(), 4)
    idle_5 = pygame.transform.scale_by(pygame.image.load('assets/heroes/knight/knight_idle_anim_f5.png').convert_alpha(), 4)
    self.hero_idle = [idle_0, idle_1, idle_2, idle_3, idle_4, idle_5]
    self.hero_idle_index = 0
    self.image = self.hero_idle[self.hero_idle_index]
    self.rect = self.image.get_rect(midbottom = (200, 200))
  
  def user_input(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
      self.rect.y -= 6
    if keys[pygame.K_a]:
      self.rect.x -= 6
    if keys[pygame.K_s]:
      self.rect.y += 6
    if keys[pygame.K_d]:
      self.rect.x += 6

  def idle_animation(self):
    self.hero_idle_index += 0.2
    if self.hero_idle_index >= len(self.hero_idle):
      self.hero_idle_index = 0
    self.image = self.hero_idle[int(self.hero_idle_index)]

  def update(self):
    self.user_input()
    self.idle_animation()


