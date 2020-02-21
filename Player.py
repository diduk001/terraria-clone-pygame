import pygame
from Blocks import Block
import Mobs
import Main
from pygame.rect import Rect


class Player:
    def __init__(self, x, y):
        # координаты по x, y
        self.x = x
        self.y = y
        self.size_x = Block.size
        self.size_y = 2 * Block.size
        self.vx = 0
        self.vy = 0
        self.sprite = bool()
        self.hp = int()
        self.jump_speed = -10
        self.direction = bool()
        self.attack = int()
        self.speed = 10

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.vy < 0:
            self.vy += 5

    def speed_x(self, x):
        self.vx += x

    def fall(self, world):
        bx, by = self.block_now()
        print(bx, by)
        by += 1
        print(world[bx][by].name)
        if (world[bx][by].solidity_pickaxe == -1 and self.vy == 0):
            self.vy -= self.jump_speed

    def jump(self):
        if self.vy == 0:
            self.vy += self.jump_speed

    def block_now(self):
        print()
        return self.x // Block.size, self.y // Block.size

    def collide(self):
        pass

    def show(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.size_x, self.size_y))

    def damage(self, x):
        self.hp -= x

    def is_live(self):
        if self.hp > 0:
            return True
        return False
