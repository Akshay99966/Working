import pygame
import MyPlayer
from MyProjectile import Projectiles
from MyEnemy import Enemy

# Initialise pygame
pygame.init()

# Screen Size
length = 1200
breadth = 600

# Display Screen, Title
window = pygame.display.set_mode((length, breadth))
pygame.display.set_caption('Chase ME')

bulletsound = pygame.mixer.Sound('bullet.wav')
hitsound = pygame.mixer.Sound('hit.wav')
shellsound = pygame.mixer.Sound('shell.wav')
m = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
score = 0

# Set Background Image
background = pygame.image.load('background1.jpg')


# Draw Function
def draw():
	window.blit(background, (0, 0))
	text = font.render('HITPOINTS - ' + str(score), 1, (0, 0, 0))
	window.blit(text, (1000, 30))
	goblin.draw(window)
	bob.drawplayer(window)

	for BULLET in bullets:
		BULLET.draw(window)
	pygame.display.update()


# MainLoop
bob = MyPlayer.Player(50, 406, 64, 64, 5, 10)
shootloop = 0
font = pygame.font.SysFont('comicsans', 30, True)
goblin = Enemy(length, 406, 64, 64, length- 64, 5)
bullets = []
run = True
while run:
	clock.tick(27)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	for bullet in bullets:
		if goblin.visible == True:
			if bullet.y + bullet.radius > goblin.hitbox[1] and bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] :
				if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
					goblin.hit()
					score += 1
					bullets.pop(bullets.index(bullet))
		if 0 < bullet.x < length:
			bullet.x += bullet.velocity
		else:
			bullets.pop(bullets.index(bullet))

	keys = pygame.key.get_pressed()

	if keys[pygame.K_SPACE]:
		shootloop += 1
		if bob.left:
			facing = -1
		else:
			facing = 1
		if len(bullets) < 8:
			if shootloop > 3:
				shellsound.play()
				bulletsound.play()

				bullets.append(Projectiles(round(bob.x + bob.width//2), round(bob.y + bob.height//2), 4, (255, 0, 0), 20, facing))
				shootloop = 0
	if keys[pygame.K_LEFT] and bob.x > bob.velocity:
		bob.x -= bob.velocity
		bob.left = True
		bob.right = False
		bob.standing = False
	elif keys[pygame.K_RIGHT] and bob.x < length - bob.velocity - bob.width:
		bob.x += bob.velocity
		bob.left = False
		bob.right = True
		bob.standing = False
	else:
		bob.standing = True
		bob.walkCount = 0
	if not bob.isjump:
		if keys[pygame.K_UP]:
			bob.isjump = True
			bob.walkCount = 0
	else:
		if bob.jumpCount >= -10:
			neg = 1
			if bob.jumpCount < 0:
				neg = -1
			bob.y -= (bob.jumpCount ** 2) * 0.5 * neg
			bob.jumpCount -= 1
		else:
			bob.isjump = False
			bob.jumpCount = 10

	draw()

pygame.quit()
