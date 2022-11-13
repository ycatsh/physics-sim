import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import pygame, sys
import math
from pygame.locals import *

clock = pygame.time.Clock()

pygame.init()

windowSize = (1500, 800)
window = pygame.display.set_mode((windowSize), pygame.NOFRAME, vsync=1)

text_color = (255,255,255)
def mtext(text, font, text_color, x, y):
	m = font.render(text, True, text_color)
	window.blit(m, (x,y))

obj = pygame.image.load(f'assets/ball.png').convert_alpha()
bg = pygame.image.load(f'assets/bg.png').convert_alpha()
font = pygame.font.Font('fonts/font.ttf', 25)
font2 = pygame.font.Font('fonts/font.ttf', 15)

time = 0
x = 0
y = 0

userValues = 0

#bootleg error handler 
n = 0 
try:
	while True: 
		n += 1
	
		while userValues < 3:
			speed = int(input('\nENTER SPEED VALUE (1, 50 pixels per second): '))
			gravity = int(input('\nENTER GRAVITY VALUE (1, 25 pixels per second): '))
			angle = int(input('\nENTER ANGLE OF PROJECTION VALUE (1, 91 deg): '))
			print('\n')

			if speed <= 50 and speed > 0:
				userValues += 1
			else:
				userValues = 0
				print('Error! please enter a valid initial speed\n')

			if gravity <= 25 and gravity > 0:
				userValues += 1
			else:
				userValues = 0
				print('Error! please enter valid acceleration due to gravity\n')

			if angle < 91 and angle > 0:
				userValues += 1
			else:
				userValues = 0
				print('Error! please enter a valid angle\n')

			if userValues < 3:
				userValues = 0

			if userValues == 3:
				print(f'check the opened window!\n\nAttributed Values:\nu={speed}\ng={gravity}\nangle={angle}')
				break

		class Obj():
			def __init__(self, x, y):
				self.image = obj
				self.rect = self.image.get_rect()
				self.rect.center = (x,y)
				self.speed = speed 
				self.gravity = gravity 
				self.angle = angle 
				self.time = time 

			def move(self, x, y, speed, angle, time):
				angleRadian = angle*(math.pi/180)
				uX = abs(math.cos(angleRadian)*speed)
				uY = abs(math.sin(angleRadian)*speed)

				sX = uX*time #displacement along x (here) = speed * time 
				sY = (uY * time)+((-gravity * (time)**2)/2) #displacement along y (here) = u*t + [1/2*{a*(t^2)}] {u = initial velocity, t = time, a = acceleratiopn due to force of gravity}

				dX = round(sX + x)
				dY = round(y - sY)

				return dX, dY

			def show(self):
				window.blit(self.image, (self.rect.x, self.rect.y))

		obj = Obj(112, 712)

		def main():

			start = False 

			while True:
				global pos

				mX = [(100,724), (obj.rect.x, 724)]

				if start:
					if obj.rect.y < 700+24:
						time += 0.3
						pos = obj.move(x, y, speed, angle, time)
						obj.rect.x = pos[0]
						obj.rect.y = pos[1]
					else: 
						start = False 
						obj.rect.y = 700
				
				if userValues == 3:
					window.blit(bg, (0, 0))
					mtext(f"angle of projection: {obj.angle}°", font, text_color, 100, 50)
					mtext(f"press 'space' to start", font, text_color, 700, 50)
					mtext(f"initial velocity: {obj.speed}", font, text_color, 100, 100)

					mtext(f"position: {obj.rect.x, obj.rect.y}", font, text_color, 700, 100) 

					s = obj.rect.x - 112
					cX = ((mX[0])[0])+((((mX[1])[0])-((mX[0])[0]))/2)
					angleRadian2 = obj.angle*(math.pi/180)

					hMax = round(((obj.speed**2)*(math.sin(angleRadian2)**2))/(2*obj.gravity))
					dRange = round(((obj.speed**2)*(math.sin(2*angleRadian2)))/(obj.gravity))
					
					if start:
						mtext(f"displacement: *moving*", font, text_color, 100, 150) 
					else:
						if s < 0:
							mtext(f"displacement: 0", font, text_color, 100, 150)
							mtext("0 px", font2, text_color, cX, 740) 
							mtext(f"max height: -", font, text_color, 700, 150)
						else: 
							mtext(f"displacement: {dRange} units along x axis", font, text_color, 100, 150)
							mtext(f"{dRange} px", font2, text_color, cX, 740) 
							mtext(f"max height: {hMax} px", font, text_color, 700, 150)

					pygame.draw.line(window, (255, 255, 255), mX[0], mX[1])
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

except KeyboardInterrupt:
	n = -1
	print('\n\n*simulation closed*\n')
	pygame.quit()
	if n == -1:
		sys.exit()
	