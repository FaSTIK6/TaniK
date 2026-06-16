import time
from rich.live import Live
from rich.panel import Panel
from rich.console import Console

def generate_frame(x: int) -> Panel:
    """Генерирует контент для одного кадра."""
    content = " " * x + "@"
    return Panel(content, title="TaniK RPG", subtitle=f"Pos: {x}")

def main():
    console = Console()
    x = 0
    
    with Live(generate_frame(x), refresh_per_second=10) as live:
        while x < 20:
            time.sleep(0.1)
            x += 1
            # Обновляем кадр
            live.update(generate_frame(x))

if __name__ == "__main__":
    main()