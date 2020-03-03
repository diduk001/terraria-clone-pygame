import os.path

import pygame


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
border_sprites = pygame.sprite.Group()
item_sprites = pygame.sprite.Group()


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


class BorderSprites(pygame.sprite.Sprite):
    def __init__(self, group, x, y, width, height):
        super().__init__(group)
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update_coordinates(self, x, y):
        self.rect.x = x
        self.rect.y = y


class ItemSprite(MySprite):
    def __init__(self, item):
        super().__init__(item_sprites, item)
        self.item = item
        self.vy = 0
        self.image.fill(self.item.color)

    def move(self):
        dirt = False
        for block_sprite in pygame.sprite.spritecollide(self, blocks_sprites, False):
            block = block_sprite.block
            if not block.is_passable:
                dirt = True
                self.vy = 0
            elif not dirt:
                self.vy = 2
        self.rect.y += self.vy


class MobSprite(MySprite):
    def __init__(self, mob):
        super().__init__(player_sprite, mob)
        self.mob = mob
        up = [self.mob.x, self.mob.y + self.mob.jump_speed, self.mob.width, -self.mob.jump_speed]
        down = [self.mob.x, self.mob.y + self.mob.height, self.mob.width, -self.mob.jump_speed]
        left = [self.mob.x - self.mob.speed, self.mob.y, self.mob.speed, self.mob.height]
        right = [self.mob.x + self.mob.width, self.mob.y, self.mob.speed, self.mob.height]
        self.up = BorderSprites(border_sprites, *up)
        self.down = BorderSprites(border_sprites, *down)
        self.left = BorderSprites(border_sprites, *left)
        self.right = BorderSprites(border_sprites, *right)

    def move(self):
        # блоки в которые врезался игрок сверху
        for block_sprite in pygame.sprite.spritecollide(self.up, blocks_sprites, False):
            block = block_sprite.block
            if not block.is_passable:
                self.mob.jump_now = False
                self.mob.vy = max(0, self.mob.vy)
                self.mob.up_free = False
                self.mob.now_jump_time = 0

        # блоки в которые врезался игрок снизу
        dirt = False
        for block_sprite in pygame.sprite.spritecollide(self.down, blocks_sprites, False):
            block = block_sprite.block

            if not block.is_passable:
                dirt = True
                self.mob.vy = min(0, self.mob.vy)
                self.mob.down_free = False
            elif not dirt and not self.mob.jump_now:
                self.mob.vy = -self.mob.jump_speed

        # блоки в которые врезался игрок слева
        for block_sprite in pygame.sprite.spritecollide(self.left, blocks_sprites, False):
            block = block_sprite.block
            if not block.is_passable:
                self.mob.vx = max(0, self.mob.vx)
                self.mob.right = False

        # блоки в которые врезался игрок справа
        for block_sprite in pygame.sprite.spritecollide(self.right, blocks_sprites, False):
            block = block_sprite.block
            if not block.is_passable:
                self.mob.vx = min(0, self.mob.vx)
                self.mob.right = False

        self.rect = self.rect.move(self.mob.vx, self.mob.vy)
        self.update_coordinates()

    def update_coordinates(self):
        self.mob.x = self.rect.x
        self.mob.y = self.rect.y
        self.up.update_coordinates(self.mob.x, self.mob.y - 1)
        self.down.update_coordinates(self.mob.x, self.mob.y + self.mob.height)
        self.left.update_coordinates(self.mob.x - self.mob.speed, self.mob.y)
        self.right.update_coordinates(self.mob.x + self.mob.width, self.mob.y)


class PlayerSprites(MobSprite):
    def __init__(self, player):
        super().__init__(player)
        self.player = player
    def move(self):
        super().move()
        for item_sprite in pygame.sprite.spritecollide(self, item_sprites, False):
            item = item_sprite.item
            self.player.inventory.item_add(item, 1)
            item_sprite.delete()