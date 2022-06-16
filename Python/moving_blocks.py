# file settings.json should have at least {}
# when you are clicking n than is creating new block on mouse position
# but when you are clicking DEL and your mouse is over some block than that block will be deleted

import pygame, random, json

screen = pygame.display.set_mode([0, 0])

class Block:
    objects = []

    @staticmethod
    def get_json():
        json_data = "{"
        i = 0
        for obj in Block.objects:
            json_data += f'\n\t"{i}":' + "{\n\t\t"
            json_data += f'"x": {obj.x},\n\t\t"y": {obj.y},\n\t\t"w": {obj.width},\n\t\t"h": {obj.height},\n\t\t"c": {list(obj.color)}'
            json_data += "\n\t},"
            i += 1
        json_data = json_data[:-1]
        json_data += "\n}"
        return json_data

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
        pygame.draw.rect(surface, [255, 255, 255], [self.x, self.y, self.width, self.height], 5)

    def delete(self):
        Block.objects.remove(self)

with open("settings.json", "r") as file:
    json_data = json.load(file)
    for obj in json_data:
        w = json_data[obj]['w']
        h = json_data[obj]['h']
        x = json_data[obj]['x']
        y = json_data[obj]['y']
        c = json_data[obj]['c']
        Block(w, h, x, y, c)

def exit_and_save():
    json_data = Block.get_json()
    with open("settings.json", "w") as file:
        file.write(json_data)
    exit()

mouse_down = [0, 0]
while True:
    screen.fill([0, 0, 0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_and_save()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit_and_save()
            if event.key == pygame.K_n:
                Block(100, 100, pygame.mouse.get_pos()[0] - 50, pygame.mouse.get_pos()[1] - 50, [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
            if event.key == pygame.K_DELETE:
                deleted_block = None
                for block in Block.objects:
                    x, y = pygame.mouse.get_pos()
                    if block.x <= x and block.x + block.width >= x and block.y <= y and block.y + block.height >= y:
                        deleted_block = block
                if deleted_block is not None:
                    deleted_block.delete()

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
                    block.x = x - block.drag_x
                    block.y = y - block.drag_y
        if event.type == pygame.MOUSEBUTTONUP:
            for block in Block.objects:
                block.moving = False

    for block in Block.objects:
        block.draw(screen)

    pygame.display.flip()
