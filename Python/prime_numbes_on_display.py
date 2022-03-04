import pygame, sys, random
screen = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)
time = pygame.time.Clock()
surface = pygame.Surface([5000, 5000])
surface.fill([255, 255, 255])
pygame.display.set_caption("")
screen.fill([255, 255, 255])
showX = screen.get_width()/2-2500
showY = screen.get_height()/2-2500
def czy_pierwsza(l):
    for i in range(2, l):
        if l%i==0:
            return False
    print(l)
    return True

i = 0
j = 0
k = 0
k2 = 0
x = 2500
y = 2500
go = [0, 1]
while True:
    if k > 30000:
        break
    pygame.draw.rect(surface, (0, 0, 0), (x-1, y-1, 2, 2))
    x+=go[0]
    y+=go[1]
    k2+=1
    if k2 == 100:
        k += 1
        k2 = 0
        if czy_pierwsza(k):
            pygame.draw.rect(surface, (255, 0, 0), (x-4, y-4, 8, 8))
    if i == 5*j:
        i = 0
        j+=1
        if go == [0, 1]:
            go = [-1, 0]
        elif go == [-1, 0]:
            go = [0, -1]
        elif go == [0, -1]:
            go = [1, 0]
        elif go == [1, 0]:
            go = [0, 1]
    else:
        i += 1
    

while True:
    screen.fill([255, 255, 255])
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        showX+=1
    if keys[pygame.K_RIGHT]:
        showX-=1
    if keys[pygame.K_UP]:
        showY+=1
    if keys[pygame.K_DOWN]:
        showY-=1
        
    screen.blit(surface, [showX, showY])
    pygame.display.flip()
