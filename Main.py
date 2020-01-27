import pygame
import World
import Blocks
import Player


def main():
    pygame.init()

    # Расширение игры

    height, width = 800, 400
    screen = pygame.display.set_mode((height, width))

    # Создание мира и игрока в ценре мира

    world = World.World(screen)
    player = Player.Player(world.width // 2, world.height // 2)

    # Настройка fps, цикла игры

    fps = 60
    clock = pygame.time.Clock()
    running = True

    while running:
        # Обработка событий

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        world.show()
        player.show(screen)

        pygame.display.flip()

        # Обновление персонажа

        player.update()
        player.move()

        clock.tick(fps)

if __name__ == '__main__':
    main()