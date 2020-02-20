import pygame
from pygame.rect import Rect


class Block:
    # размер блока (в пикселях)
    size = 20

    def __init__(self, id, x, y):
        # id блока

        self.id = id
        self.x = x
        self.y = y

        # Имя блока, его цвет отрисовки, флаг is_breakable, прочность блока

        self.name = str()
        self.color = tuple()
        self.is_breakable = bool()
        self.solidity = int()

    # Функция отрисоки
    # screen - экран для отрисовки
    # x - x координата левого верхнего угла на экране
    # y - y координата левого верхнего угла на экране
    def show(self, screen, x, y):
        if self.color == ():
            return

        pygame.draw.rect(screen, self.color, Rect(x + 1, y + 1, self.size - 1, self.size - 1))

    def __str__(self):
        return f"<Block {self.name}>"

    def __repr__(self):
        return str(self)

# Блок Воздуха

class Air(Block):
    def __init__(self, x, y):
        super().__init__(0, x, y)

        self.name = "Air"
        self.color = (105, 180, 255)
        self.is_breakable = False
        self.solidity = -1


# Блок Грязи

class Dirt(Block):
    def __init__(self, x, y):
        super().__init__(1, x, y)

        self.name = "Dirt"
        self.color = (77, 38, 0)
        self.is_breakable = True
        self.solidity = 10


# Блок Камня

class Stone(Block):
    def __init__(self, x, y):
        super().__init__(2, x, y)

        self.name = "Stone"
        self.color = (107, 107, 71)
        self.is_breakable = True
        self.solidity = 25
