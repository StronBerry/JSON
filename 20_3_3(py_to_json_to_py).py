import json

# Исходный словарь
data = {
    'translator': {
        'bugs': 'ошибка',
        'function': 'функция',
        'approve': 'согласовать'
    },
    1: 'int key',
    'set': (0, 1, 2, 3),
    'empty value': None
}

# Запись словаря в файл в формате JSON
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False)

# Чтение данных из JSON-файла и преобразование в словарь
with open("data.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

# Вывод полученного словаря
print("Словарь после чтения из JSON файла:", loaded_data)

# Сравнение типов данных
for key in data:
    print(f"Ключ: {key}")
    print(f"  Исходное значение: {data[key]} - тип {type(data[key])}")
    print(f"  Загруженное значение: {loaded_data.get(str(key))} - тип {type(loaded_data.get(str(key)))}")
