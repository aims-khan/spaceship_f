import pygame
import os


WIDTH. HEIGHT =900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.dispaly.set_caption("spiceship femle")
WIDTH =(255,255,255)
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.iamge.load(os.path.join("Assets",'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,SPACESHIP_WIDTH,spaceship_HEIGHT)),90)
RED_SPICESHIP_IMAGE=pygame.image.load(os.path.join("Assets",'spiceship_yellow.png'))
RED_SPICESHIP= pygame.transform.rotate(pygame.transform.scale(RED_SPICESHIP_IMAGE,(SPICESHIP_WEDTH,SPICESHIP_HEIGHT)),270)

def draw_window():
	WIN.fill((255,255,255))
	WIN.blit(yellow_spicsship,(300,100))
	WIN.blit(RED_SPICESHIP,(100))
	pygame.display.update()

def main ();
    run = True
    While(run):
        for event in pygame.event.get():
        	if even.type ==pygame.QUIT:
        		run = False
        draw_window()
      pygame.quit()
      if __name__ == "__main__"
      main()	