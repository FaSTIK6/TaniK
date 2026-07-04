# Разные утилиты для удобной работы
from utils import clear_terminal

# Логика игры
from tanik.engine import AssetManager, AssetId, Color
from tanik.engine import bus, Signals
from tanik.engine import menu_input_handler

# UI игры
from tanik.ui import draw_menu


def main():
    # Инициализация
    assets = AssetManager()

    # Загрузка ассетов
    assets.load(AssetId.PLAYER, "@", Color.YELLOW)
    assets.load(AssetId.WALL, "#", Color.GRAY)
    assets.load(AssetId.SMALL_ENEMY, "e", Color.RED)
    assets.load(AssetId.NORMAL_ENEMY, "E", Color.RED)
    assets.load(AssetId.FLOOR, ".", Color.GRAY)

    bus.connect(
        Signals.CURRENT_MENU_STATE,
        draw_menu,
    )

    while True:
        clear_terminal()
        menu_input_handler()

    assets.unload_all()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass