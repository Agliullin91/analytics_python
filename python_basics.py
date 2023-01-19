import random
import math


def task_1(str1, str2):
    if len(str1) == len(str2):
        return 'Фразы равной длинны'
    elif len(str1) > len(str2):
        return 'Фраза 1 длиннее фразы 2'
    else:
        return 'Фраза 2 длиннее фразы 1'


def task_2(year):
    if year % 4 == 0 or year % 100 == 0:
        return f'{year} год високосный'
    else:
        return f'{year} год обычный'


def _task_3_date_check(input_day, separator_day, zodiac1, zodiac2):
    if input_day <= separator_day:
        return zodiac1
    else:
        return zodiac2


def task_3():
    month = input('Month: ')
    day = input('Day: ')
    if month == 'jan':
        return _task_3_date_check(int(day), 20, 'Козерог', 'Водолей')
    if month == 'feb':
        return _task_3_date_check(int(day), 19, 'Водолей', 'Рыбы')
    if month == 'mar':
        return _task_3_date_check(int(day), 20, 'Рыбы', 'Овен')
    if month == 'apr':
        return _task_3_date_check(int(day), 20, 'Овен', 'Телец')
    if month == 'may':
        return _task_3_date_check(int(day), 21, 'Телец', 'Близнецы')
    if month == 'jun':
        return _task_3_date_check(int(day), 21, 'Близнецы', 'Рак')
    if month == 'jul':
        return _task_3_date_check(int(day), 22, 'Рак', 'Лев')
    if month == 'aug':
        return _task_3_date_check(int(day), 23, 'Лев', 'Дева')
    if month == 'sep':
        return _task_3_date_check(int(day), 22, 'Дева', 'Весы')
    if month == 'oct':
        return _task_3_date_check(int(day), 22, 'Весы', 'Скорпион')
    if month == 'nov':
        return _task_3_date_check(int(day), 22, 'Скорпион', 'Стрелец')
    if month == 'dec':
        return _task_3_date_check(int(day), 21, 'Стрелец', 'Козерог')


def task_4(width, height,length):
    if width <= 15 and height <= 15 and length <= 15:
        return 'Коробка №1'
    elif 15 < width <= 50 or 15 < height <= 50 or 15 < length <= 50:
        return 'Коробка №2'
    elif width >= 200 or height >= 200 or length >= 200:
        return 'Упаковка для лыж'
    else:
        return 'Коробка №3'


def task_5(ticket_number):
    string_num = str(ticket_number)
    part1 = int(string_num[0]) + int(string_num[1]) + int(string_num[2])
    part2 = int(string_num[3]) + int(string_num[4]) + int(string_num[5])
    if part1 == part2:
        return 'Счастливый билет'
    else:
        return 'Несчастливый билет'


def task_6():
    fig = input('Укажите фигуру(c,r,t): ')
    if fig == 'c':
        r = input('Введите радиус круга: ')
        return f'Площадь круга: {math.pi * (int(r)^2)}'
    if fig == 'r':
        a = input('Укажите длину прямоугольника: ')
        b = input('Укажите ширину прямоугольника: ')
        return f'Площадь прямоугольника: {int(a) * int(b)}'
    if fig == 't':
        a = input('Укажите сторону а треугольника: ')
        b = input('Укажите сторону б треугольника: ')
        c = input('Укажите сторону ц треугольника: ')
        p = (int(a) + int(b) + int(c))/2
        return f'Площадь треугольника: {math.sqrt(p*(p-int(a)) * (p-int(b)) * (p-int(c)))}'


if __name__ == "__main__":
    phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
    phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
    print(task_1(phrase_1, phrase_2))

    for i in range(1978, 2024):
        print(task_2(i))

    print(task_3())

    for i in range(0, 25):
        print(i, task_4(random.randint(1, 250), random.randint(1, 100), random.randint(1, 100)))

    print(task_5(121112))

    # print(task_6())