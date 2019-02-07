import pygame


class Projectiles(object):
	def __init__(self, x, y, radius, color, velocity, facing):
		self.radius = radius
		self.x = x
		self.y = y
		self.color = color
		self.facing = facing
		self.velocity = velocity * facing

	def draw(self, window):
		pygame.draw.circle(window, self.color, (self.x, self.y), self.radius )