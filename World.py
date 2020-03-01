import Sprites
import Blocks
import Generation

class World:
    # Высота и Ширина мира (в блоках)
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

        # self.world = [[Blocks.Air(x, y) for y in range(self.height)] for x in range(self.width)]
        # Часть мира заполняется землёй
        # for y in range(self.height // 2, self.height):
        #     for x in range(self.width):
        #         self.world[x][y] = Blocks.Dirt(x, y)
        self.world = Generation.generate(self.width, self.height)
        # self.world[31][14] = Blocks.Dirt(31, 14)
        # self.world[11][14] = Blocks.Dirt(11, 14)
        # self.world[25][11] = Blocks.Dirt(25, 11)

    # Функция отрисовки

    def show(self):
        Sprites.blocks_sprites.draw(self.screen)

    def get_block_coords(self, x, y):
        return x // Blocks.Block.size, y // Blocks.Block.size

    def get_block(self, x, y):
        x_block, y_block = self.get_block_coords(x, y)
        return self.world[x_block][y_block]

    def is_block(self, x, y, block):
        x_block, y_block = self.get_block_coords(x, y)
        return self.world[x_block][y_block] == block(x, y)