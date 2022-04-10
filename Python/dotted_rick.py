from pygame import *
from pygame import camera
import math, random, sys, requests, os

clc = time.Clock()

if len(sys.argv) != 3:
    sys.exit("\npython rick.py --type --path\n - file file.png\n - web https://url.to.image/")

screen = display.set_mode([512, 512])
display.set_caption("Mouse move over dots")
if sys.argv[1] == "file":
    _image = image.load(sys.argv[2])
elif sys.argv[1] == "web":
    open("file.png", "wb").write(requests.get(sys.argv[2]).content)
    _image = image.load("file.png")
elif sys.argv[1] == "camera":
    camera.init()
    cameras = camera.list_cameras()
    webcam = camera.Camera(cameras[0])
    webcam.start()
    _image = webcam.get_image()
    
_image = transform.scale(_image, [512, 512])
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
        self.level = level
        self.pos = pos
        self.color = [0, 0, 0]
        self.__class__.objects.append(self)
        
    def load_color(self):
        self.color = get_avg_colors_from_surface(_image, int(round(self.pos[0] - (levels[self.level] / 2), 0)), levels[self.level], int(round(self.pos[1] - (levels[self.level] / 2))), levels[self.level])
   
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
    screen.fill([20, 20, 20])
    for evt in event.get():
        if evt.type == QUIT:
            exit()
        if evt.type == MOUSEMOTION:
            for dot in Dot.objects:
                if dot.level < 10:
                    if math.sqrt(abs(dot.pos[0] - mouse.get_pos()[0])**2 + abs(dot.pos[1] - mouse.get_pos()[1])**2) <= levels[dot.level]:
                        dot.division()

    for dot in Dot.objects:
        dot.load_color()
        dot.draw()
    if sys.argv[1] == "camera":
        _image = webcam.get_image()
        _image = transform.flip(_image, True, False)
    _image = transform.scale(_image, [512, 512])
    clc.tick(60)
    print(clc.get_fps(), end="\r")
    display.flip()
