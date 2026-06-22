# IT'S TEST
# IT'S TEST
# IT'S TEST
# IT'S TEST

from tanik.bus import bus

# 1. Создаем тестовые обработчики
def test_engine_handler(thrust):
    print(f"Двигатель получил сигнал: Мощность {thrust}%")

def test_ui_handler(thrust):
    print(f"UI получил сигнал: Рисуем шкалу {thrust}%")

# 2. Подписываем их на событие
bus.connect("ENGINE", test_engine_handler)
bus.connect("UI", test_ui_handler)

# 3. Эмитим событие
print("--- Начинаем тест шины ---")
bus.emit("ENGINE", 12)
bus.emit("UI", 56)