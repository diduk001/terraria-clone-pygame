import Sprites
import Main

# Отдельный файл с классом камеры, позволяющей сфокусироваться на объекте и держать его в центре
# экрана

class Camera:
    def __init__(self):
        # Начальный сдвиг камеры

        self.dx = 0
        self.dy = 0

    # Сдвинуть объект obj на смещение камеры

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # Направить камеру на объект

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - Main.width // 2)
    # Метод отрисовки

    def show(self):
        for sprite in Sprites.all_sprites:
            self.apply(sprite)
