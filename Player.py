import pygame
from Blocks import Block
import Main
from pygame.rect import Rect


class Player:
    def __init__(self, x, y):
        # координаты по x, y
        self.x = int()
        self.y = int()

        self.size_x = Block.size
        self.size_y = 2 * Block.size

        self.vx = int()
        self.vy = int()

        self.hp = int()
        self.jump_height = int()
        self.is_jump = bool()
        self.jump_speed = int()
        self.direction = bool()

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def speed_x(self, x):
        self.vx += x

    def fall(self, y):
        self.vy -= y

    def jump(self, y):
        if self.vy == 0:
            self.vy += self.jump_speed

    def block_now(self):
        return self.x / Block.size, self.y / Block.size

    def collide(self):
        b_x, b_y = self.block_now()
        if (((self.x + self.size_x + 1) % Block.size == 0 and (Main.world[b_x + 1][b_y + 1].solid != -1) or
            (self.x + 1) % Block.size == 0 and (Main.world.world[b_x + 1][b_y].solid != -1)) and self.x > 0):
            self.x = 0