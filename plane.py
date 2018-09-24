import pygame
from plane_sprites import *

#游戏初始化
pygame.init()

screen = pygame.display.set_mode((SCREEN_RECR.width,SCREEN_RECR.height))
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))

hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(180,500))
pygame.display.update()

#我方飞机位置区域大小
hero_rect = pygame.Rect(180,500,102,126)

#创建时钟
clock = pygame.time.Clock()

#创建精灵对象
enemy1 = GameSprite("./images/enemy1.png")
enemy2 = GameSprite("./images/enemy1.png",2)
#创建敌机精灵组
enemy_group = pygame.sprite.Group(enemy1,enemy2)

while True:

    clock.tick(60)

    #监听事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT
            exit()

    if hero_rect.y == -126:
        hero_rect.y = 700

    hero_rect.y -= 1
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    enemy_group.update()
    enemy_group.draw(screen)

    pygame.display.update()

    pass

#游戏结束
pygame.quit()