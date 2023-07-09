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

    self.block_size = 64
    self.blocks = []
    self.world_size = (1280, 1280)

    for _ in range(12):
      row = [random.choice([F_1, F_2, F_3, F_4, F_5, F_6, F_7, F_8, F_9, F_10]) for _ in range(20)]
      self.blocks.append(row)
  
  def render(self, screen):
    for row in range(len(self.blocks)):
      for col in range(len(self.blocks[0])):
        screen.blit(self.blocks[row][col].image, (col * self.block_size, row * self.block_size))