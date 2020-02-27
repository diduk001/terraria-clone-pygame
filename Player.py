import pygame
from Blocks import Block
import Sprites
import Mobs
import Main
from pygame.rect import Rect


class Player:
    def __init__(self, x, y):
        # координаты по x, y
        self.x = x
        self.y = y
        self.size = 1
        self.weight = Block.size
        self.height = 2 * Block.size
        self.vx = 0
        self.vy = 0
        self.sprite = bool()
        self.hp = int()
        self.jump_speed = -30
        self.direction = bool()
        self.attack = int()
        self.speed = 10
        self.image = pygame.Surface((self.weight, self.height))
        self.sprite = Sprites.PlayerSprite(self)
        self.right = True
        self.left = True
        self.down = True
        self.up = True

    def move(self):
        self.sprite.move()

    def speed_x(self, x):
        self.vx += x

    def fall(self):
        if self.vy < 0:
            self.vy -= self.jump_speed

    def jump(self):
        if self.vy == 0:
            self.vy += self.jump_speed

    def block_now(self):
        return self.x // Block.size, self.y // Block.size

    def collide(self):
        pass

    def show(self, screen):
        Sprites.player_sprite.draw(screen)

    def damage(self, x):
        self.hp -= x

    def is_live(self):
        if self.hp > 0:
            return True
        return False
