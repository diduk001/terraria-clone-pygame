import pygame
import Sprites
import Blocks


class World:

    # Высота и Ширина мира (в блоках)
    size = Blocks.Block.size
    width = 30
    height = 26

    def __init__(self, screen):
        self.world = list()
        self.screen = screen
        self.gen()

    # Генерация мира

    def gen(self):
        # Мир заполняется блоками воздуха

        self.world = [[Blocks.Air(x, y) for y in range(self.height)] for x in range(self.width)]

        # Часть мира заполняется землёй
        for y in range(self.height // 2, self.height):
            for x in range(self.width):
                self.world[x][y].sprite.delete()
                if (x + y) % 2 == 0:
                    self.world[x][y] = Blocks.Dirt(x, y)
                else:
                    self.world[x][y] = Blocks.Stone(x, y)
        self.world[6][10] = Blocks.Dirt(6, 10)
        self.world[11][11] = Blocks.Dirt(11, 11)
        self.world[25][7] = Blocks.Dirt(25, 7)

    # Функция отрисовки

    def show(self):
        Sprites.blocks_sprites.draw(self.screen)
        Sprites.mobs_sprites.draw(self.screen)