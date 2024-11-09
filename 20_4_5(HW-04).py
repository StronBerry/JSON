import json

# Чтение данных из JSON-файла
with open("orders_july_2023.json", "r", encoding="utf-8") as file:
    orders = json.load(file)

# 1. Номер самого дорогого заказа и его сумма
most_expensive_order_number = None
max_price = 0
for order_number, details in orders.items():
    if details['price'] > max_price:
        max_price = details['price']
        most_expensive_order_number = order_number
print(f"Номер самого дорогого заказа: {most_expensive_order_number}, сумма: {max_price}")

# 2. Номер заказа с самым большим количеством товаров и их количество
most_quantity_order_number = None
max_quantity = 0
for order_number, details in orders.items():
    if details['quantity'] > max_quantity:
        max_quantity = details['quantity']
        most_quantity_order_number = order_number
print(f"Номер заказа с наибольшим количеством товаров: {most_quantity_order_number}, количество товаров: {max_quantity}")

# 3. День с наибольшим количеством заказов и общая сумма заказов в этот день
date_order_count = {}
date_total_sum = {}

for details in orders.values():
    date = details['date']
    price = details['price']

    if date in date_order_count:
        date_order_count[date] += 1
        date_total_sum[date] += price
    else:
        date_order_count[date] = 1
        date_total_sum[date] = price

most_orders_date = max(date_order_count, key=date_order_count.get)
most_orders_count = date_order_count[most_orders_date]
total_sum_on_most_orders_date = date_total_sum[most_orders_date]

print(
    f"День с наибольшим количеством заказов: {most_orders_date}, количество заказов: {most_orders_count}, общая сумма: {total_sum_on_most_orders_date}")

#Первый вариант пункта 4 приводил к тому, что в консоли выводился полный список ID пользователей,
# так как все они сделали по 1 заказу исходя из данных "orders_july_2023.json".

# # 4. Пользователь, сделавший наибольшее количество заказов, и количество его заказов
# user_order_count = {}
# for details in orders.values():
#     user_id = details['user_id']
#     if user_id in user_order_count:
#         user_order_count[user_id] += 1
#     else:
#         user_order_count[user_id] = 1
# most_active_user = max(user_order_count, key=user_order_count.get)
# most_active_user_orders = user_order_count[most_active_user]
# print(f"Пользователь с наибольшим количеством заказов: {most_active_user}, количество заказов: {most_active_user_orders}")

#Второй вариант пункта 4

# 4. Пользователи, сделавшие наибольшее количество заказов
user_order_count = {}
for details in orders.values():
    user_id = details['user_id']
    if user_id in user_order_count:
        user_order_count[user_id] += 1
    else:
        user_order_count[user_id] = 1

# Находим уникальные значения количества заказов
unique_order_counts = set(user_order_count.values())

if len(unique_order_counts) == 1:
    # Если пользователи имеют одинаковое количество заказов
    common_order_count = unique_order_counts.pop()
    print(f"В данном месяце все пользователи совершили одинаковое количество заказов: {common_order_count}")
else:
    # Максимальное количество заказов и собираем пользователей с этим количеством
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
top_spender_user = max(user_total_spending, key=user_total_spending.get)
top_spender_total = user_total_spending[top_spender_user]
print(f"Пользователь с самой большой суммарной стоимостью заказов: {top_spender_user}, общая сумма: {top_spender_total}")

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