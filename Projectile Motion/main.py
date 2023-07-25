import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame.locals import *
from assets import *
import pygame
import math
import sys

clock = pygame.time.Clock()

time = 0
x = 0
y = 0

if len(sys.argv) != 4:
    print("Error: Provide 3 arguments (u, g, θ)")
    sys.exit(1)

try:
    speed = int(sys.argv[1])
    gravity = int(sys.argv[2])
    angle = int(sys.argv[3])

except ValueError:
    print("Error: Provide only integers")


class Obj():
    def __init__(self, x, y):
        self.image = obj
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed
        self.gravity = gravity
        self.angle = angle
        self.time = time

    def move(self, x, y, speed, angle, time):
        angleRadian = angle*(math.pi/180)
        uX = abs(math.cos(angleRadian)*speed)
        uY = abs(math.sin(angleRadian)*speed)

        sX = uX*time
        sY = (uY * time)+((-gravity * (time)**2)/2)

        dX = round(sX + x)
        dY = round(y - sY)

        return dX, dY

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


obj = Obj(110, 710)


def main():

    start = False
    hMax_occur = False

    while True:
        global pos

        angleRadian2 = obj.angle*(math.pi/180)

        hMax = round(((obj.speed**2)*(math.sin(angleRadian2)**2))/(2*obj.gravity))
        dRange = abs(round(((obj.speed**2)*(math.sin(2*angleRadian2)))/(obj.gravity)))

        mX = [(100, 720), (obj.rect.x, 720)]
        cX = (mX[0][0]+mX[1][0]/2)-55

        if 700-obj.rect.y < hMax-2:
            if not hMax_occur == True:
                mY = [((abs(dRange)/2)+100, 720), ((abs(dRange)/2)+100, obj.rect.y+20)]
        else:
            mY = [((abs(dRange)/2)+100, 720), ((abs(dRange)/2)+100, 700-hMax)]
            hMax_occur = True

        if start:
            if obj.rect.y < 701:
                time += 0.2
                pos = obj.move(x, y, speed, angle, time)
                obj.rect.x = pos[0]
                obj.rect.y = pos[1]
            else:
                start = False
                obj.rect.y = 700


        window.blit(bg, (0, 0))
        text(f"angle of projection: {obj.angle}°", font, 1100, 50)
        text(f"press 'space' to start", font, 1100, 300)
        text(f"initial velocity: {obj.speed}", font, 1100, 100)

        text(f"position: {obj.rect.x-100, 700-obj.rect.y}", font, 1100, 250)

        s = obj.rect.x - 110

        if start:
            text(f"displacement: *moving*", font, 1100, 150)
            text(f"max height: {hMax} px", font, 1100, 200)
        else:
            if s < 0:
                text(f"displacement: 0", font, 1100, 150)
                text("0 px", font2, cX, 740)
                text(f"max height: -", font, 1100, 200)
            else:
                text(f"displacement: {obj.rect.x-100} px", font, 1100, 150)
                text(f"{obj.rect.x-100} px", font2, cX-10, 740)
                text(f"max height: {hMax} px", font, 1100, 200)

        pygame.draw.line(window, (255, 255, 255), mX[0], mX[1])
        pygame.draw.line(window, (255, 255, 255), mY[0], mY[1])
        obj.show()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    start = True
                    x = obj.rect.x
                    y = obj.rect.y
                    time = 0
                    speed = obj.speed
                    angle = obj.angle

        pygame.display.update()
        clock.tick(60)


main()