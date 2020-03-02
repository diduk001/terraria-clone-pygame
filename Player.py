import pygame

import Sprites
from Blocks import Block


class Player:
    def __init__(self, x, y):
        # координаты по x, y
        self.x = x
        self.y = y
        self.size = 1
        self.width = Block.size
        self.height = 2 * Block.size
        self.vx = 0
        self.vy = 0
        self.sprite = bool()
        self.hp = int()
        self.jump_speed = -8
        self.jump_time = 16
        self.jump_now = False
        self.now_jump_time = 0
        self.direction = bool()
        self.attack = int()
        self.speed = 4
        self.image = pygame.Surface((self.width, self.height))
        self.sprite = Sprites.PlayerSprites(self)
        self.right_free = True
        self.left_free = True
        self.down_free = True
        self.up_free = True

    def move(self):
        self.sprite.move()

    def move_right(self):
        if self.right_free:
            self.vx += self.speed

    def move_left(self):
        if self.left_free:
            self.vx -= self.speed

    def update(self):
        self.vx = 0
        if self.jump_now:
            self.now_jump_time += 1
        if self.now_jump_time == self.jump_time:
            self.now_jump_time = 0
            self.jump_now = False
        self.right_free = True
        self.left_free = True
        self.down_free = True
        self.up_free = True

    def jump(self):
        if self.vy == 0 and self.up_free:
            self.jump_now = True
            self.vy = self.jump_speed

    def block_now(self):
        return self.x // Block.size, self.y // Block.size

    def collide(self):
        pass

    def show(self, screen):
        Sprites.player_sprite.draw(screen)

    def damage(self, x):
        self.hp -= x

    def is_live(self):
        return self.hp < 0
