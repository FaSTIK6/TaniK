from .bus import bus, States, Signals


current_state: States = States.PLAY_STATE


def menu_input_handler():
    global current_state
    
    bus.emit(
        Signals.CURRENT_MENU_STATE,
        current_state=current_state,
    )