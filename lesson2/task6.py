'''
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
'''


features = []

name = None
price = None
quantity = None
unit = None
finish = "n"
q = "y"
while finish != q:
    if name is None:
        ask = input('Введите название товара: ')
        if not ask.isalnum():
            print('Название!')
            continue
        name = ask

    if price is None:
        ask = input('Введите стоимость товара: ')
        if not ask.isdigit():
            print('Неверно, давай без копеек.')
            continue
        price = ask

    if quantity is None:
        ask = input('Введите количество: ')
        if not ask.isdigit():
            print('Можно только целое число.')
            continue
        quantity = ask

    if unit is None:
        ask = input('Введите единицы измерения: ')
        if not ask.isalpha():
            print('Неверно.')
            continue
        unit = ask

    features.append({'name': name, 'price': price, 'quantity': quantity, 'unit': unit})
    for ind, line in enumerate(features, 1):
        print(ind, line)
    name = None
    price = None
    quantity = None
    unit = None

    q = input('Подолжаем? (y/n)) ').lower()

analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}

for item in features:
    analytics['name'].append(item['name'])
    analytics['price'].append(item['price'])
    analytics['quantity'].append(item['quantity'])
    analytics['unit'].append(item['unit'])

for line in analytics.items():
    print(line)
