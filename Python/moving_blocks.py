import pygame, random

screen = pygame.display.set_mode([0, 0])

class Block:
    objects = []
    def create_surface(self):
        self.surface = pygame.Surface([self.width, self.height])
        self.surface.fill(self.color)

    def move(self, x, y):
        self.moving = True
        self.drag_x = x - self.x
        self.drag_y = y - self.y
        Block.objects.remove(self)
        Block.objects.append(self)
        
    def __init__(self, w, h, x, y, c):
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        self.moving = False
        self.color = c
        Block.objects.append(self)
        self.create_surface()
    
    def draw(self, surface):
        surface.blit(self.surface, [self.x, self.y])
    
    def delete(self):
        Block.objects.remove(self)
        
for i in range(10):
    Block(100, 100, random.randint(0,screen.get_width()-40), random.randint(0,screen.get_height()-40), (random.randint(0,255), random.randint(0,255), random.randint(0,255)))


mouse_down = [0, 0]
while True:
    screen.fill([255, 255, 255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for block in Block.objects:
                x, y = pygame.mouse.get_pos()
                mouse_down = [x, y]
                if block.x <= x and block.x + block.width >= x and block.y <= y and block.y + block.height >= y:
                    b = block
            try:
                b.move(x, y)
                b = None
            except:
                pass
        if event.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()
            for block in Block.objects:
                if block.moving:
                    block.x = x-block.drag_x
                    block.y = y-block.drag_y
        if event.type == pygame.MOUSEBUTTONUP:
            for block in Block.objects:
                block.moving = False

    for block in Block.objects:
        block.draw(screen)
    
    pygame.display.flip()
