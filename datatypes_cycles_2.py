
def task_1(ids):
    unique_ids = set()
    for i in ids.values():
        for k in i:
            unique_ids.add(k)
    return unique_ids


def task_2(queries_list):
    queries_dict = dict()
    for i in queries_list:
        i_len = len(i.split(' '))
        if i_len not in queries_dict.keys():
            queries_dict[i_len] = 1
        else:
            k = queries_dict[i_len] + 1
            queries_dict[i_len] = k
    all_queries = sum(queries_dict.values())
    for query_len, value in queries_dict.items():
        print(f'Поисковых запросов, содержащих {query_len} слов(а): {round((value / all_queries)*100, 2)}%')


def task_3(results_dict):
    for value in results_dict.values():
        value['ROI'] = round((value['revenue'] / value['cost'] - 1) * 100, 2)
    return results_dict


def task_4(stats_dict):
    sorted_tuple = sorted(stats_dict.items(), key=lambda x: x[1], reverse=True)
    return f'Максимальный объем продаж на рекламном канале: {sorted_tuple[0][0]}'


def task_5(my_list):
    my_list.reverse()
    my_dict = my_list[0]
    for item in my_list[1::]:
        my_dict = {item: my_dict}
    return my_dict


def task_6(cook_book):
    portions = int(input('Введите количество порций: '))
    result = {}
    ingridients_list = cook_book.values()
    for item in ingridients_list:
        for i in item:
            if i['ingridient_name'] not in result.keys():
                result[i['ingridient_name']] = (i['quantity'] * portions, i['measure'])
            else:
                if i['measure'] != result.get(i['ingridient_name'])[1]:
                    result[i['ingridient_name'] + '_1'] = (i['quantity'] * portions, i['measure'])
                else:
                    result[i['ingridient_name']] = ((result.get(i['ingridient_name'])[0]) + int(i['quantity']) * portions, result.get(i['ingridient_name'])[1])
    pretty_list = []
    for key, value in result.items():
        pretty_list.append(f'{key.capitalize()}: {value[0]}, {value[1]}')
    return pretty_list


if __name__ == "__main__":
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}

    print(task_1(ids))

    queries = [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт']

    task_2(queries)

    results = {
        'vk': {'revenue': 103, 'cost': 98},
        'yandex': {'revenue': 179, 'cost': 153},
        'facebook': {'revenue': 103, 'cost': 110},
        'adwords': {'revenue': 35, 'cost': 34},
        'twitter': {'revenue': 11, 'cost': 24}}

    print(task_3(results))

    stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}

    print(task_4(stats))

    my_list = ['2018-01-01', 'yandex', 'cpc', 100]

    print(task_5(my_list))

    cook_book = {
        'салат': [
            {'ingridient_name': 'сыр', 'quantity': 50, 'measure': 'гр'},
            {'ingridient_name': 'томаты', 'quantity': 2, 'measure': 'шт'},
            {'ingridient_name': 'огурцы', 'quantity': 20, 'measure': 'гр'},
            {'ingridient_name': 'маслины', 'quantity': 10, 'measure': 'гр'},
            {'ingridient_name': 'оливковое масло', 'quantity': 20, 'measure': 'мл'},
            {'ingridient_name': 'салат', 'quantity': 10, 'measure': 'гр'},
            {'ingridient_name': 'перец', 'quantity': 20, 'measure': 'гр'}
        ],
        'пицца': [
            {'ingridient_name': 'сыр', 'quantity': 20, 'measure': 'гр'},
            {'ingridient_name': 'колбаса', 'quantity': 30, 'measure': 'гр'},
            {'ingridient_name': 'бекон', 'quantity': 30, 'measure': 'гр'},
            {'ingridient_name': 'оливки', 'quantity': 10, 'measure': 'гр'},
            {'ingridient_name': 'томаты', 'quantity': 20, 'measure': 'гр'},
            {'ingridient_name': 'тесто', 'quantity': 100, 'measure': 'гр'},
        ],
        'лимонад': [
            {'ingridient_name': 'лимон', 'quantity': 1, 'measure': 'шт'},
            {'ingridient_name': 'вода', 'quantity': 200, 'measure': 'мл'},
            {'ingridient_name': 'сахар', 'quantity': 10, 'measure': 'гр'},
            {'ingridient_name': 'лайм', 'quantity': 20, 'measure': 'гр'},
        ]
    }

    ingridients = task_6(cook_book)
    for item in ingridients:
        print(item)
