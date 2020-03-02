import pygame

import Items
import Sprites


class Inventory:
    def __init__(self, qapheight, bpheight, width, x, y):

        # Координаты левого верхнего угла инвенторя

        self.x = x
        self.y = y

        # qap - панель быстрого доступа (Quick Access Panel)
        # bp - рюкзак (BackPack)
        # Высто панели быстрого доступа и рюкзака в ячейках
        # Ширина инвентаря в ячейках
        # Список координат каждой из ячеек

        self.qapheight = qapheight
        self.bpheight = bpheight
        self.width = width
        self.coordinates = [[(0, 0) for j in range(width)] for i in range(qapheight + bpheight)] + [
            [(0, 0)]]

        # Размер ячеек и рамок между ними в пикселях

        self.cell_size = 32
        self.frame_size = 6

        # Вычисление координат каждой ячейки (по порядку пбд, рюкзак, урна)

        for i in range(self.qapheight):
            for j in range(self.width):
                self.coordinates[i][j] = (
                    self.x + j * (self.cell_size + self.frame_size) + self.frame_size,
                    self.y + i * (self.cell_size + self.frame_size) + self.frame_size)

        for i in range(self.qapheight, self.bpheight + self.qapheight):
            for j in range(self.width):
                self.coordinates[i][j] = (
                    self.x + j * (self.cell_size + self.frame_size) + self.frame_size,
                    self.y + i * (self.cell_size + self.frame_size) + 3 * self.frame_size)

        self.coordinates[-1][-1] = (
            self.x + (self.width - 1) * (self.frame_size + self.cell_size) + self.frame_size,
            self.y + (self.qapheight + self.bpheight) * self.cell_size +
            (self.qapheight + self.bpheight + 3) * self.frame_size)

        # Открыт ли инвентарь
        # Содержимое инвенторя по ячейкам

        self.is_open = bool()
        self.content = [[[Items.VoidItem(), 0] for i in range(width)] for j in range(qapheight +
                                                                                     bpheight)]

        # Список ячеек, содержимое которых надо поменять местами
        # Выбранная ячейка (только для пбд, тоже самое, что и итем в руке)

        self.to_swap = []
        self.chosen_cell = (0, 0)

        self.last_click_is_right = bool()

        self.workbench_is_available = False
        self.furnace_is_available = False
        self.enable_to_craft = [Items.Workbench(), Items.Furnace()]

        self.chosen_recipe = 1
        self.craft_coordinates = [(0, 0) for i in range(len(self.enable_to_craft))]
        self.craft_button_coordinates = (self.x + self.width * (self.cell_size + self.frame_size)
                                         + 2.5 * self.frame_size,
                                         self.y + self.frame_size / 2)

        for i in range(len(self.enable_to_craft)):
            self.craft_coordinates[i] = (
                self.x + self.width * (self.frame_size + self.cell_size) + 3 * self.frame_size,
                self.y + (self.qapheight + i) * (self.frame_size + self.cell_size)
                + 3 * self.frame_size)

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
                item, count = self.content[i][j]
                if item.id != -1:
                    x, y = self.coordinates[i][j]
                    x += 2
                    y += 2
                    pygame.draw.rect(screen, self.content[i][j][0].color, (x, y, 28, 28), 0)
                    font = pygame.font.Font("MainFont.fon", 16)
                    text = font.render(str(count), 1, (100, 230, 100))
                    screen.blit(text, (x + 2, y))

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
                    pygame.draw.rect(screen, (174, 174, 174), (x, y, self.cell_size, self.cell_size),
                                     0)
                    item, count = self.content[i][j]
                    if item.id != -1:
                        x, y = self.coordinates[i][j]
                        x += 2
                        y += 2
                        pygame.draw.rect(screen, self.content[i][j][0].color, (x, y, 28, 28), 0)
                        font = pygame.font.Font("MainFont.fon", 16)
                        text = font.render(str(count), 1, (100, 230, 100))
                        screen.blit(text, (x + 2, y))

            # Пометка урны
            x, y = self.coordinates[-1][-1]
            pygame.draw.rect(screen, (149, 149, 149),
                             (x - self.frame_size, y - self.frame_size,
                              2 * self.frame_size + self.cell_size,
                              2 * self.frame_size + self.cell_size), 0)
            pygame.draw.rect(screen, (174, 174, 174), (x, y, self.cell_size, self.cell_size), 0)
            pygame.draw.rect(screen, (149, 149, 149),
                             (x + self.cell_size / 4, y + self.cell_size / 4, self.cell_size / 2,
                              self.cell_size / 2),
                             0)

        # Отрисовка обводки вещи в руке
        if self.chosen_cell != ():
            i, j = self.chosen_cell
            x, y = self.coordinates[i][j]
            pygame.draw.rect(screen, (100, 200, 200), (x, y, self.cell_size - 1, self.cell_size - 1),
                             2)

        # Отрисовка обводки выбранных клеток

        for i, j in self.to_swap:
            x, y = self.coordinates[i][j]
            pygame.draw.rect(screen, (200, 100, 100), (x, y, self.cell_size - 1, self.cell_size - 1),
                             2)

        # Отрисовка крафтов
        if self.is_open:

            # Отрисовка кнопки крафта
            x, y = self.craft_button_coordinates
            size = self.cell_size + self.frame_size
            pygame.draw.rect(screen, (149, 149, 149), (x, y, size, size), 0)
            x += self.frame_size / 2
            y += self.frame_size / 2
            size -= self.frame_size
            pygame.draw.rect(screen, (174, 174, 174), (x, y, size, size), 0)
            x += self.frame_size
            y += self.frame_size
            size -= 2 * self.frame_size
            pygame.draw.rect(screen, (200, 100, 100), (x, y, size, size), 0)

            height = len(self.enable_to_craft) * (self.frame_size + self.cell_size) + self.frame_size
            width = 2 * self.frame_size + self.cell_size
            x = self.x + self.width * (self.frame_size + self.cell_size) + 2 * self.frame_size
            y = self.y + self.qapheight * (self.frame_size + self.cell_size) + 2 * self.frame_size
            pygame.draw.rect(screen, (149, 149, 149), (x, y, width, height), 0)
            for i in range(len(self.enable_to_craft)):
                x, y = self.craft_coordinates[i]
                pygame.draw.rect(screen, (174, 174, 174), (x, y, self.cell_size, self.cell_size), 0)
                item = self.enable_to_craft[i]
                pygame.draw.rect(screen, item.color, (x + 2, y + 2, 28, 28), 0)
                font = pygame.font.Font("MainFont.fon", 16)
                text = font.render(str(item.craft_count), 1, (100, 230, 100))
                screen.blit(text, (x + 4, y + 2))
            x, y = self.craft_coordinates[self.chosen_recipe]
            item = self.enable_to_craft[self.chosen_recipe]
            pygame.draw.rect(screen, (100, 200, 200), (x, y, self.cell_size - 1, self.cell_size - 1),
                             2)
            x += self.cell_size + self.frame_size
            y -= self.frame_size
            width = len(item.recipe) * (self.frame_size + self.cell_size)
            height = self.cell_size + 2 * self.frame_size
            pygame.draw.rect(screen, (149, 149, 149), (x, y, width, height), 0)
            y += self.frame_size
            for i in range(len(item.recipe)):
                pygame.draw.rect(screen, (174, 174, 174), (x, y, self.cell_size, self.cell_size), 0)
                ingredient, count = item.recipe[i]
                pygame.draw.rect(screen, ingredient.color, (x + 2, y + 2, 28, 28), 0)
                font = pygame.font.Font("MainFont.fon", 16)
                text = font.render(str(count), 1, (100, 230, 100))
                screen.blit(text, (x + 4, y + 2))
                x += self.cell_size + self.frame_size

    def left_swap(self):
        x1, y1 = self.to_swap[0]
        x2, y2 = self.to_swap[1]
        if (x1, y1) == (-1, -1):
            self.content[x2][y2] = [Items.VoidItem(), 0]
        elif (x2, y2) == (-1, -1):
            self.content[x1][y1] = [Items.VoidItem(), 0]
        elif self.content[x1][y1][0].id == self.content[x2][y2][0].id:
            if self.content[x1][y1][1] <= (
                    self.content[x2][y2][0].max_stack - self.content[x2][y2][1]):
                self.content[x2][y2][1] += self.content[x1][y1][1]
                self.content[x1][y1] = [Items.VoidItem(), 0]
            else:
                self.content[x1][y1][1] -= self.content[x2][y2][0].max_stack - self.content[x2][y2][
                    1]
                self.content[x2][y2][1] = self.content[x2][y2][0].max_stack

        else:
            self.content[x1][y1], self.content[x2][y2] = self.content[x2][y2], self.content[x1][y1]
        self.to_swap = []

    def right_swap(self):
        x1, y1 = self.to_swap[0]
        x2, y2 = self.to_swap[1]
        if self.content[x1][y1][0].id == Items.VoidItem().id:
            self.last_click_is_right = False
            self.to_swap = []
        elif (x2, y2) == (-1, -1):
            self.content[x1][y1][1] -= 1
            self.to_swap.pop()
        elif self.content[x2][y2][0].id == Items.VoidItem().id:
            self.content[x2][y2] = [self.content[x1][y1][0], 1]
            self.content[x1][y1][1] -= 1
            self.to_swap.pop()
        elif self.content[x1][y1][0].id != self.content[x2][y2][0].id:
            self.last_click_is_right = False
            self.left_swap()
        else:
            if self.content[x2][y2][1] < self.content[x2][y2][0].max_stack:
                self.content[x2][y2][1] += 1
                self.content[x1][y1][1] -= 1
                self.to_swap.pop()
            else:
                self.to_swap = []
        if self.content[x1][y1][1] == 0:
            self.content[x1][y1] = [Items.VoidItem(), 0]

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        if self.is_open:
            cell_x, cell_y = self.craft_button_coordinates
            cell_x += self.frame_size / 2
            cell_y += self.frame_size / 2
            if cell_x <= x <= cell_x + self.cell_size and cell_y <= y <= cell_y + self.cell_size:
                return -2, -2
            for i in range(self.qapheight + self.bpheight):
                for j in range(self.width):
                    cell_x, cell_y = self.coordinates[i][j]
                    if cell_x <= x <= cell_x + self.cell_size and cell_y <= y <= (
                            cell_y + self.cell_size):
                        return i, j
            cell_x, cell_y = self.coordinates[-1][-1]
            if cell_x <= x <= cell_x + self.cell_size and cell_y <= y <= cell_y + self.cell_size:
                return -1, -1
        else:
            for i in range(self.qapheight):
                for j in range(self.width):
                    cell_x, cell_y = self.coordinates[i][j]
                    if cell_x <= x <= cell_x + self.cell_size and cell_y <= y <= (
                            cell_y + self.cell_size):
                        return i, j
        return None

    def left_clicked(self, mouse_pos):
        if self.last_click_is_right:
            self.last_click_is_right = False
            self.to_swap = []
            return
        cell = self.get_cell(mouse_pos)
        if cell is None:
            return
        if self.is_open:
            if cell == (-2, -2):
                self.craft()
                return
            self.to_swap += [cell]
            if len(self.to_swap) == 2:
                self.left_swap()
        else:
            self.chosen_cell = cell

    def right_clicked(self, mouse_pos):
        self.last_click_is_right = True
        cell = self.get_cell(mouse_pos)
        if cell == (-2, -2):
            return
        if cell is None:
            return
        elif not self.is_open:
            return
        elif len(self.to_swap) == 0:
            return
        else:
            self.to_swap += [cell]
            self.right_swap()

    def up_chosen_cell(self):
        if self.chosen_cell == ():
            self.chosen_cell = (0, 0)
            return
        x, y = self.chosen_cell
        if y == 0:
            self.chosen_cell = (x, self.width - 1)
        else:
            self.chosen_cell = (x, y - 1)

    def down_chosen_cell(self):
        if self.chosen_cell == ():
            self.chosen_cell = (0, 9)
            return
        x, y = self.chosen_cell
        if y == self.width - 1:
            self.chosen_cell = (x, 0)
        else:
            self.chosen_cell = (x, y + 1)

    def up_chosen_recipe(self):
        if self.chosen_recipe != 0:
            self.chosen_recipe -= 1

    def down_chosen_recipe(self):
        if self.chosen_recipe != len(self.enable_to_craft) - 1:
            self.chosen_recipe += 1

    def item_count(self, item_id):
        count = 0
        for i in range(self.qapheight + self.bpheight):
            for j in range(self.width):
                if self.content[i][j][0].id == item_id:
                    count += self.content[i][j][1]
        return count

    def item_delete(self, item_id, count):
        for i in range(self.qapheight + self.bpheight):
            for j in range(self.width):
                if self.content[i][j][0].id == item_id:
                    if self.content[i][j][1] > count:
                        self.content[i][j][1] -= count
                        return
                    else:
                        count -= self.content[i][j][1]
                        self.content[i][j] = [Items.VoidItem(), 0]

    def item_add(self, item, count):
        for i in range(self.qapheight + self.bpheight):
            for j in range(self.width):
                if self.content[i][j][0].id == Items.VoidItem().id:
                    if count < item.max_stack:
                        self.content[i][j] = [item, count]
                        count = 0
                    else:
                        count -= item.max_stack
                        self.content[i][j] = [item, item.max_stack]
                elif self.content[i][j][0].id == item.id:
                    if self.content[i][j][1] + count < item.max_stack:
                        self.content[i][j][1] += count
                        count = 0
                    else:
                        count -= item.max_stack - self.content[i][j][1]
                        self.content[i][j][1] = item.max_stack
                if count == 0:
                    return

    def craft(self):
        item = self.enable_to_craft[self.chosen_recipe]
        for ingredient, count in item.recipe:
            if self.item_count(ingredient.id) < count:
                return
        for ingredient, count in item.recipe:
            self.item_delete(ingredient.id, count)
        self.item_add(item, item.craft_count)

    def update(self, player):
        self.update_hand(player)
        for item in pygame.sprite.spritecollide(player.sprite, Sprites.item_sprites, False):
            self.item_add(item, 1)

    def update_hand(self, player):
        if self.chosen_cell is None:
            player.hand = None
        else:
            x, y = self.chosen_cell
            if self.content[x][y][0].name == "Void":
                player.hand = None
            else:
                player.hand = self.content[x][y]
