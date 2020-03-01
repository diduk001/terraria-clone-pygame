import pygame


class Window:
    def __init__(self):
        # размеры окна в ячейках и размеры ячейки
        self.height = 4
        self.weight = 10
        self.size = 40
        self.open = False

        # сам инвентарь
        self.case = [[[] for y in range(self.height)] for x in range(self.weight)]

    def show(self, screen):
        pygame.draw.rect(screen, (149, 149, 149),
                         (5 * self.size - 4, 5 * self.size - 4, self.weight * self.size + 16,
                          self.height * self.size + 8))
        for x in range(5, self.weight + 5):
            for y in range(5, self.height + 5):
                pygame.draw.rect(screen, (149, 149, 149),
                                 (x * self.size, y * self.size, self.size + 4, self.size + 4))
                pygame.draw.rect(screen, (176, 174, 174),
                                 (x * self.size + 2, y * self.size + 2, self.size, self.size))
