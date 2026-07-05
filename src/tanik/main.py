# Разные утилиты для удобной работы
from utils import clear_terminal

# Логика игры
from tanik.engine import AssetManager, AssetId, Color
from tanik.engine import bus, Signals, States
from tanik.engine import menu_input_handler

# UI игры
from tanik.ui import draw_menu


def main() -> None:
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

        current_state: States = menu_input_handler()
        bus.emit(
            Signals.CURRENT_MENU_STATE,
            current_state=current_state,
        )

        if 1 == 1:
            break

    assets.unload_all()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass