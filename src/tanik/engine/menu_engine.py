from .states import States, state_map


def menu_input_handler() -> States:
    user_input = input("   => ").strip().lower()
    return state_map.get(user_input, States.PLAY_STATE)
