# Шина
from engine import EventBus

# Разные утилиты для удобной работы
from utils import clear_terminal

# Логика игры
from engine import AssetManager, AssetId, Color

# Визуальная часть игры
from ui import draw_menu

if __name__ == "__main__":
    # Инициализация
    assets = AssetManager()
    bus = EventBus

    # Загрузка ассетов
    assets.load(AssetId.PLAYER, "@", Color.YELLOW)
    assets.load(AssetId.WALL, "#", Color.GRAY)
    assets.load(AssetId.SMALL_ENEMY, "e", Color.RED)
    assets.load(AssetId.NORMAL_ENEMY, "E", Color.RED)
    assets.load(AssetId.FLOOR, ".", Color.GRAY)

    # TODO: The Entire Game!!!

    assets.unload_all()