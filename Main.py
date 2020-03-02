import pygame
import Blocks
import Mobs
import Inventory
import Items
import World

global world


def block_coordinates(coordinates):
    return coordinates[0] // Blocks.Block.size, coordinates[1] // Blocks.Block.size


def main():
    pygame.init()

    # Расширение игры

    height, width = 1000, 600
    screen = pygame.display.set_mode((height, width))

    # Создание мира и игрока в центре мира

    world = World.World(screen)

    # Выбор места для спавна игрока

    spawn_x_coord = world.width // 2 * Blocks.Block.size + 1
    spawn_y_coord = int()
    for spawn_y in range(1, world.height * Blocks.Block.size, Blocks.Block.size):
        if isinstance(world.get_block(spawn_x_coord, spawn_y + 2 * Blocks.Block.size), Blocks.Dirt):
            spawn_y_coord = spawn_y
            break

    # Создание игрока, инвентаря

    player = Mobs.Player(spawn_x_coord, spawn_y_coord - 1)
    inventory = Inventory.Inventory(1, 3, 10, 10, 10)
    inventory.content[0][0] = [Items.DugDirt(), 2]
    inventory.content[3][2] = [Items.Timber(), 100]
    inventory.content[0][9] = [Items.QuarriedStone(), 100]
    inventory.content[1][9] = [Items.QuarriedCopperOre(), 100]

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
        if pygame.mouse.get_pressed()[0]:
            x, y = block_coordinates(pygame.mouse.get_pos())
            player.left_clicked(world.world[x][y])
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and (event.key == 32 or event.key == 119):
                player.jump()

            if event.type == pygame.KEYDOWN and event.key == 9:
                inventory.is_open = not inventory.is_open
                inventory.to_swap = []

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    inventory.left_clicked(event.pos)
                if event.button == 3:
                    inventory.right_clicked(event.pos)
                    x, y = block_coordinates(pygame.mouse.get_pos())
                    player.right_clicked(world.world[x][y])
                if event.button == 4:
                    if inventory.is_open:
                        inventory.up_chosen_recipe()
                    else:
                        inventory.up_chosen_cell()
                if event.button == 5:
                    if inventory.is_open:
                        inventory.down_chosen_recipe()
                    else:
                        inventory.down_chosen_cell()

            if event.type == pygame.QUIT:
                running = False

        world.show()
        world.update()
        inventory.show(screen)
        pygame.display.flip()
        # Обновление персонажа
        player.move()
        player.update()

        clock.tick(fps)

if __name__ == '__main__':
    main()