from project.restaurant import Restaurant
if __name__ == "__main__":
    # 1. Создаем ресторан с лимитом на 3 официанта
    my_rest = Restaurant("Gusteau's", 3)

    # 2. Добавляем официантов
    print(my_rest.add_waiter("Linguini"))  # Успешно
    print(my_rest.add_waiter("Colette"))  # Успешно
    print(my_rest.add_waiter("Linguini"))  # Ошибка: уже существует

    # 3. Добавляем заработок напрямую в словари (имитируем рабочую смену)
    my_rest.waiters[0]['total_earnings'] = 1500  # Linguini
    my_rest.waiters[1]['total_earnings'] = 3000  # Colette

    # 4. Проверяем общий заработок
    print(f"\nTotal earnings of all waiters: {my_rest.get_total_earnings()}")

    # 5. Тестируем хитрую фильтрацию
    print("\n--- Фильтрация ---")

    # Ищем тех, кто заработал от 1000 до 2000
    mid_earners = my_rest.get_waiters(min_earnings=1000, max_earnings=2000)
    print("Waiters (1000-2000):", mid_earners)

    # Ищем тех, кто заработал больше 2000 (без максимума)
    top_earners = my_rest.get_waiters(min_earnings=2000)
    print("Waiters (>2000):", top_earners)