import random
import pygame

SCREEN_RECR = pygame.Rect(0,0,480,700)
#刷新帧率
FRAME_PRE_SEC = 60
#创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
#发射子弹的事件
OPEN_FIRE = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
    def __init__(self,image_name,speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
    def update(self):
        #垂直方向上的移动速度
        self.rect.y += self.speed

class Background(GameSprite):
    def update(self):
        super().update()

        if self.rect.y >= SCREEN_RECR.height:
            self.rect.y = -SCREEN_RECR.height


class Enemy(GameSprite):
    def __init__(self):
        super().__init__("./images/enemy1.png")
        self.speed = random.randint(1,3)
        self.rect.bottom = 0
        self.rect.x = random.randint(0,480-57)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECR.height:
            pass
        if self.rect.y > SCREEN_RECR.height:
            self.kill()
    def __del__(self):
        print("敌机被销毁：%s" %self.rect)

class Hero(GameSprite):
    def __init__(self):
        super().__init__("./images/me1.png",0)
        self.rect.centerx = SCREEN_RECR.centerx
        self.rect.bottom = SCREEN_RECR.bottom - 70

        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_RECR.right:
            self.rect.right = SCREEN_RECR.right

    def fire(self):
        print("发射子弹")
        for i in (0,1,2):
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y - i* 20
            bullet.rect.centerx = self.rect.centerx
            self.bullets.add(bullet)

class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./images/bullet1.png",-2)

    def update(self):
        if self.rect.bottom <= 0:
            self.kill()

        self.rect.y += self.speed

    def __del__(self):
        print("子弹被销毁：%s" % self.rect)

