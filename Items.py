import pygame

class Item:
    def __init__(self, id):
        # id итема;

        self.id = id

        # Имя итема
        # Его цвет
        # Рецепт крафта (список туплов(id материала, кол-во) );
        # Размер стака;

        self.name = str()
        self.color = tuple()
        self.recipe = list(tuple())
        self.max_stack = int()


# Предметы, которые можно ставить;

class PlaceableItem(Item):
    def __init__(self, id):
        super().__init__(id)

        # id блока, соответствующего текстуре;

        self.block = int()

    # функция размещения;

    def place(self, x, y):
        pass


# Предметы, на которых можно крафтить;

class CraftItem(PlaceableItem):
    def __init__(self, id):
        super().__init__(id)

        # Список предметов (id), доступных для крафта;

        self.enable_to_craft = list()

    # функция крафта (обмена ресурсов на продукт);

    def craft(self, id):
        pass


# Пердметы - инструменты (мечи, кирки, топоры);

class Instrument(Item):
    def __init__(self, id):
        super().__init__(id)

        # Инструменты не стакаются =(

        self.max_stack = 1

        # Тип инструмента (меч, кирка, топор); Наносимый урон (есть у всех инструментов); Эффективность инструмента;

        self.type = int()
        self.damage = int()
        self.efficiency = int()

    # Функция атаки;

    def attack(self):
        pass

    # Функция добычи блоков;

    def destroy(self):
        pass


class DugDirt(PlaceableItem):
    def __init__(self):
        super().__init__(0)

        self.name = "Dug Dirt"
        self.color = (77, 38, 0)
        self.recipe = []
        self.max_stack = 128
        self.block = 2


class QuarriedStone(PlaceableItem):
    def __init__(self):
        super().__init__(1)

        self.name = "Quarried Stone"
        self.color = (107, 107, 71)
        self.recipe = []
        self.max_stack = 128
        self.block = 3


class QuarriedCopperOre(PlaceableItem):
    def __init__(self):
        super().__init__(2)

        self.name = "Quarried Copper Ore"
        self.color = (72, 45, 20)
        self.recipe = []
        self.max_stack = 128
        self.block = 4


class QuarriedIronOre(PlaceableItem):
    def __init__(self):
        super().__init__(3)

        self.name = "Quarried Iron Ore"
        self.color = (203, 205, 205)
        self.recipe = []
        self.max_stack = 128
        self.block = 5


class Timber(PlaceableItem):
    def __init__(self):
        super().__init__(4)

        self.name = "Timber"
        self.color = (150, 75, 0)
        self.recipe = []
        self.max_stack = 128
        self.block = 8


class Workbench(CraftItem):
    def __init__(self):
        super().__init__(5)

        self.name = "Workbench"
        self.color = (252, 211, 59)
        self.recipe = []
        self.max_stack = 16
        self.block = 9
        self.enable_to_craft = []


class Furnace(CraftItem):
    def __init__(self):
        super().__init__(6)

        self.name = "Furnace"
        self.color = (112, 128, 144)
        self.recipe = []
        self.max_stack = 16
        self.block = 10
        self.enable_to_craft = []


class TimberSword(Instrument):
    def __init__(self):
        super.__init__(7)

        self.name = "Timber Sword"
        self.color = ()
        self.recipe = []
        self.type = 0
        self.damage = 10
        self.efficiency = 0


class TimberPickaxe(Instrument):
    def __init__(self):
        super().__init__(8)

        self.name = "Timber Pickaxe"
        self.color = ()
        self.recipe = []
        self.type = 1
        self.damage = 3
        self.efficiency = 35


class TimberAxe(Instrument):
    def __init__(self):
        super().__init__(9)

        self.name = "Timber Axe"
        self.color = ()
        self.recipe = []
        self.type = 2
        self.damage = 6
        self.efficiency = 40