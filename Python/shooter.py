import pygame
from pygame import *
import math
import random


def move_dot(degrees, magnitude):
    return magnitude * math.cos(math.radians(degrees)), magnitude * math.sin(math.radians(degrees))


init()
font.init()

fps = 1
clc = time.Clock()

screen = display.set_mode([0, 0], FULLSCREEN)


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def is_touching(bullet, player):
    if abs(bullet.pos.x - player.pos.x) ** 2 + abs(bullet.pos.y - player.pos.y) < (player.radius + bullet.radius):
        return True
    return False


class Bullet:
    objects = []

    def __init__(self, owner, x, y, move_x, move_y, color=(255, 255, 255)):
        self.move_x = move_x
        self.move_y = move_y
        self.owner = owner
        self.radius = 5
        self.pos = Vector2(x, y)
        self.color = color
        self.__class__.objects.append(self)
        self.speed = 20

    def draw(self):
        draw.circle(screen, self.color, (self.pos.x, self.pos.y), self.radius)

    def move(self):
        self.pos.x += self.move_x * self.speed / fps
        self.pos.y += self.move_y * self.speed / fps
        for player in Player.objects:
            if player.color != self.owner.color:
                if is_touching(self, player):
                    player.hidden = True


class Player:
    objects = []

    def __init__(self, x, y, d, color, keys=None):
        if keys is None:
            keys = [K_a, K_d, K_w, K_SPACE]
        self.color = color
        self.hidden = False
        self.radius = 40
        self.keys = keys
        self.deg = d
        self.eye_radius = 10
        self.move_speed = 3
        self.rotate_speed = 220
        self.pos = Vector2(x, y)
        self.__class__.objects.append(self)

    def draw(self):
        if not self.hidden:
            draw.circle(screen, self.color, (self.pos.x, self.pos.y), self.radius)
            x, y = move_dot(self.deg, self.radius - self.eye_radius - 2)
            draw.circle(screen, (0, 0, 0), (self.pos.x + x, self.pos.y + y), self.eye_radius)

    def go_ahead(self):
        x, y = move_dot(self.deg, self.move_speed)
        self.pos.x += x * self.move_speed / fps
        self.pos.y += y * self.move_speed / fps

    def create_bullet(self):
        if not self.hidden:
            move_x, move_y = move_dot(self.deg, 200)
            Bullet(self, self.pos.x, self.pos.y, move_x / 200, move_y / 200)


Player(40, 200, 225, [0, 255, 0], keys=[K_LEFT, K_RIGHT, K_UP, K_RETURN])
Player(screen.get_width() - 200, screen.get_height() - 40, 45, [255, 0, 0])


def main():
    while True:
        screen.fill([40, 40, 40])
        for ev in event.get():
            if ev.type == QUIT:
                exit()
            if ev.type == KEYUP:
                if ev.key == K_r:
                    for bullet in Bullet.objects:
                        del bullet
                for player in Player.objects:
                    if ev.key == player.keys[3]:
                        player.create_bullet()

        keys = key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            exit()

        for player in Player.objects:
            if keys[player.keys[0]]:
                player.deg -= player.rotate_speed / (fps + 1)
            if keys[player.keys[1]]:
                player.deg += player.rotate_speed / (fps + 1)
            if keys[player.keys[2]]:
                player.go_ahead()

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
