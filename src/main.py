import random
import pygame
from hero import Hero
from slime import Slime
from world import World
from chest import Chest
from bullet import Bullet
from spritesheet import Spritesheet

class Game:
  def __init__(self):
    WIDTH = 1280
    HEIGHT = 768
    self.PLAYER_SHOOT_COOLDOWN = 8
    pygame.init()
    pygame.font.init()
    self.font = pygame.font.SysFont('Comic Sans MS', 30)
    self.clock = pygame.time.Clock()
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    self.running = True
    self.player_shooting = False
    self.player_shoot_cooldown = 0
    self.in_menu = True
    self.in_pause_menu = False
    self.wave = 1
    self.hero = pygame.sprite.GroupSingle(Hero())
    self.enemies = pygame.sprite.Group()
    self.world = World()
    self.chest_group = pygame.sprite.Group()
    self.chest_group.add(Chest(640, 200))

    for _ in range(5):
      self.enemies.add(Slime())
    
    self.bullets = pygame.sprite.Group()

    # Hit effect animation
    hit_sprite_sheet = Spritesheet('assets/effects/hit_effect_anim_spritesheet.png')
    hit_frame_2 = hit_sprite_sheet.sprite_at(8, 0, 8, 8)
    hit_frame_3 = hit_sprite_sheet.sprite_at(16, 0, 8, 8)

    hit_frame_2 = pygame.transform.scale(hit_frame_2, (32, 32))
    hit_frame_3 = pygame.transform.scale(hit_frame_3, (32, 32))

    self.hit_frames = [hit_frame_2, hit_frame_3]
    self.hit_idx = 0
    
  def run(self):
    while self.running:
      self.update_screen()
      self.check_events()
  
  def draw_pause_menu(self):
    self.screen.fill((0, 0, 0))
    title = self.font.render("PAUSED", False, (200, 255, 255))
    self.screen.blit(title, (560, 100))

    resume = self.font.render("ESC to resume", False, (200, 255, 255))
    self.screen.blit(resume, (535, 350))

    quit = self.font.render("Q to quit", False, (200, 255, 255))
    self.screen.blit(quit, (560, 400))
  
  def open_chest(self, chest):
    chest.open = True
  
  def check_open_chests(self):
    for chest in self.chest_group:
      if chest.open:
        chest.items.draw(self.screen)
    
  def pick_up_item(self, item, chest):
    if len(self.hero.sprite.inventory.items) == 8: return
    self.hero.sprite.inventory.items.add(item)
    self.hero.sprite.inventory.draw_item(item)
    chest.items.remove(item)
  
  def handle_interactions(self):
    for chest in self.chest_group:
      if chest.open:
        collided_items = pygame.sprite.spritecollide(self.hero.sprite, chest.items, False)
        if collided_items:
          self.pick_up_item(collided_items[0], chest)

    collided_chests = pygame.sprite.spritecollide(self.hero.sprite, self.chest_group, False) 
    if collided_chests: self.open_chest(collided_chests[0])
  
  def draw_menu(self):
    self.screen.fill((0, 0, 0))
    title = self.font.render("can you last", False, (200, 255, 255))
    self.screen.blit(title, (560, 100))

    start = self.font.render("SPACE to start", False, (200, 255, 255))
    self.screen.blit(start, (535, 350))

  def draw_wave(self):
    wave = self.font.render(f"WAVE {self.wave}", False, (255, 255, 255))
    wave = pygame.transform.scale_by(wave, 0.8)
    self.screen.blit(wave, (2, 2))
        
  def check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_e:
          self.handle_interactions()
        if event.key == pygame.K_SPACE and self.in_menu:
          self.in_menu = False
        if event.key == pygame.K_ESCAPE:
          self.in_pause_menu = not self.in_pause_menu
        if event.key == pygame.K_q and self.in_pause_menu:
          pygame.quit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        self.player_shooting = True
      if event.type == pygame.MOUSEBUTTONUP:
        self.player_shooting = False
        self.player_shoot_cooldown = 0
  
  def player_shoot(self):
    if self.player_shoot_cooldown > 0:
      self.player_shoot_cooldown -= 1
      return
    self.player_shoot_cooldown = self.PLAYER_SHOOT_COOLDOWN
    mouse_pos = pygame.mouse.get_pos()
    bullet = Bullet(self.hero.sprite.rect.x + 32, self.hero.sprite.rect.y + 32, mouse_pos[0], mouse_pos[1], 200, 10)
    self.bullets.add(bullet)

  def hit_animation(self, x, y):
    self.hit_idx += 0.2
    if self.hit_idx >= len(self.hit_frames):
      self.hit_idx = 0
    self.hit_image = self.hit_frames[int(self.hit_idx)]
    self.screen.blit(self.hit_image, (x, y))
  
  def check_bullet_collision(self):
    for enemy in self.enemies:
      collided_bullets = pygame.sprite.spritecollide(enemy, self.bullets, True)
      for bullet in collided_bullets:
        self.hit_animation(bullet.rect.x, bullet.rect.y)
        enemy.hit(self.hero.sprite.strength)
  
  def update_wave(self):
    if not self.enemies:
      self.wave += 1
      for _ in range(5 * self.wave):
        self.enemies.add(Slime())

  def update_screen(self):
    if self.in_menu:
      self.draw_menu()
    elif self.in_pause_menu:
      self.draw_pause_menu()
    else:
      self.world.render(self.screen)
      self.draw_wave()
      self.chest_group.draw(self.screen)
      self.chest_group.update()
      self.check_open_chests()
      self.hero.draw(self.screen)
      self.hero.update(self.screen)
      self.hero.sprite.inventory.render(self.screen)
      self.enemies.draw(self.screen)
      self.enemies.update(self.hero.sprite.rect.x, self.hero.sprite.rect.y)
      if self.player_shooting: self.player_shoot()
      self.bullets.draw(self.screen)
      self.bullets.update()
      self.check_bullet_collision()
      self.update_wave()

    pygame.display.flip()
    self.clock.tick(60)

game = Game()
game.run()	
