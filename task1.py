import json

# Создаем словарь
purchases = {}

# Открываем файл и читаем первые 6 строк (1 строка заголовок + 5 строк данных)
with open('Downloads/purchase_log.txt', encoding='utf-8') as f:
    # Пропускаем первую строку с заголовками
    next(f)
    # Читаем следующие 5 строк
    for i in range(5):
        line = f.readline()  # Читаем одну строку из файла и сохраняем ее в переменную 'line'
        # Преобразуем строку JSON в словарь Python
        record = json.loads(line)
        # Добавляем в словарь purchases новую запись, где ключом является user_id, а значением - category
        purchases[record['user_id']] = record['category']  

# Смотрим что получилось
print(purchases)
