class Mobs:
    def __init__(self):
        # Кол-во очков здоровья

        self.hp = int()

        # Высота, Ширина Моба

        self.height = int()
        self.width = int()

        # x, y координата Моба

        self.x = int()
        self.y = int()

        # Скорость Моба по x, y в данный момент

        self.speed_x = int()
        self.speed_y = int()

        # Урон, наносимый Мобом

        self.attack = int()

        # Флаг, показывающий агрессивность Моба

        self.is_aggressive = bool()

    # Метод нанесения урона Мобу

    def damage(self, x):
        self.hp -= x

    # Метод, вызываемый при ударении Моба

    def punch(self, mob):
        mob.damage(self.attack)
