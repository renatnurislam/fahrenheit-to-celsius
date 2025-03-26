# bug_filter.py

# Список багов
bug_reports = [
    "Ошибка 1 — High",
    "Ошибка 2 — Medium",
    "Ошибка 3 — Low",
    "Ошибка 4 — High",
    "Ошибка 5 — Low",
    "Ошибка 6 — Medium",
    "Ошибка 7 — High"
]

# Ввод от пользователя
priority = input("Введите приоритет для поиска (High, Medium, Low): ").strip().capitalize()

# Фильтрация багов
filtered_bugs = [bug for bug in bug_reports if f"— {priority}" in bug]

# Вывод результата
if filtered_bugs:
    print("\nНайденные баги:")
    for bug in filtered_bugs:
        print("-", bug)
else:
    print("Багов с таким приоритетом не найдено.")
