import pygame
import os.path


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


blocks_sprites = pygame.sprite.Group()
mobs_sprites = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()


class MySprite(pygame.sprite.Sprite):
    def __init__(self, group, object):
        super().__init__(group)
        self.image = object.image
        self.rect = self.image.get_rect()
        self.rect.x = object.x * object.size
        self.rect.y = object.y * object.size
        self.group = group

    def update_image(self, new_image):
        self.image = new_image

    def delete(self):
        self.group.remove(self)


class BlockSprite(MySprite):
    def __init__(self, block):
        super().__init__(blocks_sprites, block)
        self.image = block.image
        self.block = block


class PlayerSprite(MySprite):
    def __init__(self, player):
        super().__init__(player_sprite, player)
        self.player = player

    def move(self):
        self.rect = self.rect.move(self.player.vx // 10, self.player.vy // 30)
        self.player.x = self.rect.x
        self.player.y = self.rect.y
        self.player.up = True
        self.player.down = True
        self.player.left = True
        self.player.right = True
        for block_sprite in pygame.sprite.spritecollide(self, blocks_sprites, False):
            # врезался в блок слева
            block = block_sprite.block
            if (block.x + 1) * block.size == self.player.x + 1 and block.solidity_pickaxe != -1:
                self.player.vx = 0
                self.player.left = False
            # врезался в блок справа
            elif block.x * block.size + 1 == self.player.x + block.size and (
                    block.solidity_pickaxe != -1):
                self.player.vx = 0
                self.player.right = False
            # врезался в блок сверху
            elif (block.y + 1) * block.size == self.player.y + 1 and block.solidity_pickaxe != -1:
                self.player.vy = max(0, self.player.vy)
                self.player.up = False
            # врезался в блок снизу
            elif block.y * block.size + 1 == self.player.y + 2 * block.size and (
                    block.solidity_pickaxe != -1):
                self.player.vy = min(0, self.player.vy)
                self.player.down = False
            elif block.y * block.size + 1 == self.player.y + 2 * block.size and (
                    block.solidity_pickaxe == 1):
                self.player.vy = 1


class MobSprite(MySprite):
    def __init__(self, mob):
        super().__init__(mobs_sprites, mob)
