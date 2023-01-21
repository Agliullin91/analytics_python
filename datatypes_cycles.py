import math
import re


def task_1(word):
    n = len(word)/2
    if len(word) % 2 == 0:
        return word[int(n-1):int(n+1)]
    else:
        return word[math.floor(n)]


def task_2():
    summa = 0
    while True:
        number = input('Введите число: ')
        summa += int(number)
        if int(number) == 0:
            break
    return summa


def task_3(boys_list, girls_list):
    if len(boys_list) == len(girls_list):
        print('Идеальные пары:')
        for i in range(len(boys_list)):
            print(f'{sorted(boys_list)[i]} и {sorted(girls_list)[i]}')
    else:
        print('Внимание, кто-то может остаться без пары!')


def task_4(temp_list):
    print('Средняя температура в странах:')
    for i in temp_list:
        print(f'{i[0]} - {round((((math.fsum(i[1]) / len(i[1])) - 32) / 1.8), 1)} C')


def task_5(id_list):
    for i in id_list:
        valid_id = re.match(r'[ABCETYOPHKXMАВСУКНХРОМТ]{1}\d{3}[ABCETYOPHKXMАВСУКНХРОМТ]{2}\d{2,3}', i)
        if valid_id:
            print(f'Номер {i[:6]} валиден. Регион: {i[6:]}')
        else:
            print(f'Номер {i} не валиден')


def task_6(logs):
    unique_users = set()
    entries = 0
    for i in logs:
        unique_users.add(i.split(',')[0])
        entries += int(i.split(';')[1])
    return f'Среднее количество просмотров на уникального пользователя: {entries/len(unique_users)}'


if __name__ == "__main__":
    print(task_1('testing'))

    # print(task_2())

    boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
    girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
    task_3(boys, girls)

    countries_temperature = [
        ['Таиланд', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
        ['Германия', [57.2, 55.4, 59, 59, 53.6]],
        ['Россия', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
        ['Польша', [50, 50, 53.6, 57.2, 55.4, 55.4]]
    ]

    task_4(countries_temperature)

    car_ids = ['А222ВС96', 'АБ22ВВ193', 'A249MT177', 'M467XB98', 'NR221T177', 'B122KM102']

    task_5(car_ids)

    stream = [
        'user4,2021-01-01;3',
        'user3,2022-01-07;4',
        'user2,2022-03-29;1',
        'user1,2020-04-04;13',
        'user2,2022-01-05;7',
        'user1,2021-06-14;4',
        'user3,2022-07-02;10',
        'user4,2021-03-21;19',
        'user4,2022-03-22;4',
        'user4,2022-04-22;8',
        'user4,2021-05-03;9',
        'user4,2022-05-11;11'
    ]

    print(task_6(stream))