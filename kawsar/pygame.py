import pygame

WIN = pygame.display.set_mode((900, 500))

def main():
	run = true
	while(run):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = false
	pygame.quit()
