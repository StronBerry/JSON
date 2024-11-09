import json

with open("orders_july_2023.json", "r", encoding="utf-8") as file:
    orders = json.load(file)

# 1. Номер самого дорогого заказа и его сумма
most_expensive_order_number = None
max_price = 0
for order_number, details in orders.items():
    if details['price'] > max_price:
        max_price = details['price']
        most_expensive_order_number = [order_number]  # начинаем список с одного заказа
    elif details['price'] == max_price:
        most_expensive_order_number.append(order_number)  # добавляем еще один заказ в список, если стоимость одинаковая

# Если только один заказ с наибольшей стоимостью
if len(most_expensive_order_number) == 1:
    print(f"Номер самого дорогого заказа: {most_expensive_order_number[0]}, сумма: {max_price}")
else:
    # Если несколько заказов с одинаковой максимальной стоимостью
    print(f"Количество заказов с наибольшей стоимостью: {len(most_expensive_order_number)}, сумма: {max_price} список заказов: {', '.join(most_expensive_order_number)}")


# 2. Номер заказа с наибольшим количеством товаров и их количество
most_quantity_order_number = None
max_quantity = 0
for order_number, details in orders.items():
    if details['quantity'] > max_quantity:
        max_quantity = details['quantity']
        most_quantity_order_number = [order_number]  # начинаем список с одного заказа
    elif details['quantity'] == max_quantity:
        most_quantity_order_number.append(order_number)  # добавляем еще один заказ в список, если количество товаров одинаково

# Если только один заказ с наибольшим количеством товаров
if len(most_quantity_order_number) == 1:
    print(f"Номер заказа с наибольшим количеством товаров: {most_quantity_order_number[0]}, количество товаров: {max_quantity}")
else:
    # Если несколько заказов с одинаковым количеством товаров
    print(f"Количество заказов с наибольшим количеством товаров: {len(most_quantity_order_number)}, список таких заказов: {', '.join(most_quantity_order_number)}, количество товаров: {max_quantity}")


# # 3. День с наибольшим количеством заказов и количество заказов в этот день
# date_order_count = {}
# for details in orders.values():
#     date = details['date']
#     if date in date_order_count:
#         date_order_count[date] += 1
#     else:
#         date_order_count[date] = 1
# most_orders_date = max(date_order_count, key=date_order_count.get)
# most_orders_count = date_order_count[most_orders_date]
# print(f"День с наибольшим количеством заказов: {most_orders_date}, количество заказов: {most_orders_count}")

# 3. День с наибольшим количеством заказов и количество заказов в этот день
date_order_count = {}
for details in orders.values():
    date = details['date']
    if date in date_order_count:
        date_order_count[date] += 1
    else:
        date_order_count[date] = 1

# Максимальное количество заказов в день
max_orders_in_a_day = max(date_order_count.values())

# Все дни с этим максимальным количеством заказов
days_with_max_orders = [date for date, count in date_order_count.items() if count == max_orders_in_a_day]

# Если только один день с наибольшим количеством заказов
if len(days_with_max_orders) == 1:
    print(f"День с наибольшим количеством заказов: {days_with_max_orders[0]}, количество заказов: {max_orders_in_a_day}")
else:
    # Если несколько дней с одинаковым количеством заказов
    print(f"Количество дней с наибольшим количеством заказов: {len(days_with_max_orders)}")
    print(f"Дни с наибольшим количеством заказов: {', '.join(days_with_max_orders)}, количество заказов: {max_orders_in_a_day}")


# 4. Пользователи, сделавшие наибольшее количество заказов
user_order_count = {}
for details in orders.values():
    user_id = details['user_id']
    if user_id in user_order_count:
        user_order_count[user_id] += 1
    else:
        user_order_count[user_id] = 1

unique_order_counts = set(user_order_count.values())

if len(unique_order_counts) == 1:
    # Все пользователи имеют одинаковое количество заказов
    common_order_count = unique_order_counts.pop()
    print(f"В данном месяце все пользователи совершили одинаковое количество заказов: {common_order_count}")
else:
    # Находим максимальное количество заказов и собираем пользователей с этим количеством
    max_orders = max(unique_order_counts)
    most_active_users = [user_id for user_id, count in user_order_count.items() if count == max_orders]
    print(f"Пользователь(и) с наибольшим количеством заказов: {most_active_users}, количество заказов: {max_orders}")

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
    # Если только один пользователь с максимальной суммой
    print(f"Пользователь с самой большой суммарной стоимостью заказов: {top_spender_users[0]}, общая сумма: {top_spender_total}")
else:
    # Если несколько пользователей с одинаковой суммой
    print(f"Пользователи с самой большой суммарной стоимостью заказов: {', '.join(top_spender_users)}, сумма: {top_spender_total}")


# 6. Средняя стоимость заказа
total_price = 0
order_count = 0
for details in orders.values():
    total_price += details['price']
    order_count += 1
average_order_price = total_price / order_count if order_count > 0 else 0
print(f"Средняя стоимость заказа: {average_order_price:.2f}")

# 7. Средняя стоимость товаров
total_items = 0
total_spent = 0
for details in orders.values():
    total_items += details['quantity']
    total_spent += details['price']
average_item_price = total_spent / total_items if total_items > 0 else 0
print(f"Средняя стоимость товаров: {average_item_price:.2f}")

