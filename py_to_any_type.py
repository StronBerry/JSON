import json

translator = {
'bugs':'ошибка',
'function':'функция',
'approve':'согласовать'
}

with open("translator2.txt", "w") as my_file:
# преобразовываем словарь в json и записываем в файл
    json.dump(translator, my_file)