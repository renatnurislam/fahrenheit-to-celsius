# user_profile.py

# 1. Исходные переменные
name = "Renat"
profession = "QA Engineer"
tool = "Postman"

# 2. Позволяем пользователю обновить данные
name_input = input("Введите имя: ").strip()
if name_input:
    name = name_input
else:
    print("Имя не указано. Используется значение по умолчанию.")

profession_input = input("Введите профессию: ").strip()
if profession_input:
    profession = profession_input
else:
    print("Профессия не указана. Используется значение по умолчанию.")

tool_input = input("Введите ваш любимый инструмент для тестирования: ").strip()
if tool_input:
    tool = tool_input
else:
    print("Инструмент не указан. Используется значение по умолчанию.")

# 3. Вывод результата
print(f"\nИмя: {name}")
print(f"Профессия: {profession}")
print(f"Любимый инструмент: {tool}")