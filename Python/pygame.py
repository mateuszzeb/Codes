import pygame, sys
screen = pg.display.set_mode([600, 500], pg.RESIZABLE)
time = pg.time.Clock()


while True:
	screen.fill([0, 0, 0])
	for evt in pg.event.get():
		if evt.type == pg.QUIT:
			sys.exit()
      
	time.tick(100)
	pg.display.flip()
