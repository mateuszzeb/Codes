import pygame, sys
screen = pygame.display.set_mode([600, 500], pygame.RESIZABLE)
time = pygame.time.Clock()

pygame.display.set_caption("")
pygame.display.set_icon(pygame.image.load("img.png"))

while True:
	screen.fill([0, 0, 0])
	for evt in pygame.event.get():
		if evt.type == pygame.QUIT:
			sys.exit()
      
	time.tick(100)
	pygame.display.flip()
