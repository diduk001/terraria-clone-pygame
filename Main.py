import pygame
import World
import Blocks
import Player
import Inventory

def main():
    pygame.init()

    # Расширение игры

    height, width = 1000, 600
    screen = pygame.display.set_mode((height, width))

    # Создание мира и игрока в ценре мира

    world = World.World(screen)
    player = Player.Player(world.width // 2 * Blocks.Block.size, (world.height // 2 - 2) * Blocks.Block.size)
    inventory = Inventory.Window()
    # Настройка fps, цикла игры

    fps = 60
    clock = pygame.time.Clock()
    running = True

    while running:
        # Обработка событий
        if pygame.key.get_pressed()[32] and player.up:
            player.jump()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == 9:
                if inventory.open:
                    inventory.open = False
                else:
                    inventory.open = True
            if event.type == pygame.KEYDOWN:
                if event.key == 100 and player.right:
                    player.speed_x(player.speed)
                if event.key == 97 and player.left:
                    player.speed_x(-player.speed)
            if event.type == pygame.KEYUP:
                if event.key == 100 and player.vx != 0:
                    player.speed_x(-player.speed)
                if event.key == 97 and player.vx != 0:
                    player.speed_x(player.speed)
            if event.type == pygame.QUIT:
                running = False

        world.show()
        player.show(screen)
        if inventory.open:
            inventory.show(screen)
        pygame.display.flip()

        # Обновление персонажа
        player.move()


        clock.tick(fps)

if __name__ == '__main__':
    world = list()
    main()