# Задача 1: Добавление элемента в список
numbers = [1, 2, 3]
numbers.append(4)
print("После добавления:", numbers)

# Задача 2: Удаление элемента из списка
fruits = ["Москва", "Лондон", "Париж"]
fruits.remove("Лондон")
print("После удаления:", fruits)

# Задача 3: Доступ к элементу по индексу
cities = ["Москва", "Питер", "Новосибирск", "Екатеринбург"]
print("Элемент по индексу 2:", cities[2])

# Задача 4: Доступ к элементу по срезу списка
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Срез [3:7]:", numbers[3:7])

# Задача 5: Изменение элемента списка
colors = ["red", "green", "blue"]
colors[1] = "yellow"
print("После изменения:", colors)

# Задача 6: Узнаем длину списка
animals = ["cat", "dog", "rabbit", "hamster"]
print("Длина списка:", len(animals))

# Задача 7: Добавление элемента в словарь
student = {"name": "Ivan", "age": 20}
student["grade"] = "A"
print("После добавления:", student)

# Задача 8: Изменение элемента словаря
student = {"name": "Ivan", "age": 20, "grade": "B"}
student["grade"] = "A"
print("После изменения:", student)

# Задача 9: Удаление элемента из словаря
student = {"name": "Ivan", "age": 20, "grade": "A"}
del student["age"]
print("После удаления:", student)

# Задача 10: Доступ к элементу словаря по ключу
student = {"name": "Ivan", "age": 20, "grade": "A"}
print("Имя студента:", student["name"])

# Задача 11: Проверка наличия ключа в словаре
student = {"name": "Ivan", "age": 20, "grade": "A"}
if "grade" in student:
    print("Ключ 'grade' найден.")
else:
    print("Ключ 'grade' не найден.")

# Задача 12: Изменение элемента во вложенном словаре
student = {"name": "Ivan", "address": {"city": "Moscow", "street": "Lenina"}}
student["address"]["city"] = "Saint Petersburg"
print("После изменения города:", student)

# Задача 13: Изменение элемента в списке внутри словаря
student = {"name": "Maria", "grades": [75, 82, 90]}
student["grades"][0] = 85
print("После изменения оценки:", student)

# Задача 14: Изменение элемента в словаре, находящемся в списке
students = [{"name": "Ivan", "age": 20}, {"name": "Petya", "age": 22}]
for s in students:
    if s["name"] == "Petya":
        s["age"] = 23
print("После изменения возраста Петя:", students)

# Задача 15: Проверка наличия элемента и длины кортежа
colors = ("red", "green", "blue")
print("Наличие 'green':", "green" in colors)
print("Длина кортежа:", len(colors))
