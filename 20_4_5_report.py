import json
import os
from datetime import datetime

# Чтение данных из JSON-файла
with open("orders_july_2023.json", "r", encoding="utf-8") as file:
    orders = json.load(file)

# Формирование вывода в переменную
output = ""

# 1. Номер самого дорогого заказа и его сумма
most_expensive_order_number = None
max_price = 0
for order_number, details in orders.items():
    if details['price'] > max_price:
        max_price = details['price']
        most_expensive_order_number = [order_number]  # начинаем список с одного заказа
    elif details['price'] == max_price:
        most_expensive_order_number.append(order_number)  # добавляем еще один заказ в список, если стоимость одинаковая

if len(most_expensive_order_number) == 1:
    output += f"Номер самого дорогого заказа: {most_expensive_order_number[0]}, сумма: {max_price}\n"
else:
    output += f"Количество заказов с наибольшей стоимостью: {len(most_expensive_order_number)}, сумма: {max_price} список заказов: {', '.join(most_expensive_order_number)}\n"

# 2. Номер заказа с наибольшим количеством товаров и их количество
most_quantity_order_number = None
max_quantity = 0
for order_number, details in orders.items():
    if details['quantity'] > max_quantity:
        max_quantity = details['quantity']
        most_quantity_order_number = [order_number]  # начинаем список с одного заказа
    elif details['quantity'] == max_quantity:
        most_quantity_order_number.append(order_number)  # добавляем еще один заказ в список, если количество товаров одинаково

if len(most_quantity_order_number) == 1:
    output += f"Номер заказа с наибольшим количеством товаров: {most_quantity_order_number[0]}, количество товаров: {max_quantity}\n"
else:
    output += f"Количество заказов с наибольшим количеством товаров: {len(most_quantity_order_number)}, список таких заказов: {', '.join(most_quantity_order_number)}, количество товаров: {max_quantity}\n"

# 3. День с наибольшим количеством заказов и количество заказов в этот день
date_order_count = {}
for details in orders.values():
    date = details['date']
    if date in date_order_count:
        date_order_count[date] += 1
    else:
        date_order_count[date] = 1

max_orders_in_a_day = max(date_order_count.values())
days_with_max_orders = [date for date, count in date_order_count.items() if count == max_orders_in_a_day]

if len(days_with_max_orders) == 1:
    output += f"День с наибольшим количеством заказов: {days_with_max_orders[0]}, количество заказов: {max_orders_in_a_day}\n"
else:
    output += f"Количество дней с наибольшим количеством заказов: {len(days_with_max_orders)}\n"
    output += f"Дни с наибольшим количеством заказов: {', '.join(days_with_max_orders)}, количество заказов: {max_orders_in_a_day}\n"

# 4. Пользователи с наибольшим количеством заказов
user_order_count = {}
for details in orders.values():
    user_id = details['user_id']
    if user_id in user_order_count:
        user_order_count[user_id] += 1
    else:
        user_order_count[user_id] = 1

unique_order_counts = set(user_order_count.values())

if len(unique_order_counts) == 1:
    common_order_count = unique_order_counts.pop()
    output += f"В данном месяце все пользователи совершили одинаковое количество заказов: {common_order_count}\n"
else:
    max_orders = max(unique_order_counts)
    most_active_users = [user_id for user_id, count in user_order_count.items() if count == max_orders]
    output += f"Пользователь(и) с наибольшим количеством заказов: {most_active_users}, количество заказов: {max_orders}\n"

# 5. Пользователь с самой большой суммарной стоимостью заказов и общая сумма
user_total_spending = {}
for details in orders.values():
    user_id = details['user_id']
    price = details['price']
    if user_id in user_total_spending:
        user_total_spending[user_id] += price
    else:
        user_total_spending[user_id] = price

top_spender_total = max(user_total_spending.values())
top_spender_users = [str(user_id) for user_id, total in user_total_spending.items() if total == top_spender_total]

if len(top_spender_users) == 1:
    output += f"Пользователь с самой большой суммарной стоимостью заказов: {top_spender_users[0]}, общая сумма: {top_spender_total}\n"
else:
    output += f"Пользователи с самой большой суммарной стоимостью заказов: {', '.join(top_spender_users)}, сумма: {top_spender_total}\n"

# 6. Средняя стоимость заказа
total_price = 0
order_count = 0
for details in orders.values():
    total_price += details['price']
    order_count += 1
average_order_price = total_price / order_count if order_count > 0 else 0
output += f"Средняя стоимость заказа: {average_order_price:.2f}\n"

# 7. Средняя стоимость товаров
total_items = 0
total_spent = 0
for details in orders.values():
    total_items += details['quantity']
    total_spent += details['price']
average_item_price = total_spent / total_items if total_items > 0 else 0
output += f"Средняя стоимость товаров: {average_item_price:.2f}\n"

# Сохранение результата в файл
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
report_filename = f"Reports/report_{current_time}.txt"

# Убедимся, что директория существует
os.makedirs(os.path.dirname(report_filename), exist_ok=True)

# Запись в файл
with open(report_filename, "w", encoding="utf-8") as report_file:
    report_file.write(output)

print(output)  # Печатаем вывод в консоль для наглядности
