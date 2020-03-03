import random

import Blocks

# Файл с функциями для генерации смира
# generate - функция для генерации всего мира


def generate(width, height):
    # Наполнение мира землёй

    layers_dirt = gen_dirt(2, height // 2, width, height // 4, 3 * height // 4, [0, 0, 0,
                                                                                 1, 1, 1, 1,
                                                                                 2, 2, 3,
                                                                                 3])
    layers_dirt[-1] = layers_dirt[-2]

    # Наполнение мира камнем

    # d_dirt_stone - Минимальное кол-во блоков грязи над камнем

    d_dirt_stone = 4
    layers_stone = gen_stone(4, width, 2, d_dirt_stone, layers_dirt, [0, 0, 0, 0, 1, 1, 1, 2])
    # Заполнение мира

    world = [[Blocks.Air(x, y) for y in range(height)] for x in range(width)]

    for x in range(width):

        # Наолнение землёй

        for y in range(height - 1, height - layers_dirt[x], -1):
            world[x][y] = Blocks.Dirt(x, y)

        # Наполнение камнем

        for y in range(height - 1, height - layers_stone[x], -1):
            world[x][y] = Blocks.Stone(x, y)

        # Наполнение ЖожоСтоуном (яре яре дазе)

        world[x][height - 1] = Blocks.JoJoStone(x, height - 1)
    return world


# Функция генерация слоёв земли (слои расположены слева направо (Намджун, Чонгук, Чингачгук,
#                                                                Гойко Митич, Джин, Юнги)

# step          - шаг для генерации случайных значений
# start_height  - стартовая высота (значение в layers[0]), в блоках
# width         - ширина мира в блоках
# lower_bound   - самое низкое допустимое значение layers
# upper_bound   - самое высокое допустимое значение layers
# rand_arr      - список с возможными изменениями высоты

def gen_dirt(step, start_height, width, lower_bound, upper_bound, rand_arr):
    layers = [0 for _ in range(width)]
    layers[0] = start_height

    # Заполняем все слои, чей номер кратен step

    for layer in range(step, width, step):
        try:
            layers[layer] = layers[layer - step] + random.choice([1, -1]) * random.choice(rand_arr)
        except IndexError:
            continue

        if layers[layer] < lower_bound:
            layers[layer] = layers[layer - step] + 1

        if layers[layer] > upper_bound:
            layers[layer] = layers[layer - step] - 1

    #  Заполняем промежуточные слои

    for layer in range(1, width):
        if layer % step == 0:
            continue

        try:
            # Заполняем слой средним арифметическим из предыдущего и следующего слоя, кратных step

            layers[layer] = (layers[layer - layer % step] + layers[layer + (step - layer % step)]) \
                            // step
        except IndexError:
            continue
    return layers


# Функция генерации слоёв камня (аналогична gen_dirt, но с весомыми поправками)

# step          - шаг для генерации случайных значений
# start_height  - стартовая высота (значение в layers[0]), в блоках
# width         - ширина мира в блоках
# lower_bound   - самое низкое допустимое значение layers
# d_dirt_stone  - минимальная прослойка земли в блоках
# dirt_layers   - список, сгенерированный функцией gen_dirt
# rand_arr      - список с возможными изменениями высоты

def gen_stone(step, width, lower_bound, d_dirt_stone, layers_dirt, rand_arr):
    layers = [0 for _ in range(width)]
    layers[0] = layers_dirt[0] - d_dirt_stone

    # Заполняем все слои, чей номер кратен step

    for layer in range(step, width, step):
        try:
            layers[layer] = layers[layer - step] + random.choice([1, -1]) * random.choice(rand_arr)
        except IndexError:
            continue

        if layers[layer] < lower_bound:
            layers[layer] = layers[layer - step] + 1

        if layers[layer] > layers_dirt[layer] - d_dirt_stone:
            layers[layer] = layers[layer - step] - 1

    #  Заполняем промежуточные слои

    for layer in range(1, width):
        if layer % step == 0:
            continue

        try:
            # Заполняем слой средним арифметическим из предыдущего и следующего слоя, кратных step

            layers[layer] = (layers[layer - layer % step] + layers[layer + (step - layer % step)]) \
                            // step
        except IndexError:
            continue
    return layers
