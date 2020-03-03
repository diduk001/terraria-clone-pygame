import Blocks
import Generation
import Sprites


class World:
    # Размер блока, Высота и Ширина мира (в блоках)
    size = Blocks.Block.size
    width = 100
    height = 30

    def __init__(self, screen):
        self.world = list()
        self.screen = screen
        self.gen()

    # Генерация мира

    def gen(self):
        # Генерируем мир
        self.world = Generation.generate(self.width, self.height)

    # Функция отрисовки

    def show(self):
        Sprites.blocks_sprites.draw(self.screen)
        Sprites.player_sprite.draw(self.screen)
        Sprites.item_sprites.draw(self.screen)

    def update(self):
        for x, y in Blocks.deleted:
            self.world[x][y] = Blocks.Air(x, y)
        Blocks.deleted = []
        for sprite in Sprites.item_sprites:
            sprite.move()

    def get_block_coords(self, x, y):
        return x // Blocks.Block.size, y // Blocks.Block.size

    def get_block(self, x, y):
        x_block, y_block = self.get_block_coords(x, y)
        return self.world[x_block][y_block]

    def is_block(self, x, y, block):
        x_block, y_block = self.get_block_coords(x, y)
        return self.world[x_block][y_block] == block(x, y)
