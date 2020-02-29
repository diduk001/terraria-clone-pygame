import pygame
import World
import Blocks
import Mobs
import Inventory


def main():
    pygame.init()
    # Расширение игры

    height, width = 1000, 600
    screen = pygame.display.set_mode((height, width))

    # Создание мира и игрока в центре мира

    world = World.World(screen)
    player = Mobs.Player(world.width // 2 * Blocks.Block.size, (world.height // 2 - 2) * Blocks.Block.size)
    inventory = Inventory.Window()
    # Настройка fps, цикла игры

    fps = 120
    clock = pygame.time.Clock()

    running = True
    while running:
        # Обработка событий
        if pygame.key.get_pressed()[100]:
            player.move_right()
        if pygame.key.get_pressed()[97]:
            player.move_left()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and (event.key == 32 or event.key == 119):
                player.jump()
            if event.type == pygame.KEYDOWN and event.key == 9:
                if inventory.open:
                    inventory.open = False
                else:
                    inventory.open = True
            if event.type == pygame.QUIT:
                running = False

        world.show()
        if inventory.open:
            inventory.show(screen)
        pygame.display.flip()

        # Обновление персонажа
        player.move()
        player.update()

        clock.tick(fps)


if __name__ == '__main__':
    main()
