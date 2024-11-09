import json

translator = {
'bug':'ошибка',
'function':'функция',
'approve':'согласовать'
}
# преобразовываем словарь в json
translator_json = json.dumps(translator)
# записываем полученную строку в файл
with open("translator1.json", "w") as my_file:
    my_file.write(translator_json)