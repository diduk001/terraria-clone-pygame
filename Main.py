import pygame
import World
import Blocks
import Player


def main():
    global world
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
        if pygame.key.get_pressed()[32]:
            player.jump()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == 100:
                    player.speed_x(player.speed)
                if event.key == 97:
                    player.speed_x(-player.speed)
            if event.type == pygame.KEYUP:
                if event.key == 100:
                    player.speed_x(-player.speed)
                if event.key == 97:
                    player.speed_x(player.speed)
            if event.type == pygame.QUIT:
                running = False

        world.show()
        player.show(screen)

        pygame.display.flip()

        # Обновление персонажа

        player.move()

        clock.tick(fps)

if __name__ == '__main__':
    world = list()
    main()