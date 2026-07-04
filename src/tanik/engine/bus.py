from enum import Enum, auto

class States(Enum):
    PLAY_STATE       = auto() # 1. Go fight!
    STATS_STATE      = auto() # 2. Stats
    ACHIVMENTS_STATE = auto() # 3. Achivments
    INVENTORY_STATE  = auto() # i. Inventory
    UPGRADE_STATE    = auto() # u. Upgrade menu
    SHOP_STATE       = auto() # s. Shop
    EVENTS_STATE     = auto() # v. Events
    SETTINGS_STATE   = auto() # e. Setings
    SAVE_STATE       = auto() # a. Save
    QUIT_STATE       = auto() # q. Quit

class Signals(Enum):
    CURRENT_MENU_STATE = auto()

class EventBus:
    def __init__(self):
        self._subscribers = {}

    def connect(self, event_name, callback):
        if event_name not in self._subscribers:
            self._subscribers[event_name] = []
        self._subscribers[event_name].append(callback)

    def disconnect(self, event_name, callback):
        if event_name in self._subscribers:
            self._subscribers[event_name].remove(callback)

    def emit(self, event_name, *args, **kwargs):
        if event_name in self._subscribers:
            for callback in self._subscribers[event_name]:
                callback(*args, **kwargs)

bus = EventBus()