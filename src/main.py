import pygame

class Game:
  WIDHT = 1280
  HEIGHT = 800

  def __init__(self):
    pygame.init()
    self.clock = pygame.time.Clock()
    self.screen = pygame.display.set_mode((1280,800), pygame.RESIZABLE)
    self.running = True

  def run(self):
    while self.running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()

    pygame.display.update()
    self.clock.tick(60)

game = Game()
game.run()	
