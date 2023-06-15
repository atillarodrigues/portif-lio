import pygame, random


WIDTH = 1200
HEIGTH = 600
SPEED = 10
GAME_SPEED = 10
GROUND_WIDTH = 2 * WIDTH
GROUND_HEIGTH = 30
FLY = 30


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_run = [pygame.image.load('sprites/Run__000.png').convert_alpha(),
                          pygame.image.load('sprites/Run__001.png').convert_alpha(),
                          pygame.image.load('sprites/Run__002.png').convert_alpha(),
                          pygame.image.load('sprites/Run__003.png').convert_alpha(),
                          pygame.image.load('sprites/Run__004.png').convert_alpha(),
                          pygame.image.load('sprites/Run__005.png').convert_alpha(),
                          pygame.image.load('sprites/Run__006.png').convert_alpha(),
                          pygame.image.load('sprites/Run__007.png').convert_alpha(),
                          pygame.image.load('sprites/Run__008.png').convert_alpha(),
                          pygame.image.load('sprites/Run__009.png').convert_alpha(),]
        self.image_fall = pygame.image.load('sprites/Fall.png').convert_alpha()
        self.image = pygame.image.load('sprites/Run__000.png').convert_alpha()
        self.rect = pygame.Rect(100, 100, 100, 100)
        self.current_image = 0

    def update(self, *args):
        def move_player(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_d]:
                self.rect[0] += GAME_SPEED
            if key[pygame.K_a]:
                self.rect[0] -= GAME_SPEED
            self.current_image = (self.current_image + 1) % 10
            self.image = self.image_run[self.current_image]
            self.image = pygame.transform.scale(self.image,[100, 100])
        move_player(self)
        self.rect[1] += SPEED

        def fly(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                self.rect[1] -= FLY
                self.image = pygame.image.load('sprites/Fly.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, [100, 100])
                # print('fly')
        fly(self)

        def fall(self):
            key = pygame.key.get_pressed()
            if not pygame.sprite.groupcollide(playerGroup, groundGroup, False, False) and not key[pygame.K_SPACE]:
                self.image = self.image_fall
                self.image = pygame.transform.scale(self.image, [100, 100])
                # print('falling')
        fall(self)

class Ground(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprites/ground.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (GROUND_WIDTH, GROUND_HEIGTH))
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = HEIGTH - GROUND_HEIGTH

    def update(self, *args):
        self.rect[0] -= GAME_SPEED

class Obstacles(pygame.sprite.Sprite):
    def __init__(self, xpos, ysize):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/Box.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(100, 100, 100, 100)
        self.rect[0] = xpos
        self.mask = pygame.mask.from_surface(self.image)
        self.rect[1] = HEIGTH - ysize

    def update(self, *args):
        self.rect[0] -= GAME_SPEED
        # print('obstacle')

class Coins(pygame.sprite.Sprite):
    def __init__(self, xpos, ysize):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/coin.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, [40, 40])
        self.rect = pygame.Rect(100, 100, 20 , 20)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect[0] = xpos
        self.rect[1] = HEIGTH - ysize

    def update(self, *args):
        self.rect[0] -= GAME_SPEED
        # print('coin')

def get_random_obstacles(xpos):
    size = random.randint(120, 600)
    box = Obstacles(xpos, size)
    return box
def get_random_coins(xpos):
    size = random.randint(120,600)
    coin = Coins(xpos, size)
    return coin

def is_off_scream(sprite):
    return sprite.rect[0] < -(sprite.rect[2])

pygame.init()
game_window = pygame.display.set_mode([WIDTH, HEIGTH])
pygame.display.set_caption('Jogo TESTE')

BACKGROUND = pygame.image.load('sprites/background_03.jpg')
BACKGROUND = pygame.transform.scale(BACKGROUND,[WIDTH, HEIGTH])

playerGroup = pygame.sprite.Group()
player = Player()
playerGroup.add(player)

groundGroup = pygame.sprite.Group()
for i in range(2):
    ground = Ground(WIDTH * i)
    groundGroup.add(ground)

coinsGroup = pygame.sprite.Group()
for i in range(2):
    coin = get_random_coins(WIDTH * i + 1000)
    coinsGroup.add(coin)

obstacleGroup = pygame.sprite.Group()
for i in range(2):
    obstacle = get_random_obstacles(WIDTH * i + 1000)
    obstacleGroup.add(obstacle)

gameloop = True
def draw():
    playerGroup.draw(game_window)
    groundGroup.draw(game_window)
    obstacleGroup.draw(game_window)
    coinsGroup.draw(game_window)

def update():
    playerGroup.update()
    groundGroup.update()
    obstacleGroup.update()
    coinsGroup.update()

clock = pygame.time.Clock()
placar = 0


while gameloop:
    game_window.blit(BACKGROUND, (0, 0))
    font = pygame.font.SysFont('Arial', 30)
    text = font.render('Placar', True, [255, 255, 255])
    game_window.blit(text, [1100, 20])
    contador = font.render(f'{placar}', True, [255, 255, 255])
    game_window.blit(contador, [1125, 50])
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    if is_off_scream(groundGroup.sprites()[0]):
        groundGroup.remove(groundGroup.sprites()[0])
        newGround = Ground(WIDTH - 20)
        groundGroup.add(newGround)

    if is_off_scream(obstacleGroup.sprites()[0]):
        obstacleGroup.remove(obstacleGroup.sprites()[0])
        newObstacle = get_random_obstacles(WIDTH * 1.5)
        # newObstacle1 = get_random_obstacles(WIDTH * 4)
        # obstacleGroup.add(newObstacle1)
        obstacleGroup.add(newObstacle)
        newCoin1 = get_random_coins(WIDTH * 2)
        newCoin2 = get_random_coins(WIDTH * 2.2)
        newCoin3 = get_random_coins(WIDTH * 2.4)
        newCoin4 = get_random_coins(WIDTH * 2.6)
        newCoin5 = get_random_coins(WIDTH * 2.8)
        coinsGroup.add(newCoin1)
        coinsGroup.add(newCoin2)
        coinsGroup.add(newCoin3)
        coinsGroup.add(newCoin4)
        coinsGroup.add(newCoin5)

    if pygame.sprite.groupcollide(playerGroup, groundGroup,False, False):
        SPEED = 0
        # print('colission')
    else:
        SPEED = 10

    if pygame.sprite.groupcollide(playerGroup, coinsGroup, False, True):
        placar += 1

    if placar % 5 == 0 and placar != 0:
        GAME_SPEED += 0.02
        print('GAMESPEED ALTERADA')

    if pygame.sprite.groupcollide(playerGroup, obstacleGroup, False, False):
        break

    update()
    draw()
    pygame.display.update()