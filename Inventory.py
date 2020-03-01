import pygame


class Inventory:
    def __init__(self, qapheight, bpheight, width, x, y):

        # Координаты левого верхнего угла инвенторя

        self.x = x
        self.y = y

        # Высто панели быстрого доступа (qap - quick access panel) и рюкзака (bp - backpack) в ячейках
        # Ширина инвентаря в ячейках
        # Список координат каждой из ячеек

        self.qapheight = qapheight
        self.bpheight = bpheight
        self.width = width
        self.coordinates = [[(200, 200) for i in range(width)] for i in range(qapheight + bpheight)]

        # Размер ячеек и рамок между ними в пикселях

        self.cell_size = 32
        self.frame_size = 6

        # Вычисление координат каждой ячейки (сначала пбд, потом рюкзака)

        for i in range(self.qapheight):
            for j in range(self.width):
                self.coordinates[i][j] = (self.x + j * (self.cell_size + self.frame_size) + self.frame_size,
                                          self.y + i * (self.cell_size + self.frame_size) + self.frame_size)

        for i in range(self.qapheight, self.bpheight + self.qapheight):
            for j in range(self.width):
                self.coordinates[i][j] = (self.x + j * (self. cell_size + self.frame_size) + self.frame_size,
                                          self.y + i * (self.cell_size + self.frame_size) + 3 * self.frame_size)

        # Открыт ли инвентарь
        # Содержимое инвенторя по ячейкам

        self.is_open = bool()
        self.content = [[(-1, 0) for i in range(width)] for i in range(qapheight + bpheight)]

        # Список ячеек, содержимое которых надо поменять местами
        # Выбранная ячейка (только для пбд, тоже самое, что и итем в руке)

        self.to_swap = []
        self.chosen_cell = ()


    def show(self, screen):

        # Отрисовка панели быстрого доступа

        # Отрисовка заднего фона
        qap_x_size = self.width * (self.cell_size + self.frame_size) + self.frame_size
        qap_y_size = self.qapheight * (self.cell_size + self.frame_size) + self.frame_size
        pygame.draw.rect(screen, (149, 149, 149), (self.x, self.y, qap_x_size, qap_y_size), 0)

        # Отрисовка ячеек
        for i in range(self.qapheight):
            for j in range(self.width):
                x, y = self.coordinates[i][j]
                pygame.draw.rect(screen, (174, 174, 174), (x, y, self.cell_size, self.cell_size), 0)

        # Отрисовка рюкзака

        if self.is_open:

            # Отрисовка заднего фона
            bp_x_size = self.width * (self.cell_size + self.frame_size) + self.frame_size
            bp_y_size = self.bpheight * (self.cell_size + self.frame_size) + self.frame_size
            bp_x = self.x
            bp_y = self.y + qap_y_size + self.frame_size
            pygame.draw.rect(screen, (149, 149, 149), (bp_x, bp_y, bp_x_size, bp_y_size), 0)

            # Отрисовка ячеек
            for i in range(self.qapheight, self.bpheight + self.qapheight):
                for j in range(self.width):
                    x, y = self.coordinates[i][j]
                    pygame.draw.rect(screen, (174, 174, 174), (x, y, self.cell_size, self.cell_size), 0)

        # Отрисовка обводки вещи в руке
        if self.chosen_cell != ():
            i, j = self.chosen_cell
            x, y = self.coordinates[i][j]
            pygame.draw.rect(screen, (100, 200, 200), (x, y, self.cell_size, self.cell_size), 2)

        # Отрисовка обводки выбранных клеток

        for i, j in self.to_swap:
            x, y = self.coordinates[i][j]
            pygame.draw.rect(screen, (200, 100, 100), (x, y, self.cell_size, self.cell_size), 2)

    def swap(self):
        x1, y1 = self.to_swap[0]
        x2, y2 = self.to_swap[1]
        self.content[x1][y1], self.content[x2][y2] = self.content[x2][y2], self.content[x1][y1]
        self.to_swap = []
        print("swaped")

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        if self.is_open:
            for i in range(self.qapheight + self.bpheight):
                for j in range(self.width):
                    cell_x, cell_y = self.coordinates[i][j]
                    if cell_x <= x <= cell_x + self.cell_size and cell_y <= y <= cell_y + self.cell_size:
                        return i, j
        else:
            for i in range(self.qapheight):
                for j in range(self.width):
                    cell_x, cell_y = self.coordinates[i][j]
                    if cell_x <= x <= cell_x + self.cell_size and cell_y <= y <= cell_y + self.cell_size:
                        return i, j
        return None

    def clicked(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        print(cell)
        if cell is None:
            return
        if self.is_open:
            self.to_swap += [cell]
            if len(self.to_swap) == 2:
                self.swap()
        else:
            self.chosen_cell = cell
