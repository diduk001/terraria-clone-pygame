import pygame
from pygame.rect import Rect


class Player:
    def __init__(self, x, y):
        # Координаты по x и по y

        self.x = x
        self.y = y

        # Размкры по x, y

        self.x_size = 10
        self.y_size = 20

        # Скорость по x вправо (не меньше 0), по x влево (не меньше 0), по y

        self.vx_right = int()
        self.vx_left = int()
        self.vy = int()

        # Ускорение по x (при ходьбе, не меньше 0), Сила трения (не больше 0)

        self.ax = int()
        self.friction = int()

        # Ускорение по y (при прыжке, не больше 0), Ускорение свободного падения (не меньше 0)

        self.ay = int()
        self.gravity = int()

        # Максимальная допустимая скорость по x, минимальная скорость по y, максимальная скорость
        # по y соответственно

        self.vx_max = int()
        self.vy_min = int()
        self.vy_max = int()

    # Скорость по x не может быть меньше 0 и не может быть больше vx_max

    # Движение влево

    def move_left(self):
        self.vx_right = 0
        self.vx_left = min(self.vx_left, self.vx_left + self.ax)

    # Движение вправо

    def move_right(self):
        self.vx_left = 0
        self.vx_right = min(self.vx_right, self.vx_right + self.ax)

    # Прыжок

    def jump(self):
        self.vy = max(self.vy - self.ay, 0)

    # Обновление скоростей

    def update(self):
        self.vy -= self.gravity
        self.vx_left = max(self.vx_left, self.vx_left - self.friction)
        self.vx_right = max(self.vx_right, self.vx_right - self.friction)

    # Обновление координат

    def move(self):
        self.y += self.gravity
        self.x += self.vx_right
        self.x -= self.vx_left

    # Отрисовка персонажа

    def show(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), Rect(self.x, self.y, self.x_size, self.y_size))
