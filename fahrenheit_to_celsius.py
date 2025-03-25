# Функция для преобразования температуры из Фаренгейта в Цельсий
def fahrenheit_to_celsius(f):
    c = (f - 32) * 5 / 9
    return c

# Задаём температуру в Фаренгейтах
f_temperature = 100

# Вычисляем температуру по Цельсию
c_temperature = fahrenheit_to_celsius(f_temperature)

# Выводим результат
print(f"{f_temperature} градусов по Фаренгейту равняется {c_temperature:.2f} по Цельсию.")
