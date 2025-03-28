# test_case_stats.py

# Список для хранения количества тест-кейсов за каждый день недели
test_cases = []

# Дни недели (для подсказки пользователю)
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

# Запрашиваем данные у пользователя
for day in days:
    while True:
        try:
            count = int(input(f"Сколько тест-кейсов вы выполнили в {day}? "))
            if count < 0:
                print("Число не может быть отрицательным. Попробуйте снова.")
                continue
            test_cases.append(count)
            break
        except ValueError:
            print("Пожалуйста, введите целое число.")

# Подсчёт общего и среднего количества тестов
total = sum(test_cases)
average = total / len(test_cases)

# Вывод результатов
print(f"\nВсего тест-кейсов за неделю: {total}")
print(f"Среднее количество тест-кейсов в день: {average:.2f}")

# Мотивашка
if average > 10:
    print("Отличная работа!")
else:
    print("Попробуйте улучшить результат.")
