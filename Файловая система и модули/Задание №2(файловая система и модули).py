import json

# Создаем словарь покупок из purchase_log.txt
purchases = {}
with open('Downloads/purchase_log.txt', encoding='utf-8') as f:
    next(f)  # пропускаем заголовок
    for line in f:
        record = json.loads(line)
        purchases[record['user_id']] = record['category']

# Создаем funnel.csv и записываем в него данные
with open('Downloads/visit_log.csv') as visits, \
     open('Downloads/funnel.csv', 'w') as funnel:
    
    # Записываем заголовок
    funnel.write('user_id,source,category\n')
    
    # Пропускаем заголовок в visit_log.csv
    next(visits)
    
    # Обрабатываем каждую строку из visit_log.csv
    for line in visits:
        user_id, source = line.strip().split(',')
        
        # Если пользователь есть в словаре purchases, записываем информацию в funnel.csv
        if user_id in purchases:
            funnel.write(f'{user_id},{source},{purchases[user_id]}\n')
