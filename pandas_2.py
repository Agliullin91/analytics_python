import pandas as pd
import re

# Задание 1
# Напишите функцию, которая классифицирует фильмы из материалов занятия по правилам:
# оценка 2 и ниже — низкий рейтинг;
# оценка 4 и ниже — средний рейтинг;
# оценка 4.5 и 5 — высокий рейтинг.
# Результат классификации запишите в столбец class.


def movie_class(rating: float):
    if rating <= 2.0:
        return 'Low rating'
    elif rating <= 4.0:
        return 'Medium rating'
    return 'High rating'

# Задание 2
# Используйте файл keywords.csv.
# Нужно написать гео-классификатор, который каждой строке сможет выставить географическую принадлежность определённому
# региону. Т. е. если поисковый запрос содержит название города региона, то в столбце ‘region’ пишется название этого
# региона. Если поисковый запрос не содержит названия города, то ставим ‘undefined’.
# Правила распределения по регионам Центр, Северо-Запад и Дальний Восток:

# Результат классификации запишите в отдельный столбец region.


def region(keyword):
    geo_data = {
    'Центр': ['москва', 'тула', 'ярославль'],
    'Северо-Запад': ['петербург', 'псков', 'мурманск'],
    'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']
    }
    for item in keyword.split(' '):
        if item in geo_data['Центр']:
            return 'Центр'
        elif item in geo_data['Северо-Запад']:
            return 'Северо-Запад'
        elif item in geo_data['Дальний Восток']:
            return 'Дальний восток'
    return 'undefined'

# Задание 3 (бонусное)
# Есть мнение, что раньше снимали настоящее кино, не то что сейчас. Ваша задача — проверить это утверждение, используя
# файлы с рейтингами фильмов из прошлого домашнего занятия: файл movies.csv и ratings.csv из базы. Нужно проверить, верно
# ли, что с ростом года выпуска фильма его средний рейтинг становится ниже.
# Вы не будете затрагивать субьективные факторы выставления этих рейтингов, а пройдётесь по алгоритму:
# В переменную years запишите список из всех годов с 1950 по 2010 года.
# Напишите функцию production_year, которая каждой строке из названия фильма выставляет год выпуска.
# Не все названия фильмов содержат год выпуска в одинаковом формате, поэтому используйте алгоритм:
# для каждой строки пройдите по всем годам списка years;
# если номер года присутствует в названии фильма, то функция возвращает этот год, как год выпуска;
# если ни один из номеров года списка years не встретился в названии фильма, то возвращается 1900 год.
# Запишите год выпуска фильма по алгоритму пункта 2 в новый столбец ‘year’.
# Посчитайте средний рейтинг всех фильмов для каждого значения столбца ‘year’ и отсортируйте результат по
# убыванию рейтинга.


def production_year(title):
    years = range(1950, 2010)
    title_year = re.search(r'\(\d{4}\)', title)
    if title_year:
        for year in years:
            if str(year) in title_year[0]:
                return year
    return 1900


if __name__ == '__main__':
    pd.set_option('display.max_columns', None)

    rating = pd.read_csv('datasets/ratings.csv')
    print(rating.info())
    rating['class'] = rating['rating'].apply(movie_class)
    print(rating['class'].value_counts().head())

    # Medium rating 65551
    # High rating 21762
    # Low rating 13523
    # Name: class , dtype: int64

    keywords = pd.read_csv('datasets/keywords.csv')
    print(keywords.info())
    keywords['region'] = keywords['keyword'].apply(region)
    print(keywords[ keywords.keyword.isin(['москва', 'псков', 'сахалин', 'ютуб'])].head())

    #     keyword shows region
    # 3 ютуб 39995567 undefined
    # 1259 москва 153050 Центр
    # 11222 псков 24885 Северо - Запад
    # 21445 сахалин 14494 Дальний восток

    movie = pd.read_csv('datasets/movies.csv')
    movie['year'] = movie['title'].apply(production_year)
    print(movie[['title', 'year']].sort_values('year').head())
    full_table = movie.merge(rating, left_on='movieId', right_on='movieId')
    print(full_table.groupby('year').agg('mean', numeric_only=True)['rating'].sort_values(ascending=False).head())

    # year
    # 1957 4.039535
    # 1954 4.009191
    # 1962 3.969466
    # 1952 3.953125
    # 1964 3.940160
    # Name: rating, dtype: float64
