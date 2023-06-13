import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
from pygame.locals import *
import math
from assets import *

clock = pygame.time.Clock()

time = 0
x = 0
y = 0

userValues = 0

while userValues < 3:
    speed = int(
        input('\nENTER INITIAL SPEED (1, 100 px/s): '))
    gravity = int(
        input('\nENTER ACC DUE TO GRAVITY (1, 25 px/s): '))
    angle = int(
        input('\nENTER ANGLE OF PROJECTION (1, 90): '))

    if speed <= 100 and speed > 0:
        userValues += 1
    else:
        userValues = 0
        print('\nError! please enter a valid initial speed\n')

    if gravity <= 25 and gravity > 0:
        userValues += 1
    else:
        userValues = 0
        print('\nError! please enter valid acceleration due to gravity\n')

    if angle < 91 and angle > 0:
        userValues += 1
    else:
        userValues = 0
        print('\nError! please enter a valid angle\n')

    if userValues < 3:
        userValues = 0

    if userValues == 3:
        print(
            f'\ncheck the opened window!')
        break


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

        sX = uX*time  # displacement along x (here) = speed * time
        # displacement along y (here) = u*t + [1/2*{a*(t^2)}] {u = initial velocity, t = time, a = acceleratiopn due to force of gravity}
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

        if userValues == 3:
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