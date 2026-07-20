from enum import Enum, auto


class States(Enum):
    PLAY_STATE         = auto()
    STATS_STATE        = auto()
    ACHIEVEMENTS_STATE = auto()
    INVENTORY_STATE    = auto()
    UPGRADE_STATE      = auto()
    SHOP_STATE         = auto()
    EVENTS_STATE       = auto()
    SETTINGS_STATE     = auto()
    SAVE_STATE         = auto()
    QUIT_STATE         = auto()


state_map = {
    "1": States.PLAY_STATE,
    "2": States.STATS_STATE,
    "3": States.ACHIEVEMENTS_STATE,
    "i": States.INVENTORY_STATE,
    "u": States.UPGRADE_STATE,
    "s": States.SHOP_STATE,
    "v": States.EVENTS_STATE,
    "e": States.SETTINGS_STATE,
    "a": States.SAVE_STATE,
    "q": States.QUIT_STATE,
}
