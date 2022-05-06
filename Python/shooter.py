from pygame import *
import math

def move_dot(degrees, magnitude):
    return magnitude * math.cos(math.radians(degrees)), magnitude * math.sin(math.radians(degrees))

init()
font.init()

fps = 1
clc = time.Clock()

screen = display.set_mode([0, 0], FULLSCREEN)

class Bullet:
    objects = []
    def __init__(self, x, y, move_x, move_y):
        self.move_x = move_x
        self.move_y = move_y
        self.radius = 5
        self.pos = Vector2(x, y)
        self.color = (255, 255, 255)
        self.__class__.objects.append(self)
        self.speed = 20

    def draw(self):
        draw.circle(screen, self.color, (self.pos.x, self.pos.y), self.radius)

    def move(self):
        self.pos.x += self.move_x*self.speed/fps
        self.pos.y += self.move_y*self.speed/fps
        if self.pos.x <= 0 or self.pos.x >= screen.get_width():
            self.move_x = -self.move_x
        if self.pos.y <= 0 or self.pos.y >= screen.get_height():
            self.move_y = -self.move_y


class Player:
    objects = []
    def __init__(self, color):
        self.color = color
        self.radius = 40
        self.deg = 0
        self.eye_radius = 10
        self.move_speed = 3
        self.rotate_speed = 90
        self.pos = Vector2(screen.get_width() / 2 - self.radius, screen.get_height() / 2 - self.radius)
        self.__class__.objects.append(self)

    def draw(self):
        draw.circle(screen, self.color, (self.pos.x, self.pos.y), self.radius)
        x, y = move_dot(self.deg, self.radius - self.eye_radius - 2)
        draw.circle(screen, (0, 0, 0), (self.pos.x + x, self.pos.y + y), self.eye_radius)

    def go_ahead(self):
        x, y = move_dot(self.deg, self.move_speed)
        self.pos.x += x*self.move_speed/fps
        self.pos.y += y*self.move_speed/fps
    
    def create_bullet(self):
        move_x, move_y= move_dot(self.deg, 200)
        Bullet(self.pos.x, self.pos.y, move_x/200, move_y/200)

Player([0, 255, 0])

def main():
    while True:
        screen.fill([40, 40, 40])
        for ev in event.get():
            if ev.type == QUIT:
                exit()
            if ev.type == KEYUP:
                if ev.key == K_SPACE:
                    for player in Player.objects:
                        player.create_bullet()
                if ev.key == K_r:
                    for bullet in Bullet.objects:
                        bullet.radius -= 1
                if ev.key == K_t:
                    for bullet in Bullet.objects:
                        bullet.radius += 1
                        
                    print(len(Bullet.objects))


        keys = key.get_pressed()

        if keys[K_LEFT]:
            for player in Player.objects:
                player.deg -= 1*player.rotate_speed/(fps+1)
        if keys[K_RIGHT]:
            for player in Player.objects:
                player.deg += 1*player.rotate_speed/(fps+1)
        if keys[K_UP]:
            for player in Player.objects:
                player.go_ahead()
        if keys[K_SPACE]:
            for player in Player.objects:
                player.create_bullet()

        for bullet in Bullet.objects:
            bullet.move()
            bullet.draw()

        for player in Player.objects:
            player.draw()
        clc.tick(60)
        fps = clc.get_fps()
        display.flip()

if __name__ == '__main__':
    main()
