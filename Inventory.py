import pygame


class Inventory:
    def __init__(self, qapheight, bpheight, width, x, y):

        # Высота и ширина панели быстрого доступа (qap - quick access panel) и рюкзака (bp - backpack) в ячейках

        self.qapheight = qapheight
        self.bpheight = bpheight
        self.width = width

        # Размер ячеек и рамок между ними в пикселях

        self.cell_size = 32
        self.frame_size = 6

        # Координаты левого верхнего угла инвенторя

        self.x = x
        self.y = y

        # Открыт ли инвентарь

        self.is_open = bool()

        self.qapcontent = [[(-1, 0) for i in range(width)] for i in range(qapheight)]
        self.bpcontent = [[(-1, 0) for i in range(width)] for i in range(bpheight)]

        self.to_swap = []

    def show(self, screen):

        # Отрисовка панели быстрого доступа

        # Отрисовка заднего фона
        qap_x_size = self.width * (self.cell_size + self.frame_size) + self.frame_size
        qap_y_size = self.qapheight * (self.cell_size + self.frame_size) + self.frame_size
        pygame.draw.rect(screen, (149, 149, 149), (self.x, self.y, qap_x_size, qap_y_size), 0)

        # Отрисовка ячеек
        for h in range(self.qapheight):
            for w in range(self.width):
                cell_x = self.x + self.frame_size * (w + 1) + self.cell_size * w
                cell_y = self.y + self.frame_size * (h + 1) + self.cell_size * h
                pygame.draw.rect(screen, (174, 174, 174), (cell_x, cell_y, self.cell_size, self.cell_size), 0)

        # Отрисовка рюкзака

        if self.is_open:

            # Отрисовка заднего фона
            bp_x_size = self.width * (self.cell_size + self.frame_size) + self.frame_size
            bp_y_size = self.bpheight * (self.cell_size + self.frame_size) + self.frame_size
            bp_x = self.x
            bp_y = self.y + qap_y_size + self.frame_size
            pygame.draw.rect(screen, (149, 149, 149), (bp_x, bp_y, bp_x_size, bp_y_size), 0)

            # Отрисовка ячеек
            for h in range(self.bpheight):
                for w in range(self.width):
                    cell_x = bp_x + self.frame_size * (w + 1) + self.cell_size * w
                    cell_y = bp_y + self.frame_size * (h + 1) + self.cell_size * h
                    pygame.draw.rect(screen, (174, 174, 174), (cell_x, cell_y, self.cell_size, self.cell_size), 0)



    def clicked(self):
        cell = self.get_cell()
        if cell is None:
            return
        if self.is_open:
            self.to_swap += [cell]
            if len(self.to_swap) == 2:
                self.swap()
        else:
            pass