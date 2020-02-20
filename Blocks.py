import pygame
from pygame import Rect


class Block:
    size = 20
    def __init__(self, id, x, y):
        # id блока, x координата, y координата, размер блока (в пикселях)

        self.id = id
        self.x = x
        self.y = y


        # Имя блока, его цвет отрисовки, флаг is_breakable, прочность блока

        self.name = str()
        self.color = tuple()
        self.is_breakable = bool()
        self.solidity_pickaxe = int()
        self.solidity_axe = int()
        self.drop = int()

    # Функция отрисоки

    def show(self, screen):
        if self.color == ():
            return

        pygame.draw.rect(screen, self.color, Rect(self.x, self.y, self.size, self.size))

    # Функция копания

    def destroy(self, screen):
        pass


# Блок Воздуха

class Air(Block):
    def __init__(self, x, y):
        super().__init__(0, x, y)

        self.name = "Air"
        self.color = ()
        self.is_breakable = False
        self.solidity_pickaxe = -1
        self.solidity_axe = -1


# Блок Кореной Породы (JJBA: Diamond Is Unbreakable)

class JoJoStone(Block):
    def __init__(self, x, y):
        super().__init__(1, x, y)

        self.name = "JoJoStone"
        self.color = (106, 13, 173)
        self.is_breakable = False
        self.solidity_pickaxe = 1000
        self.solidity_axe = 1000


# Блок Грязи

class Dirt(Block):
    def __init__(self, x, y):
        super().__init__(2, x, y)

        self.name = "Dirt"
        self.color = (77, 38, 0)
        self.is_breakable = True
        self.solidity_pickaxe = 25
        self.solidity_axe = 25


# Блок Камня

class Stone(Block):
    def __init__(self, x, y):
        super().__init__(3, x, y)

        self.name = "Stone"
        self.color = (107, 107, 71)
        self.is_breakable = True
        self.solidity_pickaxe = 35
        self.solidity_axe = 1000


# Блок Медной Руды

class CopperOre(Block):
    def __init__(self, x, y):
        super().__init__(4, x, y)

        self.name = "Copper Ore"
        self.color = (72, 45, 20)
        self.is_breakable = True
        self.solidity_pickaxe = 50
        self.solidity_axe = 1000


# Блок Железной Руды

class IronOre(Block):
    def __init__(self, x, y):
        super().__init__(5, x, y)

        self.name = "Iron Ore"
        self.color = (203, 205, 205)
        self.is_breakable = True
        self.solidity_pickaxe = 50
        self.solidity_axe = 1000


# Блок Дерева

class Wood(Block):
    def __init__(self, x, y):
        super().__init__(6, x, y)

        self.name = "Wood"
        self.color = (133, 94, 66)
        self.is_breakable = True
        self.solidity_pickaxe = 50
        self.solidity_axe = 20


# Блок Листвы

    class Foliage(Block):
        def __init__(self, x, y):
            super().__init__(7, x, y)

            self.name = "Foliage"
            self.color = (80, 200, 120)
            self.is_breakable = True
            self.solidity_pickaxe = 5
            self.solidity_axe = 5


# Блок Древесины

class TimberBlock(Block):
    def __init__(self, x, y):
        super().__init__(8, x, y)

        self.name = "Timber Block"
        self.color = (150, 75, 0)
        self.is_breakable = True
        self.solidity_pickaxe = 50
        self.solidity_axe = 20


# Блок Верстака

class Workbench(Block):
    def __init__(self, x, y):
        super().__init__(9, x, y)

        self.name = "Workbench"
        self.color = (252, 211, 59)
        self.is_breakable = True
        self.solidity_pickaxe = 50
        self.solidity_axe = 20


# Блок Печи

class Furnace(Block):
    def __init__(self, x, y):
        super().__init__(10, x, y)

        self.name = "Furnace"
        self.color = (112, 128, 144)
        self.is_breakable = True
        self.solidity_pickaxe = 30
        self.solidity_axe = 1000

