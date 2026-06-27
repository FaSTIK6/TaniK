def c_str(text: str) -> bytes:
    """
        Преобразует строку Python (str)
        в байты для Raylib (char *).
    """
    return text.encode('utf-8')