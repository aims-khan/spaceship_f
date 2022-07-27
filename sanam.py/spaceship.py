 improt pygame
 improt os

 WIDTH,HEIGHT = 900,500
 WIN = pygame.display.set_mode((WIDTH, HEIGHT))
 pygame.diplay.set_coption("spaceship female")
 WHITE = (255,255,255)
 SPACESHIP_WIDTH, SPACESHIP_HEIGHT =55, 40

 YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets",'spaceship_yellow.png'))
 YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
 
 RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets",'spaceship_red.png'))
 RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


 def draw_window():
     WIN.fill((255,255,255))
     WIN.blit(YELOW_SPACESHIOP, (300, 100))
     win.blit(RED_SPACESHIP, (700, 100))
     pygame.dispaly.update()
 
 def main():
     run = True
     while(run):
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                  run = False
            draw_window()
     pygame.quit()
 if__name__ == "__main__":

