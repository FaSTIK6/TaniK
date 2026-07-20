from tanik.engine import AssetManager, States, menu_input_handler
from tanik.ui import draw_menu, load_assets
from utils import clear_terminal


def main():
    assets = AssetManager()
    load_assets(assets)

    current_state = States.PLAY_STATE

    while True:
        clear_terminal()
        draw_menu()

        current_state = menu_input_handler()

        if current_state == States.QUIT_STATE:
            break

    assets.unload_all()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
