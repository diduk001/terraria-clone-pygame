import pygame
import Sprites
from pygame import Rect

blocks_sprites = pygame.sprite.Group()


class Block:
    size = 20

    def __init__(self, id, x, y):
        # id блока и его координаты в блоках;

        self.id = id
        self.x = x
        self.y = y

        # Имя блока
        # Его цвет отрисовки
        # Разрушаемость
        # Проходимость
        # Прочность блока добыче: киркой, топором
        # id итема, выпадающего при разрушении

        self.name = str()
        self.color = tuple()
        self.is_breakable = bool()
        self.is_passable = bool()
        self.solidity_pickaxe = int()
        self.solidity_axe = int()
        self.drop = int()

        # Спрайт блока
        self.image = pygame.Surface((self.size, self.size))
        self.sprite = Sprites.BlockSprite(self)

    # Функция отрисоки;

    def show(self, screen):
        if self.color == ():
            return

        pygame.draw.rect(screen, self.color,
                         Rect(self.x * self.size, self.y * self.size, self.size, self.size))

    # Функция разрушения;

    def destroy(self, screen):
        pass

    def __str__(self):
        return f"{self.name} Block on {self.x}, {self.y}"

    def __repr__(self):
        return self.__str__()


# Блок Воздуха;

class Air(Block):
    def __init__(self, x, y):
        super().__init__(0, x, y)

        self.name = "Air"
        self.color = (0, 0, 255)
        self.is_breakable = False
        self.is_passable = True
        self.solidity_pickaxe = -1
        self.solidity_axe = -1

        self.image.fill(self.color)
        self.sprite.update_image(self.image)


# Блок Кореной Породы (JJBA: Diamond Is Unbreakable);

class JoJoStone(Block):
    def __init__(self, x, y):
        super().__init__(1, x, y)

        self.name = "JoJoStone"
        self.color = (106, 13, 173)
        self.is_breakable = False
        self.is_passable = False
        self.solidity_pickaxe = 1000
        self.solidity_axe = 1000

        self.image.fill(self.color)
        self.sprite.update_image(self.image)


# Блок Грязи;

class Dirt(Block):
    def __init__(self, x, y):
        super().__init__(2, x, y)

        self.name = "Dirt"
        self.color = (77, 38, 0)
        self.is_breakable = True
        self.is_passable = False
        self.solidity_pickaxe = 25
        self.solidity_axe = 25
        self.drop = 0

        self.image.fill(self.color)
        self.sprite.update_image(self.image)


# Блок Камня;

class Stone(Block):
    def __init__(self, x, y):
        super().__init__(3, x, y)

        self.name = "Stone"
        self.color = (107, 107, 71)
        self.is_breakable = True
        self.is_passable = False
        self.solidity_pickaxe = 35
        self.solidity_axe = 1000
        self.drop = 1

        self.image.fill(self.color)
        self.sprite.update_image(self.image)


# Блок Медной Руды

class CopperOre(Block):
    def __init__(self, x, y):
        super().__init__(4, x, y)

        self.name = "Copper Ore"
        self.color = (72, 45, 20)
        self.is_breakable = True
        self.is_passable = False
        self.solidity_pickaxe = 50
        self.solidity_axe = 1000
        self.drop = 2

        self.image.fill(self.color)
        self.sprite.update_image(self.image)


# Блок Железной Руды

class IronOre(Block):
    def __init__(self, x, y):
        super().__init__(5, x, y)

        self.name = "Iron Ore"
        self.color = (203, 205, 205)
        self.is_breakable = True
        self.is_passable = False
        self.solidity_pickaxe = 50
        self.solidity_axe = 1000
        self.drop = 3

        self.image.fill(self.color)
        self.sprite.update_image(self.image)


# Блок Дерева

class Wood(Block):
    def __init__(self, x, y):
        super().__init__(6, x, y)

        self.name = "Wood"
        self.color = (133, 94, 66)
        self.is_breakable = True
        self.is_passable = True
        self.solidity_pickaxe = 50
        self.solidity_axe = 20
        self.drop = 4

        self.image.fill(self.color)
        self.sprite.update_image(self.image)


# Блок Листвы

class Foliage(Block):
    def __init__(self, x, y):
        super().__init__(7, x, y)

        self.name = "Foliage"
        self.color = (80, 200, 120)
        self.is_breakable = True
        self.is_passable = True
        self.solidity_pickaxe = 5
        self.solidity_axe = 5

        self.image.fill(self.color)
        self.sprite.update_image(self.image)


# Блок Древесины

class TimberBlock(Block):
    def __init__(self, x, y):
        super().__init__(8, x, y)

        self.name = "Timber Block"
        self.color = (150, 75, 0)
        self.is_breakable = True
        self.is_passable = False
        self.solidity_pickaxe = 50
        self.solidity_axe = 20
        self.drop = 4

        self.image.fill(self.color)
        self.sprite.update_image(self.image)


# Блок Верстака

class WorkbenchBlock(Block):
    def __init__(self, x, y):
        super().__init__(9, x, y)

        self.name = "Placed Workbench"
        self.color = (252, 211, 59)
        self.is_breakable = True
        self.is_passable = True
        self.solidity_pickaxe = 50
        self.solidity_axe = 20
        self.drop = 5

        self.image.fill(self.color)
        self.sprite.update_image(self.image)


# Блок Печи

class FurnaceBlock(Block):
    def __init__(self, x, y):
        super().__init__(10, x, y)

        self.name = "Placed Furnace"
        self.color = (112, 128, 144)
        self.is_breakable = True
        self.is_passable = True
        self.solidity_pickaxe = 30
        self.solidity_axe = 1000
        self.drop = 6

        self.image.fill(self.color)
        self.sprite.update_image(self.image)
