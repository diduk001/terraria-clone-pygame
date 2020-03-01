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

    # Создание мира и игрока в центре мира, на блоке

    world = World.World(screen)

    # Выбор места для спавна игрока

    spawn_x_coord = world.width // 2 * Blocks.Block.size + 1
    spawn_y_coord = int()
    for spawn_y in range(1, world.height * Blocks.Block.size, Blocks.Block.size):
        if isinstance(world.get_block(spawn_x_coord, spawn_y + 2 * Blocks.Block.size), Blocks.Dirt):
            spawn_y_coord = spawn_y
            break

    # Создание игрока, инвентаря

    player = Player.Player(spawn_x_coord, spawn_y_coord - 1)
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
    world = World.World
    main()
