import pygame

FLOOR_1 = 0
FLOOR_2 = 1
FLOOR_3 = 2
FLOOR_4 = 3
FLOOR_5 = 4
FLOOR_6 = 5
FLOOR_7 = 6
FLOOR_8 = 7
FLOOR_9 = 8
FLOOR_10 = 9

floor_tiles = {
  FLOOR_1: pygame.transform.scale_by(pygame.image.load('assets/tiles/floor/floor_1.png'), 5),
  FLOOR_2: pygame.transform.scale_by(pygame.image.load('assets/tiles/floor/floor_2.png'), 5),
  FLOOR_3: pygame.transform.scale_by(pygame.image.load('assets/tiles/floor/floor_3.png'), 5),
  FLOOR_4: pygame.transform.scale_by(pygame.image.load('assets/tiles/floor/floor_4.png'), 5),
  FLOOR_5: pygame.transform.scale_by(pygame.image.load('assets/tiles/floor/floor_5.png'), 5),
  FLOOR_6: pygame.transform.scale_by(pygame.image.load('assets/tiles/floor/floor_6.png'), 5),
  FLOOR_7: pygame.transform.scale_by(pygame.image.load('assets/tiles/floor/floor_7.png'), 5),
  FLOOR_8: pygame.transform.scale_by(pygame.image.load('assets/tiles/floor/floor_8.png'), 5),
  FLOOR_9: pygame.transform.scale_by(pygame.image.load('assets/tiles/floor/floor_9.png'), 5),
  FLOOR_10: pygame.transform.scale_by(pygame.image.load('assets/tiles/floor/floor_10.png'), 5),
}

class Floor:
  def __init__(self):
    self.tilesize = floor_tiles[FLOOR_1].get_width()
    self.tilemap = [
      [FLOOR_1, FLOOR_5, FLOOR_3, FLOOR_1, FLOOR_3, FLOOR_1, FLOOR_3, FLOOR_10, FLOOR_9, FLOOR_1, FLOOR_7, FLOOR_3, FLOOR_1, FLOOR_9, FLOOR_7, FLOOR_4],
      [FLOOR_2, FLOOR_5, FLOOR_6, FLOOR_4, FLOOR_1, FLOOR_4, FLOOR_6, FLOOR_2, FLOOR_4, FLOOR_8, FLOOR_4, FLOOR_2, FLOOR_2, FLOOR_9, FLOOR_9, FLOOR_2],
      [FLOOR_4, FLOOR_8, FLOOR_9, FLOOR_8, FLOOR_8, FLOOR_8, FLOOR_8, FLOOR_4, FLOOR_6, FLOOR_1, FLOOR_6, FLOOR_7, FLOOR_8, FLOOR_7, FLOOR_2, FLOOR_2],
      [FLOOR_10, FLOOR_1, FLOOR_9, FLOOR_2, FLOOR_2, FLOOR_2, FLOOR_8, FLOOR_5, FLOOR_2, FLOOR_5, FLOOR_1, FLOOR_6, FLOOR_9, FLOOR_8, FLOOR_3, FLOOR_8],
      [FLOOR_1, FLOOR_2, FLOOR_3, FLOOR_1, FLOOR_3, FLOOR_1, FLOOR_3, FLOOR_6, FLOOR_10, FLOOR_2, FLOOR_4, FLOOR_6, FLOOR_5, FLOOR_8, FLOOR_6, FLOOR_7],
      [FLOOR_4, FLOOR_5, FLOOR_6, FLOOR_6, FLOOR_1, FLOOR_4, FLOOR_2, FLOOR_7, FLOOR_8, FLOOR_3, FLOOR_10, FLOOR_8, FLOOR_5, FLOOR_3, FLOOR_6, FLOOR_8],
      [FLOOR_9, FLOOR_8, FLOOR_2, FLOOR_3, FLOOR_8, FLOOR_8, FLOOR_2, FLOOR_9, FLOOR_8, FLOOR_1, FLOOR_2, FLOOR_9, FLOOR_2, FLOOR_1, FLOOR_2, FLOOR_2],
      [FLOOR_10, FLOOR_1, FLOOR_2, FLOOR_7, FLOOR_2, FLOOR_2, FLOOR_7, FLOOR_4, FLOOR_4, FLOOR_1, FLOOR_9, FLOOR_10, FLOOR_7, FLOOR_4, FLOOR_1, FLOOR_4],
      [FLOOR_3, FLOOR_2, FLOOR_6, FLOOR_2, FLOOR_3, FLOOR_10, FLOOR_6, FLOOR_3, FLOOR_3, FLOOR_10, FLOOR_9, FLOOR_1, FLOOR_7, FLOOR_4, FLOOR_9, FLOOR_5],
      [FLOOR_4, FLOOR_5, FLOOR_3, FLOOR_1, FLOOR_1, FLOOR_4, FLOOR_5, FLOOR_3, FLOOR_10, FLOOR_1, FLOOR_5, FLOOR_3, FLOOR_8, FLOOR_7, FLOOR_8, FLOOR_5],
      [FLOOR_2, FLOOR_8, FLOOR_9, FLOOR_9, FLOOR_8, FLOOR_8, FLOOR_3, FLOOR_9, FLOOR_3, FLOOR_1, FLOOR_7, FLOOR_3, FLOOR_8, FLOOR_6, FLOOR_8, FLOOR_4],
      [FLOOR_10, FLOOR_1, FLOOR_2, FLOOR_8, FLOOR_2, FLOOR_2, FLOOR_9, FLOOR_1, FLOOR_3, FLOOR_1, FLOOR_2, FLOOR_3, FLOOR_9, FLOOR_2, FLOOR_2, FLOOR_1]
    ]
  
  def render(self, screen):
    for row in range(len(self.tilemap)):
      for col in range(len(self.tilemap[0])):
        screen.blit(floor_tiles[self.tilemap[row][col]], (col * self.tilesize, row * self.tilesize))