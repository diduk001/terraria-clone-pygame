import pygame

import Sprites
import Inventory
import Items
from Blocks import Block


class Mobs:
    def __init__(self, x, y):
        # координаты по x, y
        self.x = x
        self.y = y
        self.size = 1
        self.width = int()
        self.height = int()
        self.vx = 0
        self.vy = 0
        self.hp = int()
        self.jump_speed = int()
        self.jump_time = int()
        self.jump_now = bool()
        self.now_jump_time = 0
        self.attack = int()
        self.speed = int()
        self.image = pygame.Surface((self.width, self.height))
        self.sprite = Sprites.MobSprite(self)
        self.right_free = bool()
        self.left_free = bool()
        self.down_free = bool()
        self.up_free = bool()

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

    # Метод нанесения урона Мобу

    def damage(self, x):
        self.hp -= x

    def is_live(self):
        if self.hp > 0:
            return True
        return False

    # Метод, вызываемый при ударении Моба

    def punch(self, mob):
        mob.damage(self.attack)


class Player(Mobs):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.hp = 100
        self.width = 1 * Block.size
        self.height = 2 * Block.size
        self.jump_speed = -8
        self.jump_time = 16
        self.attack = int()
        self.speed = 1
        self.inventory = Inventory.Inventory(1, 3, 10, 10, 10)
        self.inventory.content[0][0] = [Items.DugDirt(), 2]
        self.inventory.content[0][1] = [Items.CopperPickaxe(), 1]
        self.inventory.content[3][2] = [Items.Timber(), 100]
        self.inventory.content[0][9] = [Items.QuarriedStone(), 100]
        self.inventory.content[1][9] = [Items.QuarriedCopperOre(), 100]
        self.image = pygame.Surface((self.width, self.height))
        self.sprite = Sprites.PlayerSprites(self)
        self.efficiency_pickaxe = 1
        self.efficiency_axe = 1
        self.hand = None
        self.range = 4

    def mine(self, block):
        if block.is_breakable:
            block.mine(self.efficiency_pickaxe)

    def chop(self, block):
        if block.is_breakable:
            block.chop(self.efficiency_axe)

    def left_clicked(self, block):
        player_block_x = self.x // Block.size
        player_block_y = self.y // Block.size
        if self.range ** 2 >= (block.x - player_block_x) ** 2 - (block.y - player_block_y) ** 2:
            if self.hand is None:
                if block.chop_or_mine():
                    self.chop(block)
                else:
                    self.mine(block)
            elif self.hand.type == 1:
                self.mine(block)
            elif self.hand.type == 2:
                self.chop(block)

    def right_clicked(self, block):
        pass
        if block.name == 'Air':
            player_block_x = self.x // Block.size
            player_block_y = self.y // Block.size
            if self.range ** 2 >= (block.x - player_block_x) ** 2 - (block.y - player_block_y) ** 2:
                pass

    def update(self):
        super().update()
        self.update_hand()

    def update_hand(self):
        if self.inventory.chosen_cell is None:
            self.hand = None
        else:
            x, y = self.inventory.chosen_cell
            if self.inventory.content[x][y][0].name == "Void":
                self.hand = None
            else:
                self.hand = self.inventory.content[x][y][0]