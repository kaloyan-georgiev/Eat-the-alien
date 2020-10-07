import pygame
from pygame.locals import *
from random import *


def main():
    pygame.init()

    clock = pygame.time.Clock()
    FPS = 60

    class Player():
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.speed = 2.5
            self.hitbox = (self.x + 10, self.y + 5, 50, 59)
            self.art = pygame.image.load("small_art\\alien2_1.png")
            self.isAlive = True
            self.stamina = 20
            self.score = 0
            self.turboModifier = 3

        def boundryCheck(self):
            if keys[pygame.K_LSHIFT] and self.stamina > 0:
                if self.x < 0:
                    self.x += self.speed * self.turboModifier
                elif self.x > (window_width - 64):
                    self.x -= self.speed * self.turboModifier
                if self.y < 0:
                    self.y += self.speed * self.turboModifier
                elif self.y > (window_height - 64):
                    self.y -= self.speed * self.turboModifier
            else:
                if self.x < 0:
                    self.x += self.speed
                elif self.x > (window_width - 64):
                    self.x -= self.speed
                if self.y < 0:
                    self.y += self.speed
                elif self.y > (window_height - 64):
                    self.y -= self.speed
        def turboMove(self):
                    if keys[pygame.K_w]:
                        self.y -= self.speed * self.turboModifier
                        self.stamina -= 1
                        self.art = pygame.image.load("small_art\\alien2_3.png")
                    if keys[pygame.K_a]:
                        self.x -= self.speed * self.turboModifier
                        self.stamina -= 1
                        self.art = pygame.image.load("small_art\\alien2_3.png")
                    if keys[pygame.K_s]:
                        self.y += self.speed * self.turboModifier
                        self.stamina -= 1
                        self.art = pygame.image.load("small_art\\alien2_3.png")
                    if keys[pygame.K_d]:
                        self.x += self.speed * self.turboModifier
                        self.stamina -= 1
                        self.art = pygame.image.load("small_art\\alien2_3.png")
        def movementCheck(self):
            if self.isAlive:
                self.art = pygame.image.load("small_art\\alien2_1.png")
                if self.stamina < 0:
                    self.stamina = 0
                if keys[pygame.K_LSHIFT] and self.stamina > 0:
                    self.turboMove()
                else:
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
            # pygame.draw.rect(window, RED, self.hitbox, 2)
            self.hitbox = (self.x + 10, self.y + 5, 50, 59)
        def scored(self):
            self.stamina += 30
            self.score += 1
        def hit(self):
            self.isAlive = False

    class Enemy():
        def __init__(self, speed, mature):
            self.x = randint(0, window_width - 64)
            self.y = randint(0, window_height - 64)
            self.speed = speed
            self.art = enemy_art
            self.dir = choice(["up", "down", "left", "right"])
            self.movements = 0
            self.hitbox = (self.x + 10, self.y + 5, 44, 54)
            self.hitCount = 0
            self.isMature = mature
            self.lifetime = 0

        def boundryCheck(self):
            if self.x < 0:
                self.x += self.speed
            elif self.x > (window_width - 64):
                self.x -= self.speed
            if self.y < 0:
                self.y += self.speed
            elif self.y > (window_height - 64):
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
            if self.isMature:
                self.art = enemy_art
                self.boundryCheck()
                self.randMovement()
                window.blit(self.art, (self.x, self.y))
                self.hitbox = (self.x + 10, self.y, 40, 60)
            else:
                self.art = enemy_immature
                self.lifetime += 1
                window.blit(self.art, (self.x, self.y))
                if self.lifetime == 120:
                    self.isMature = True

        def hit(self):
            enemies.remove(self)
            
    class Bait():
        def __init__(self, speed):
            self.x = randint(0, window_width)
            self.y = randint(0, window_height)
            self.width = 64
            self.height = 64
            self.speed = speed
            self.hitbox = [self.x + 20, self.y, 40, 40]
            self.art = pygame.image.load("small_art\\alien5.png")
            self.dir = choice(["up", "down", "left", "right"])
            self.movements = 0

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
            self.movements += randint(1, 4)
            if self.movements >= 32:
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
            self.randMovement()
            self.boundryCheck()
            if self.dir == "right":
                self.art = pygame.image.load("small_art\\alien5_1.png")
            elif self.dir == "left":
                self.art = pygame.image.load("small_art\\alien5.png")
            elif self.dir == "down":
                self.art = pygame.image.load("small_art\\alien5_2.png")
            window.blit(self.art, (self.x, self.y))
            self.hitbox = [self.x + 20, self.y, 40, 40]

    class Timer():
        def __init__(self):
            self.ticks = 0
            self.seconds = 0
        def tick(self):
            self.ticks += 1
            if self.ticks == FPS:
                self.seconds += 1
                self.ticks = 0
        def reset(self):
            self.ticks = 0
            self.seconds = 0

    class Particle():
        def __init__(self, x, y, art, time):
            self.x = x
            self.y = y
            self.art = pygame.image.load(art)
            self.time = time
        def draw(self):
            if(self.time > 0):
                window.blit(self.art, (self.x, self.y))
                self.time -= 1
            else:
                del self

    def player_enemy_hitCheck():
        for enemy in enemies:
            if (tentacles.hitbox[1] + tentacles.hitbox[3] > enemy.hitbox[1] and tentacles.hitbox[1] + tentacles.hitbox[3] < enemy.hitbox[1] + enemy.hitbox[3]) or (tentacles.hitbox[1] > enemy.hitbox[1] and tentacles.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3]):
                if (tentacles.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2] and tentacles.hitbox[0] > enemy.hitbox[0]) or (tentacles.hitbox[0] + tentacles.hitbox[2] > enemy.hitbox[0] and tentacles.hitbox[0] + tentacles.hitbox[2] < enemy.hitbox[0] + enemy.hitbox[3]):
                    if enemy.isMature:
                        tentacles.hit()
    def player_bait_hitCheck():
            if (tentacles.hitbox[1] + tentacles.hitbox[3] > bait.hitbox[1] and tentacles.hitbox[1] + tentacles.hitbox[3] < bait.hitbox[1] + bait.hitbox[3]) or (tentacles.hitbox[1] > bait.hitbox[1] and tentacles.hitbox[1] < bait.hitbox[1] + bait.hitbox[3]):
                if (tentacles.hitbox[0] < bait.hitbox[0] + bait.hitbox[2] and tentacles.hitbox[0] > bait.hitbox[0]) or (tentacles.hitbox[0] + tentacles.hitbox[2] > bait.hitbox[0] and tentacles.hitbox[0] + tentacles.hitbox[2] < bait.hitbox[0] + bait.hitbox[3]):
                    if tentacles.isAlive:
                        tentacles.scored()
                        return 1
                    return 0
    def trunctate(number, places):
        return int(number * 10 * places) / 10 * places

    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)

    window_width = 960
    window_height = 540

    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Eat the alien")
    #art
    enemy_art = pygame.image.load("small_art\\alien3.png")
    enemy_immature = pygame.image.load("small_art\\alien3_1.png")
    background = pygame.image.load("small_art\\background3.png")
    instructions = pygame.image.load("small_art\\instructions.png")
    bait_eat_particle = "small_art\\bait_eat1.png"
    tentacles_death_particle = "small_art\\tentacles_die.png"

    pygame.font.init()

   # enemy summon variables
    enemySpeed = 3
    maxEnemies = 8
    #ally starting speed
    bait_speed = 2
    # creating objects
    tentacles = Player(0, 0)
    bait = Bait(bait_speed)
    enemies = [Enemy(enemySpeed, False), Enemy(enemySpeed, False)]
    #particle list
    effects = []
    #hud font
    font1 = pygame.font.Font(None, 30)
    # timer variables
    gameTimer = Timer()
    afterDeath = Timer()
    summonTimer = Timer()
    # mainloop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        #display instructions

        # get list of pressed keys
        keys = pygame.key.get_pressed()
        window.blit(background, (0, 0))

        # summon enemies
        summonTimer.tick()
        if summonTimer.seconds == 10 and len(enemies) < maxEnemies:
            enemySpeed += 0.1
            enemies.append(Enemy(enemySpeed, False))
            summonTimer.reset()
        elif len(enemies) > maxEnemies and summonTimer.seconds == 1:
            summonTimer.reset()
            for enemy in enemies:
                enemy.speed += 0.001

        # draw Player
        if tentacles.isAlive:
            tentacles.draw()
        else:
            if afterDeath.ticks == 0:
                effects.append(Particle(tentacles.x, tentacles.y, tentacles_death_particle, 180))
            afterDeath.tick()
            if(afterDeath.seconds == 1):
                break
        # draw enemies
        for enemy in enemies:
            enemy.draw()
        #draw bait
        bait.draw()
        # check if there is a collision
        player_enemy_hitCheck()
        #check if the player scores
        if(player_bait_hitCheck()):
            effects.append(Particle(bait.x, bait.y, bait_eat_particle, 180))
            bait_speed += 0.1
            bait = Bait(bait_speed)
        #draw particles
        for particle in effects:
            if particle:
                particle.draw()
        # display the timer
        if tentacles.isAlive:
            gameTimer.tick()
        #display the timer box
        timer_box = font1.render("Your time is {0} seconds".format(gameTimer.seconds), False, RED)
        window.blit(timer_box, (window_width - timer_box.get_width(), 1))
        # display the score box
        score_box = font1.render("Score: {0}".format(tentacles.score), False, RED)
        window.blit(score_box, (1, 1))
        #display stamina
        stamina_box = font1.render("Stamina: {0}".format(tentacles.stamina), True, BLUE)
        window.blit(stamina_box, (window_width / 2 - stamina_box.get_width() / 2, 1))
        #update screen
        pygame.display.flip()
        clock.tick(FPS)
    #Aftergame screen
    afterGameFont = pygame.font.Font(None, 60)
    afterGameText2 = afterGameFont.render("Your time was {0} seconds".format(gameTimer.seconds), True, RED)
    afterGameText1 = afterGameFont.render("You Lost! Better luck next time", True, RED)
    afterGameText3 = afterGameFont.render("You killed {0} mosquitoes".format(tentacles.score), True, RED)
    afterGameText4 = afterGameFont.render("Net score: {0}".format(trunctate((tentacles.score * 10 / gameTimer.seconds), 2)), True, BLUE)
    window.fill(BLACK)
    window.blit(afterGameText1, (window_width / 2 - afterGameText1.get_width() / 2, 160))
    window.blit(afterGameText2, (window_width / 2 - afterGameText2.get_width() / 2, 230))
    window.blit(afterGameText3, (window_width / 2 - afterGameText3.get_width() / 2, 300))
    window.blit(afterGameText4, (window_width / 2 - afterGameText4.get_width() / 2, 370))
    pygame.display.flip()
    pygame.time.delay(3000)
    main()


if __name__ == "__main__":
    main()
