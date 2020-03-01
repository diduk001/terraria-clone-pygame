import random
import Blocks


def generate(width, height):
    layers_dirt = [0 for _ in range(width)]
    layers_dirt[0] = height // 2

    for layer in range(2, width, 2):
        try:
            layers_dirt[layer] = layers_dirt[layer - 2] + random.choice([1, -1]) * random.choice(
                [0, 0, 0,
                 1, 1, 1, 1,
                 2, 2, 3])
        except IndexError:
            continue

        if layers_dirt[layer] < height // 4:
            layers_dirt[layer] = layers_dirt[layer - 2] + 1

        if layers_dirt[layer] > (height * 3) // 4:
            layers_dirt[layer] = layers_dirt[layer - 2] - 1

    for layer in range(1, width, 2):
        try:
            layers_dirt[layer] = (layers_dirt[layer - 1] + layers_dirt[layer + 1]) // 2
        except IndexError:
            continue

    layers_dirt[-1] = layers_dirt[-2]
    world = [[Blocks.Air(x, y) for y in range(height)] for x in range(width)]

    for x in range(width):
        for y in range(height - 1, height - layers_dirt[x], -1):
            world[x][y] = Blocks.Dirt(x, y)

    return world
