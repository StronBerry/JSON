import json

# import json
# # открываем файл в режиме чтения
# with open("translator.json", "r") as my_file:
#     translator_json = my_file.read()
# # преобразовываем строку json в словарь
# translator = json.loads(translator_json)
# print(translator)


# Open the file and load JSON directly as a dictionary
with open("translator.json", "r") as my_file:
    translator = json.load(my_file)  # directly loads JSON into a dictionary

print(translator)

