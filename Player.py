import pygame
from Blocks import Block


class Player:
    def __init__(self, x, y):
        # Координаты игрока по x, y на экране в пикселях

        self.x = x
        self.y = y

        # Ширина, Высота игрока
        self.width = Block.size
        self.height = 2 * Block.size

        # Скорость игрока по x, y

        self.vx = 0
        self.vy = 0

        # Кол-во очков здоровья игрока

        self.hp = int()

        # Скорость прыжка игрока

        self.jump_speed = -30

        # Направление игрока, False - влево, True - вправо

        self.direction = bool()

        # Кол-во урона от руки

        self.attack = int()

        # Значение изменения скорости

        self.speed = 10

    # Метод передвижения

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.vy < 0:
            self.vy += 5

    # Метод ускорения на x

    def speed_x(self, x):
        self.vx += x

    # Метод падения

    def fall(self, world):
        bx, by = self.block_now()
        by += 2
        if world[bx][by].solidity_pickaxe == -1 and self.vy == 0:
            self.vy -= self.jump_speed // 3
        elif world[bx][by].solidity_pickaxe != -1:
            self.vy = 0

    # Метод прыжка

    def jump(self):
        if self.vy == 0:
            self.vy += self.jump_speed

    # Метода перевода из координат экрана в блоки

    def block_now(self):
        return self.x // Block.size, self.y // Block.size

    # Метод пересечения

    def collide(self):
        pass

    # Метод отрисовки

    def show(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

    # Метод получения урона

    def damage(self, x):
        self.hp -= x

    # Проверка на то, жив ли игрок

    def is_live(self):
        if self.hp > 0:
            return True
        return False
