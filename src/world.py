import pygame
import random
from block import Block

class World:
  def __init__(self):
    F_1 = Block(16, 16, 'assets/tiles/floor/floor_1.png')
    F_2 = Block(16, 16, 'assets/tiles/floor/floor_2.png')
    F_3 = Block(16, 16, 'assets/tiles/floor/floor_3.png')
    F_4 = Block(16, 16, 'assets/tiles/floor/floor_4.png')
    F_5 = Block(16, 16, 'assets/tiles/floor/floor_5.png')
    F_6 = Block(16, 16, 'assets/tiles/floor/floor_6.png')
    F_7 = Block(16, 16, 'assets/tiles/floor/floor_7.png')
    F_8 = Block(16, 16, 'assets/tiles/floor/floor_8.png')
    F_9 = Block(16, 16, 'assets/tiles/floor/floor_9.png')
    F_10 = Block(16, 16, 'assets/tiles/floor/floor_10.png')

    self.ROWS = 12 # 12 * 64 = 768 (screen height)
    self.COLS = 20 # 20 * 64 = 1280 (screen width)
    self.block_size = 64
    self.blocks = []
    self.i = 30
    self.j = 30

    for _ in range(100):
      row = [random.choice([F_1, F_2, F_3, F_4, F_5, F_6, F_7, F_8, F_9, F_10]) for _ in range(100)]
      self.blocks.append(row)

  def shift_world(self, direction):
    if direction == 'u':
      print("shift up")
      self.j -= 1
    elif direction == 'd':
      print("shift down")
      self.j += 1
    elif direction == 'l':
      print("shift left")
      self.i -= 1
    elif direction == 'r':
      print("shift right")
      self.i += 1
  
  def render(self, screen):
    for row in range(self.ROWS):
      for col in range(self.COLS):
        screen.blit(self.blocks[row + self.j][col + self.i].image, (col * self.block_size, row * self.block_size))
    