import pygame
import random


class Enemy(object):
	walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
	pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
	pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'),
	pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
	walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
	            pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
	            pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'),
	            pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]
	
	def __init__(self, x, y, width, height, end, velocity):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.path = [x, end]
		self.velocity = velocity
		self.walkCount = 0
		self.health = 10
		self.visible = True
		self.hitbox = (self.x + 25, self.y + 10, self.width // 2 - 10, self.height // 2 + 20)
	
	def draw(self, window):
		if self.visible:
			self.move()
			if self.walkCount + 1 > 33:
				self.walkCount = 0
			if self.velocity > 0:
				window.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
				self.hitbox = (self.x + 25, self.y + 10, self.width // 2 - 10, self.height // 2 + 20)
				self.walkCount += 1
			else:
				window.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
				self.walkCount += 1
				self.hitbox = (self.x + 25, self.y + 10, self.width // 2 - 10, self.height // 2 + 20)

			pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
			pygame.draw.rect(window, (255, 0, 0), (1100, 70, 70, 20))
			pygame.draw.rect(window, (0, 255, 0), (1100, 70, 70 - (7 * (10 - self.health)), 20))
	
	def move(self):
		if self.velocity > 0:
			if self.x < self.path[1] - self.velocity:
				self.x += self.velocity
			else:
				self.velocity = self.velocity * -1
				self.x += self.velocity
				self.walkCount = 0
		else:
			if self.x > self.velocity + self.width:
				self.x += self.velocity
			else:
				self.velocity = self.velocity * -1
				self.x += self.velocity
				self.walkCount = 0
	
	def hit(self):
		if self.health > 0:
			self.health -= 1
			print("Hitman")
		else:
			self.visible = False
