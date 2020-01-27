import pygame
import Blocks


class World:

    # Высота и Ширина мира (в блоках)

    width = 200
    height = 200

    def __init__(self, screen):
        self.world = list()
        self.screen = screen
        self.gen()

    # Генерация мира

    def gen(self):
        # Мир заполняется блоками воздуха

        self.world = [[Blocks.Air(x, y) for x in range(self.width)] for y in range(
            self.height)]

        # Часть мира заполняется землёй

        for y in range(self.height // 2, self.height):
            for x in range(self.width):
                self.world[y][x] = Blocks.Dirt(x, y)

    # Функция отрисовки

    def show(self):
        for row in self.world:
            for block in row:
                block.show(self.screen)
