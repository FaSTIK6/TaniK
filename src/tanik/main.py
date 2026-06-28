# Шина
from .bus import bus

# Разные утилиты для удобной работы
from utils import clear_terminal

# Логика игры
from engine import AssetManager, AssetId, Color
from engine import input_handler

# Визуальная часть игры
from ui import draw_menu


if __name__ == "__main__": 
    # Инициализация менеджера ассетов
    assets = AssetManager()

    # Загрузка ассетов
    assets.load(AssetId.PLAYER, "@", Color.YELLOW)
    assets.load(AssetId.WALL, "#", Color.GRAY)
    assets.load(AssetId.SMALL_ENEMY, "e", Color.RED)
    assets.load(AssetId.NORMAL_ENEMY, "E", Color.RED)