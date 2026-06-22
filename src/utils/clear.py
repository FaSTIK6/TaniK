import sys

def clear_terminal() -> None:
    """
    Перемещает курсор в начало экрана,
    не очищая его полностью.
    """
    sys.stdout.write("\033[H")
    sys.stdout.flush()