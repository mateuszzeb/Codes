from pygame import *
import math, random

screen = display.set_mode([512, 512])
display.set_caption("Mouse move over dots")
rick = image.load("./rick.png") # <-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<- IMG POWINNO MIEĆ 512x512 px
level = 0

def avg_color(*args):
    avgR = 0
    avgG = 0
    avgB = 0
    for arg in args:
        avgR += arg[0]
        avgG += arg[1]
        avgB += arg[2]
    avgR = round(avgR/len(args), 0)
    avgG = round(avgG/len(args), 0)
    avgB = round(avgB/len(args), 0)
    return (avgR, avgG, avgB)

def get_avg_colors_from_surface(surface, x, w, y, h):
    colors = []
    for i in range(x, x+w, 1):
        for j in range(y, y+h, 1):
            colors.append(surface.get_at([i, j]))
    return avg_color(*colors)

class Levels:
    def __init__(self):
        self.levels = [256, 128, 64, 32, 16, 8, 4, 2, 1]
    def __getitem__(self, i):
        if i <= 8 and i >= 0:
            return self.levels[i]
        else:
            return 1
levels = Levels()

class Dot:
    objects = []
    def __init__(self, pos, level):
        self.color = get_avg_colors_from_surface(rick, int(round(pos[0] - (levels[level] / 2), 0)), levels[level], int(round(pos[1] - (levels[level] / 2))), levels[level])
        self.level = level
        self.pos = pos
        self.__class__.objects.append(self)
    def draw(self):
        draw.circle(screen, self.color, self.pos, levels[self.level])

    def division(self):
        Dot([self.pos[0] - (levels[self.level] / 2), self.pos[1] - (levels[self.level]/2)], self.level+1)
        Dot([self.pos[0] + (levels[self.level] / 2), self.pos[1] - (levels[self.level]/2)], self.level+1)
        Dot([self.pos[0] - (levels[self.level] / 2), self.pos[1] + (levels[self.level]/2)], self.level+1)
        Dot([self.pos[0] + (levels[self.level] / 2), self.pos[1] + (levels[self.level]/2)], self.level+1)
        
        self.__class__.objects.remove(self)

Dot([256, 256], 0)



while True:
    screen.fill([255, 255, 255])
    for evt in event.get():
        if evt.type == QUIT:
            exit()
        if evt.type == MOUSEMOTION:
            for dot in Dot.objects:
                if math.sqrt(abs(dot.pos[0] - mouse.get_pos()[0])**2 + abs(dot.pos[1] - mouse.get_pos()[1])**2) <= levels[dot.level] and dot.level < 7:
                    dot.division()
    for dot in Dot.objects:
        dot.draw()
    print(len(Dot.objects), end="\r")
    display.flip()
