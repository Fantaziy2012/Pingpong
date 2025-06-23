import pygame
import sys
pygame.init()
# Создаём пустой экран
WIDTH = 700 
HIGHT = 500
main_win = pygame.display.set_mode((WIDTH, HIGHT))
pygame.display.set_caption('Пинпонг')
# Игровой таймер
clock = pygame.time.Clock()
fps = 60
# Задаём фон сцены
img = pygame.image.load('дружок1.png')
newimg = pygame.transform.scale(img,(700,500))
class Gamesprite(pygame.sprite.Sprite):
    def __init__(self,playerimage, playerx, playery, playerspeed, sizex, sizey):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(playerimage),(sizex, sizey))
        self.speed = playerspeed
        self.rect = self.image.get_rect()
        self.rect.x = playerx
        self.rect.y = playery
    def reset(self):
        main_win.blit(self.image, (self.rect.x, self.rect.y))
class Player(Gamesprite):
    def update_r(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP ] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN ] and self.rect.y <= HIGHT - 60:
            self.rect.y += self.speed
    def update_l(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w ] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s ] and self.rect.y <= HIGHT - 60:
            self.rect.y += self.speed
playergena = Player('гена.png', 10, 200, 4, 80, 100)
playermalash = Player('малыш.png', 620, 200, 4, 80, 100)
spriteball = Gamesprite('дружок.png', 200, 200, 4, 50,50)
# Запуск игрового цикл
finish = False
speed_x = 3
speed_y = 3
pygame.font.init()
font1 = pygame.font.Font(None, 50)
losegena = font1.render(
    'Player Gena lose!', True, (255, 0, 0)
)
# Аналогичная надпись для Малыша
losemalash = font1.render(
    'Player Malash lose!', True, (255, 0, 0)
)
restart = font1.render(
    'Press e for restart', True, (255, 255, 0)
)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                finish = False
                playergena = Player('гена.png', 10, 200, 4, 80, 100)
                playermalash = Player('малыш.png', 620, 200, 4, 80, 100)
                spriteball = Gamesprite('дружок.png', 200, 200, 4, 50,50)
    if not finish:
        main_win.fill((255,255,255))
        main_win.blit(newimg, (0,0))
        spriteball.rect.x += speed_x
        spriteball.rect.y += speed_y
        if spriteball.rect.y > HIGHT - 50 or spriteball.rect.y < 0:
            speed_y *= -1
        if pygame.sprite.collide_rect(playergena, spriteball) or pygame.sprite.collide_rect(playermalash, spriteball):
            speed_x *= -1
        playergena.update_l()
        playermalash.update_r()
        playergena.reset()
        playermalash.reset()
        spriteball.reset()
        if spriteball.rect.x < 0:
            finish = True
            main_win.blit(losegena,(200, 200))
            main_win.blit(restart, (200, 300))
            # Аналогичное условие для проигрыша Малыша
        if spriteball.rect.x > WIDTH:
            finish = True
            main_win.blit(losemalash,(200, 200))
            main_win.blit(restart, (200, 300))
        pygame.display.update()
    clock.tick(fps)
