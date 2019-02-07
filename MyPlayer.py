import pygame

walkright = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]

walkleft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]


class Player(object):
    def __init__(self, x, y, width, height, velocity, jumpCount):
        self.x = 50
        self.y = 406
        self.width = 64
        self.height = 64
        self.velocity = velocity
        self.isjump = False
        self.jumpCount = jumpCount
        self.left = False
        self.right = True
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 20, self.y + 15, self.width // 2 - 10, int(self.height / 2))

    def drawplayer(self, window):
        # global walkCount
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not self.standing:
            if self.left and self.right == False:
                window.blit(walkleft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            if self.right and self.left == False:
                window.blit(walkright[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                window.blit(walkright[0], (self.x, self.y))
            else:
                window.blit(walkleft[0], (self.x, self.y))
        self.hitbox = (self.x + 20, self.y + 20, self.width // 2 - 10, int(self.height / 1.5))
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
