import random
import pygame
from hero import Hero
from slime import Slime
from goblin import Goblin
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
    self.in_death_screen = False
    self.wave = 1
    self.display_new_wave_text = False
    self.hero = pygame.sprite.GroupSingle(Hero())
    self.enemies = pygame.sprite.Group()
    self.world = World()
    self.chest_group = pygame.sprite.Group()

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
    title = self.font.render("can you last", False, (255, 255, 255))
    self.screen.blit(title, (560, 100))

    start = self.font.render("SPACE to start", False, (255, 255, 255))
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
        if event.key == pygame.K_SPACE and self.in_death_screen:
          self.restart_game()
        if event.key == pygame.K_SPACE and self.display_new_wave_text:
          self.start_new_wave()
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
  
  def check_bullet_collisions(self):
    for enemy in self.enemies:
      collided_bullets = pygame.sprite.spritecollide(enemy, self.bullets, True)
      for bullet in collided_bullets:
        self.hit_animation(bullet.rect.x, bullet.rect.y)
        enemy.hit(self.hero.sprite.strength + 20)

  def check_enemy_collisions(self):
    collided_enemies = pygame.sprite.spritecollide(self.hero.sprite, self.enemies, False)
    for enemy in collided_enemies:
      if enemy.damage_cooldown > 0:
        enemy.damage_cooldown -= 1
        continue 
      self.hit_animation(enemy.rect.x, enemy.rect.y)
      self.hero.sprite.hit(enemy.damage)
      if self.hero.sprite.health <= 0:
        self.in_death_screen = True
      enemy.damage_cooldown = 60
  
  def update_wave(self):
    if not self.enemies and not self.display_new_wave_text:
      self.wave += 1
      self.display_new_wave_text = True
      self.spawn_chest()
  
  def start_new_wave(self):
    self.display_new_wave_text = False
    self.chest_group.empty()
    for _ in range(5 * self.wave):
      self.enemies.add(Slime())
      if self.wave >= 3: self.enemies.add(Goblin())
  
  def draw_new_wave_text(self):
    new_wave_text = self.font.render(f"SPACE to start wave {self.wave}", False, (255, 255, 255))
    self.screen.blit(new_wave_text, (450, 350))

  def spawn_chest(self):
    if self.wave < 3:
      self.chest_group.add(Chest(640, 300))
    elif self.wave >= 3 and self.wave < 5:
      self.chest_group.add(Chest(420, 300))
      self.chest_group.add(Chest(860, 300))
    elif self.wave >= 5:
      self.chest_group.add(Chest(320, 300))
      self.chest_group.add(Chest(640, 300))
      self.chest_group.add(Chest(960, 300))

  def draw_death_screen(self):
    self.screen.fill((0, 0, 0))
    title = self.font.render("YOU DIED", False, (255, 255, 255))
    self.screen.blit(title, (560, 100))

    restart = self.font.render("SPACE to restart", False, (255, 255, 255))
    self.screen.blit(restart, (535, 350))

  def restart_game(self):
    self.in_death_screen = False
    self.wave = 1
    self.hero.sprite.health = 100
    self.hero.sprite.speed = 5
    self.hero.sprite.strength = 5
    self.hero.sprite.healing = 5
    self.hero.sprite.inventory.items.empty()
    self.hero.sprite.inventory.weapon.empty()
    self.hero.sprite.inventory.weapon.add(self.hero.sprite.inventory.iron_sword)
    self.hero.sprite.rect = self.hero.sprite.image.get_rect(midbottom = (640, 384))
    self.enemies.empty()
    self.bullets.empty()
    self.start_new_wave()

  def update_screen(self):
    if self.in_menu:
      self.draw_menu()
    elif self.in_pause_menu:
      self.draw_pause_menu()
    elif self.in_death_screen:
      self.draw_death_screen()
    else:
      self.world.render(self.screen)
      self.draw_wave()
      self.chest_group.draw(self.screen)
      self.chest_group.update(self.screen)
      self.check_open_chests()
      self.hero.draw(self.screen)
      self.hero.update(self.screen)
      self.hero.sprite.inventory.render(self.screen)
      self.enemies.draw(self.screen)
      self.enemies.update(self.hero.sprite.rect.x, self.hero.sprite.rect.y, self.screen)
      if self.player_shooting: self.player_shoot()
      self.bullets.draw(self.screen)
      self.bullets.update()
      self.check_bullet_collisions()
      self.check_enemy_collisions()
      self.update_wave()
      if self.display_new_wave_text: self.draw_new_wave_text()

    pygame.display.flip()
    self.clock.tick(60)

game = Game()
game.run()	
