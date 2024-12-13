import os
import json
import random
from nltk.corpus import words
import nltk
import ssl

# Настройка для работы без валидации SSL
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Загрузка ресурса, если он недоступен
nltk.download('words')

# Список слов
english_words = [word for word in words.words() if word.islower()]

# Убедимся, что папка существует
os.makedirs("", exist_ok=True)

def generate_random_data():
    fields = [
        {"name": "id", "type": "number"},
        {"name": "name", "type": "word"},
        {"name": "price", "type": "number"},
        {"name": "description", "type": "word"},
        {"name": "quantity", "type": "number"}
    ]

    num_lists = random.randint(1, 3)
    data = []

    for _ in range(num_lists):
        num_objects = random.randint(1, 9)
        current_list = []

        for _ in range(num_objects):
            obj = {}
            for field in fields:
                if random.choice([True, False]):
                    if field["type"] == "number":
                        obj[field["name"]] = random.randint(1, 5000)
                    elif field["type"] == "word":
                        obj[field["name"]] = random.choice(english_words)
            current_list.append(obj)

        data.append(current_list)

    return data

def save_json_file(data, folder="json_test_data"):
    existing_files = [f for f in os.listdir(folder) if f.startswith("data") and f.endswith(".json")]
    new_file_number = len(existing_files) + 1
    file_name = f"data{new_file_number}.json"

    with open(os.path.join(folder, file_name), "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Файл {file_name} успешно создан в папке {folder}!")

data = generate_random_data()
save_json_file(data)
