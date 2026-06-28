from enum import Enum, auto


# 1. Цветовые коды ANSI для терминала
class Color:
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    GRAY = "\033[90m"
    DARK_GRAY = "\033[30m"


# Все ассеты
class AssetId(Enum):
    PLAYER = auto()
    WALL = auto()
    SMALL_ENEMY = auto()
    NORMAL_ENEMY = auto()
    FLOOR = auto()


class AssetManager:
    def __init__(self):
        self._textures = {}

    def load(self, asset_id: AssetId, ascii_art: str, color: str = Color.WHITE):
        """Сохраняет символ и оборачивает его в ANSI-код цвета."""
        colored_art = f"{color}{ascii_art}{Color.RESET}"
        self._textures[asset_id] = colored_art

    def get(self, asset_id: AssetId) -> str:
        """Возвращает покрашенный ASCII-арт."""
        return self._textures.get(asset_id, " ")

    def unload(self, asset_id: AssetId):
        """Удаляет конкретный ассет из памяти."""
        if asset_id in self._textures:
            del self._textures[asset_id]

    def unload_all(self):
        """Очищает весь менеджер ассетов."""
        self._textures.clear()
