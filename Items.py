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
        self.craft_count = int()
        self.max_stack = int()


# Предмет - пустая ячейка

class VoidItem(Item):
    def __init__(self):
        super().__init__(-1)

        self.name = "Void"
        self.color = ()
        self.recipe = []
        self.craft_count = 0
        self.max_stack = 0


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
        self.craft_count = 1
        self.enable_to_craft = list()


# Пердметы - инструменты (мечи, кирки, топоры);

class Instrument(Item):
    def __init__(self, id):
        super().__init__(id)

        # Инструменты не стакаются =(
        self.craft_count = 1
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
        self.color = (150, 60, 60)
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


class Iron(Item):
    def __init__(self):
        super().__init__(4)

        self.name = "Iron" # Утюг
        self.color = (203, 205, 205)
        self.recipe = [(QuarriedIronOre, 4)]
        self.craft_count = 2
        self.max_stack = 128


class Copper(Item):
    def __init__(self):
        super().__init__(5)

        self.name = "Copper"
        self.color = (150, 60, 60)
        self.recipe = [(QuarriedCopperOre, 4)]
        self.craft_count = 2
        self.max_stack = 128


class Timber(PlaceableItem):
    def __init__(self):
        super().__init__(6)

        self.name = "Timber"
        self.color = (150, 75, 0)
        self.recipe = []
        self.max_stack = 128
        self.block = 8


class Workbench(CraftItem):
    def __init__(self):
        super().__init__(7)

        self.name = "Workbench"
        self.color = (252, 211, 59)
        self.recipe = [(Timber(), 10)]
        self.max_stack = 16
        self.block = 9
        self.enable_to_craft = []


class Furnace(CraftItem):
    def __init__(self):
        super().__init__(8)

        self.name = "Furnace"
        self.color = (112, 128, 144)
        self.recipe = [(QuarriedStone(), 20), (Timber(), 10)]
        self.max_stack = 16
        self.block = 10
        self.enable_to_craft = []


class TimberSword(Instrument):
    def __init__(self):
        super().__init__(9)

        self.name = "Timber Sword"
        self.color = ()
        self.recipe = []
        self.type = 0
        self.damage = 10
        self.efficiency = 0


class TimberPickaxe(Instrument):
    def __init__(self):
        super().__init__(10)

        self.name = "Timber Pickaxe"
        self.color = ()
        self.recipe = []
        self.type = 1
        self.damage = 3
        self.efficiency = 35


class TimberAxe(Instrument):
    def __init__(self):
        super().__init__(11)

        self.name = "Timber Axe"
        self.color = ()
        self.recipe = []
        self.type = 2
        self.damage = 6
        self.efficiency = 40


class StoneSword(Instrument):
    def __init__(self):
        super().__init__(12)

        self.name = "Stone Sword"
        self.color = ()
        self.recipe = []
        self.type = 0
        self.damage = 15
        self.efficiency = 0


class StonePickaxe(Instrument):
    def __init__(self):
        super().__init__(13)

        self.name = "Stone Pickaxe"
        self.color = ()
        self.recipe = []
        self.type = 1
        self.damage = 5
        self.efficiency = 50


class StoneAxe(Instrument):
    def __init__(self):
        super().__init__(14)

        self.name = "Stone Axe"
        self.color = ()
        self.recipe = []
        self.type = 2
        self.damage = 9
        self.efficiency = 50


class CopperSword(Instrument):
    def __init__(self):
        super().__init__(15)

        self.name = "Copper Sword"
        self.color = ()
        self.recipe = []
        self.type = 0
        self.damage = 25
        self.efficiency = 0


class CopperPickaxe(Instrument):
    def __init__(self):
        super().__init__(16)

        self.name = "Copper Pickaxe"
        self.color = ()
        self.recipe = []
        self.type = 1
        self.damage = 7
        self.efficiency = 70


class CopperAxe(Instrument):
    def __init__(self):
        super().__init__(17)

        self.name = "Copper Axe"
        self.color = ()
        self.recipe = []
        self.type = 2
        self.damage = 15
        self.efficiency = 70


class IronSword(Instrument):
    def __init__(self):
        super().__init__(18)

        self.name = "Iron Sword"
        self.color = ()
        self.recipe = []
        self.type = 0
        self.damage = 30
        self.efficiency = 0


class IronPickaxe(Instrument):
    def __init__(self):
        super().__init__(19)

        self.name = "Iron Pickaxe"
        self.color = ()
        self.recipe = []
        self.type = 1
        self.damage = 10
        self.efficiency = 77


class IronAxe(Instrument):
    def __init__(self):
        super().__init__(20)

        self.name = "Iron Axe"
        self.color = ()
        self.recipe = []
        self.type = 2
        self.damage = 19
        self.efficiency = 77
