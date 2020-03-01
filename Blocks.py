import pygame
import Sprites
import Items
from pygame import Rect

deleted = []

class Block:
    size = 32

    def __init__(self, block_id, x, y):
        self.block_id = block_id
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

        pygame.draw.rect(screen, self.color, Rect(self.x * self.size, self.y * self.size, self.size, self.size))

    # Метод разрушения;
    def destroy(self, delete=True):
        self.sprite.delete()
        if not self.is_passable:
            self.drop.drop(self.x * self.size, self.y * self.size)
        if delete:
            deleted.append((self.x, self.y))

    def mine(self, x):
        self.solidity_pickaxe -= x
        if self.is_breakable and self.solidity_pickaxe <= 0:
            self.destroy()

    def chop(self, x):
        self.solidity_axe -= x
        if self.is_breakable and self.solidity_axe <= 0:
            self.destroy()

    def chop_or_mine(self):
        if self.solidity_axe > self.solidity_pickaxe:
            return True
        return False

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
        self.drop = Items.DugDirt()

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
        self.drop = Items.QuarriedStone

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
        self.drop = Items.QuarriedCopperOre

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
        self.drop = Items.QuarriedIronOre

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
        self.drop = Items.Timber

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
        self.drop = Items.Timber

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
        self.drop = Items.Workbench

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
        self.drop = Items.Furnace

        self.image.fill(self.color)
        self.sprite.update_image(self.image)
