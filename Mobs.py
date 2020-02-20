import pygame


class Mobs:
    def __init__(self):
        self.hp = int()
        self.height = int()
        self.wight = int()
        self.x = int()
        self.y = int()
        self.speed_x = int()
        self.speed_y = int()
        self.attack = int()
        self.is_aggressive = bool()

    def damage(self, x):
        self.hp -= x

    def punch(self, mob):
        mob.damage(self.attack)
