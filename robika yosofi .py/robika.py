import pygame
import os


WIDTH, HEIGHT=900,500
WIN = pygame.display.set mode((WIDTH, HEIGHT))
pygame.display.set caption("spaceship famle")
WHITH=(255.255.255)
SPACESHIP_WIDTH. SPACESHIP_HEIGHT=55,40


YELLOW_SPACESHIP_IMAGE=pygame.image.load(os.path.join("Assets",' spaceship_yellow.png'))
YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP IMAGE.	(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),90)
RED_SPACESHIP_IMAGE=pygame.image.load(ospath.join("Assets", 'SPACESHIP_red.png'))
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH. SPACESHIP_HEIGHT)),270)
 


def draw_window():
	WIN.fill((255,255,255))
	WIN.blit(YELLOW_SPACESHIP, (300, 100))
	WIN blit(RED_SPACESHIP,(700, 100))
	pygame.display.update(


  def main():
  	run=True
  	while(run):
  		for event in pygame.event.get():
  			if event.type== pygame.QUIT:
  				run = false
  		draw_window()
  	pygame.quit()
  if_name_=="_main_":
  		
  		





  











