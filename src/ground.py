import pygame
from block import Block

class Ground(pygame.sprite.Sprite):
    def __init__(self):
      super().__init__()
      self.blocks = pygame.sprite.Group()
      self.blocks.add(Block(200, 400, 'assets/tiles/floor/floor_1.png'))
      self.blocks.add(Block(216, 400, 'assets/tiles/floor/floor_1.png'))
      self.blocks.add(Block(232, 400, 'assets/tiles/floor/floor_1.png'))
      self.blocks.add(Block(248, 400, 'assets/tiles/floor/floor_1.png'))
      self.blocks.add(Block(264, 400, 'assets/tiles/floor/floor_1.png'))
      self.blocks.add(Block(280, 400, 'assets/tiles/floor/floor_1.png'))
      self.blocks.add(Block(296, 400, 'assets/tiles/floor/floor_1.png'))
      self.blocks.add(Block(312, 400, 'assets/tiles/floor/floor_1.png'))
      self.blocks.add(Block(328, 400, 'assets/tiles/floor/floor_1.png'))
      self.blocks.add(Block(344, 400, 'assets/tiles/floor/floor_1.png'))
