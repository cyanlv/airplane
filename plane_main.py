import pygame
from plane_sprites import *

#主程序
class PlaneGame():

    def __init__(self):
        print("游戏初始化")

        self.screen = pygame.display.set_mode((SCREEN_RECR.width,SCREEN_RECR.height))
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
        pygame.time.set_timer(OPEN_FIRE,400)

    def __create_sprites(self):
        bg1 = Background("./images/background.png")
        bg2 = Background("./images/background.png")
        bg2.rect.y = -bg2.rect.height
        self.back_group = pygame.sprite.Group(bg1,bg2)

        self.enemy_group = pygame.sprite.Group()

        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print("出现敌机")
                enemy = Enemy()

                self.enemy_group.add(enemy)

            elif event.type == OPEN_FIRE:
                self.hero.fire()
            # elif event.type == pygame.KEYDOWN and pygame.K_RIGHT:
            #     print("按下右键")
        keys_presswd = pygame.key.get_pressed()
        if keys_presswd[pygame.K_RIGHT]:
            self.hero.rect.x += 3
        elif keys_presswd[pygame.K_LEFT]:
            self.hero.speed = -3
        else:
            self.hero.speed = 0

    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)

        enemies = pygame.sprite.groupcollide(self.hero_group,self.enemy_group,True,True)
        if len(enemies) > 0:
            self.hero.kill()
            self.__game_over()
        pass

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()

    def start_game(self):
        print("游戏开始")

        while True:
            pass
            #1设置刷新帧率
            self.clock.tick(60)
            #2事件监听
            self.__event_handler()
            #3碰撞检测
            self.__check_collide()
            #4更新精灵组
            self.__update_sprites()
            #5更新显示
            pygame.display.update()

if __name__ == '__main__':

    game = PlaneGame()
    game.start_game()