from .bus import bus, States, Signals, state_map


current_state: States = States.PLAY_STATE


def menu_input_handler() -> States:
    global current_state

    current_state = state_map.get("e", "Err! menu_input_handler")

    return current_state