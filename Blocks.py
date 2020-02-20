import pygame
from pygame.rect import Rect


class Block:
    size = 16
    def __init__(self, id, x, y):
        # id блока, x координата, y координата, размер блока (в пикселях)

        self.id = id
        self.x = x
        self.y = y

        # Имя блока, его цвет отрисовки, флаг is_breakable, прочность блока

        self.name = str()
        self.color = tuple()
        self.is_breakable = bool()
        self.solidity = int()

    # Функция отрисоки

    def show(self, screen):
        if self.color == ():
            return

        pygame.draw.rect(screen, self.color, Rect(self.x, self.y, self.size, self.size))


# Блок Воздуха

class Air(Block):
    def __init__(self, x, y):
        super().__init__(0, x, y)

        self.name = "Air"
        self.color = ()
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
