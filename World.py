import Blocks


class World:
    # Размер блока, Высота и Ширина мира (в блоках)
    size = Blocks.Block.size
    width = 50
    height = 30

    def __init__(self, screen):
        self.world = list()
        self.screen = screen
        self.gen()

    # Генерация мира

    def gen(self):
        # Мир заполняется блоками воздуха

        self.world = [[Blocks.Block for y in range(self.height)] for x in range(self.width)]

        # Мир заполняется воздухом

        for x in range(self.width):
            for y in range(self.height):
                self.world[x][y] = Blocks.Air(x, y)

        # Часть мира заполняется землёй

        for x in range(self.width):
            for y in range(self.height // 2, self.height):
                self.world[x][y] = Blocks.Dirt(x, y)

    # Метод отрисовки

    def show(self):
        for x in range(self.width):
            for y in range(self.height):
                block = self.world[x][y]
                block.show(self.screen, x * block.size, y * block.size)
