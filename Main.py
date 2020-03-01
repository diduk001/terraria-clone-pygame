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

    # Создание мира и игрока в ценре мира

    world = World.World(screen)
    player = Mobs.Player(world.width // 2 * Blocks.Block.size, (world.height // 2 - 2) * Blocks.Block.size)
    inventory = Inventory.Inventory(1, 3, 10, 10, 10)

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
                inventory.is_open = not inventory.is_open
                inventory.to_swap = []
            if event.type == pygame.MOUSEBUTTONDOWN:
                inventory.clicked(event.pos)
            if event.type == pygame.QUIT:
                running = False

        world.show()
        inventory.show(screen)
        pygame.display.flip()

        # Обновление персонажа
        player.move()
        player.update()

        clock.tick(fps)

if __name__ == '__main__':
    world = list()
    main()