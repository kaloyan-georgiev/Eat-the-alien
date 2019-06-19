import pygame, sys
from pygame.locals import *
from random import *



def main():
    pygame.init()

    clock = pygame.time.Clock()
    FPS = 30

    class Player(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.speed = 5
            self.hitbox = (self.x + 10, self.y + 5, 50, 59)
            self.art = pygame.image.load("alien2_1.png")
            self.isAlive = True
        
        def boundryCheck(self):
            if self.x < 0:
                self.x += self.speed
            elif self.x > (window_width - 64):
                self.x -= self.speed
            if self.y < 0:
                self.y += self.speed
            elif self.y > (window_height - 64):
                self.y -= self.speed

        def movementCheck(self):
            if keys[pygame.K_w]:
                self.y -= self.speed
            if keys[pygame.K_a]:
                self.x -= self.speed
            if keys[pygame.K_s]:
                self.y += self.speed
            if keys[pygame.K_d]:
                self.x += self.speed

        def draw(self):
            self.boundryCheck()
            self.movementCheck()
            window.blit(self.art, (self.x, self.y))
            self.hitbox = (self.x + 10, self.y + 5, 50, 59)

        def hit(self):
            self.isAlive = False


    class Enemy():
        def __init__(self, width, height, speed):
            self.width = width
            self.height = height
            self.x = randint(0, window_width - self.width)
            self.y = randint(0, window_height - self.height)
            self.speed = speed
            self.art = enemy_art
            self.dir = choice(["up", "down", "left", "right"])
            self.movements = 0
            self.hitbox = (self.x + 5, self.y, 50, 60)
            self.hitCount = 0

        def boundryCheck(self):
            if self.x < 0:
                self.x += self.speed
            elif self.x > (window_width - self.width):
                self.x -= self.speed
            if self.y < 0:
                self.y += self.speed
            elif self.y > (window_height - self.height):
                self.y -= self.speed

        def randMovement(self):           
            if self.dir == "left":
                self.x -= self.speed
            elif self.dir == "right":
                self.x += self.speed
            elif self.dir == "up":
                self.y -= self.speed
            elif self.dir == "down":
                self.y += self.speed
            self.movements += randint(1, 2)
            if self.movements >= 16:
                if self.dir == "up":
                    self.dir = choice(["up", "left", "right"])
                elif self.dir == "right":
                    self.dir = choice(["up", "down", "right"])
                elif self.dir == "left":
                    self.dir = choice(["up", "left", "down"])
                elif self.dir == "down":
                    self.dir = choice(["down", "left", "right"])
                self.movements = 0

        def draw(self):
            self.boundryCheck()
            self.randMovement()
            window.blit(self.art, (self.x, self.y))
            self.hitbox = (self.x + 10, self.y, 40, 60)
        
        def hit(self):
            print(self.hitCount)
            self.hitCount +=1

    def hitCheck():
        for enemy in enemies:
            if (tentacles.hitbox[1] + tentacles.hitbox[3] > enemy.hitbox[1] and tentacles.hitbox[1] + tentacles.hitbox[3] < enemy.hitbox[1] + enemy.hitbox[3]) or (tentacles.hitbox[1] > enemy.hitbox[1] and tentacles.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3]):
                if (tentacles.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2] and tentacles.hitbox[0] > enemy.hitbox[0]) or (tentacles.hitbox[0] + tentacles.hitbox[2] > enemy.hitbox[0] and tentacles.hitbox[0] + tentacles.hitbox[2] < enemy.hitbox[0] + enemy.hitbox[3]):
                    tentacles.hit()

    RED = (255, 0, 0)

    window_width = 960
    window_height = 540

    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Eat the alien")
    enemy_art = pygame.image.load("alien3.png")
    background = pygame.image.load("background3.png")

    pygame.font.init()

    # creating objects
    tentacles = Player(0, 0)
    enemy1 = Enemy(64, 64, 7)
    enemy2 = Enemy(64, 64, 7)
    enemies = [enemy1, enemy2]

    font1 = pygame.font.Font(None, 30)

    #enemy summon variables
    summonTime = 0
    enemySpeed = 7

    #timer variables
    timerTicks = 0
    timerSeconds = 0

    #mainloop
    while tentacles.isAlive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                tentacles.isAlive = False

        #get list of pressed keys
        keys = pygame.key.get_pressed()
        
        window.blit(background, (0, 0))

        #draw Player
        tentacles.draw()

        #summon enemies
        summonTime += 1
        if summonTime == 300 and len(enemies) <= 20:
            enemies.append(Enemy(64, 64, enemySpeed))
            summonTime = 0
            enemySpeed += 0.1
        elif len(enemies) > 20:
            for enemy in enemies:
                enemy.speed += 0.001

        #draw enemies
        for enemy in enemies:
            enemy.draw()

        #check if there is a collision
        hitCheck()

        #display the timer
        timerTicks += 1
        if timerTicks == 30:
            timerSeconds +=1
            timerTicks = 0
        timer = font1.render("Your time is " + str(timerSeconds) + " seconds", False, RED)
        window.blit(timer, (window_width - timer.get_width(), 1))

        pygame.display.flip()
        clock.tick(FPS)

    afterGameFont = pygame.font.Font(None, 60)
    afterGameText2 = afterGameFont.render("Your time was " + str(timerSeconds) + " seconds", True, RED)
    afterGameText1 = afterGameFont.render("You Lost! Better luck next time", True, RED)
    black = (0, 0, 0)        
    window.fill(black)
    window.blit(afterGameText1, (window_width / 2 - afterGameText1.get_width() / 2, 200))
    window.blit(afterGameText2, (window_width / 2 - afterGameText2.get_width() / 2, 270))
    pygame.display.flip()
    pygame.time.delay(3000)
    main()
    
if __name__ == "__main__":
    main()