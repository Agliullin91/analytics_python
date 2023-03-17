import pandas as pd
from urllib import parse
import re

# Задание 1
# Для датафрейма log из материалов занятия создайте столбец source_type по правилам:
# если источник traffic_source равен Yandex или Google, то в source_type ставится organic;
# для источников paid и email из России ставим ad;
# для источников paid и email не из России ставим other;
# все остальные варианты берём из traffic_source без изменений.


def source_type(row):
    if row['traffic_source'] == 'yandex' or row['traffic_source'] == 'google':
        return 'organic'
    elif (row['traffic_source'] == 'paid' and row['region'] == 'Russia') or (row['traffic_source'] == 'email' and row['region'] == 'Russia'):
        return 'ad'
    elif row['traffic_source'] == 'paid' or row['traffic_source'] == 'email':
        return 'other'
    return row['traffic_source']

# Задание 2
# В файле URLs.txt содержатся URL страниц новостного сайта. Вам нужно отфильтровать его по адресам страниц с текстами
# новостей. Известно, что шаблон страницы новостей имеет внутри URL конструкцию: /, затем 8 цифр, затем дефис.
# Выполните действия:
# Прочитайте содержимое файла с датафрейм.
# Отфильтруйте страницы с текстом новостей, используя метод str.contains и регулярное выражение в соответствие с
# заданным шаблоном.

# Задание 3
# Используйте файл с оценками фильмов ml-latest-small/ratings.csv. Посчитайте среднее время жизни пользователей, которые
# выставили более 100 оценок. Под временем жизни понимается разница между максимальным и минимальным значениями столбца
# timestamp для данного значения userId.

# Задание 4
# Дана статистика услуг перевозок клиентов компании по типам (см. файл “Python_13_join.ipynb” в разделе «Материалы
# для лекции “Продвинутый pandas”» ---- Ноутбуки к лекции «Продвинутый pandas»).
# Нужно сформировать две таблицы:
# таблицу с тремя типами выручки для каждого client_id без указания адреса клиента;
# аналогичную таблицу по типам выручки с указанием адреса клиента.


if __name__ == '__main__':
    pd.set_option('display.max_columns', None)

    log = pd.read_csv('datasets/visit_log.csv', sep=';')
    print(log.info())
    log['source_type'] = log.loc[:, ['traffic_source', 'region']].apply(source_type, axis=1)
    print(log[['traffic_source', 'region', 'source_type']].head(25))

    # 6 paid Russia ad
    # 7 direct Russia direct
    # 8 direct China direct
    # 9 email Russia ad
    # 10 direct India direct
    # 11 google Ukraine organic
    # 12 paid Russia ad
    # 13 direct China direct
    # 14 direct Belarus direct
    # 15 paid Belarus other

    news = pd.read_csv('datasets/URLs.txt', sep=r'^')
    print(news.info())
    print(news[news.url.str.contains(r'\/\d{8}-')].head())

    #     url
    # 3 / politics / 36188461 - s - marta - zhizn - rossiyan - susc...
    # 4 / world / 36007585 - tramp - pridumal - kak - reshit - ukra...
    # 5 / science / 36157853 - nasa - sobiraet - ekstrennuyu - pr...
    # 6 / video / 36001498 - poyavilis - pervye - podrobnosti - g...
    # 7 / world / 36007585 - tramp - pridumal - kak - reshit - ukra...

    ratings = pd.read_csv('datasets/ratings.csv')
    print(ratings.info())
    minmax_rat = ratings.groupby('userId').agg({'timestamp': ['min', 'max']})
    print(minmax_rat.info())
    minmax_rat['lifetime'] = minmax_rat['timestamp']['max'] - minmax_rat['timestamp']['min']
    print(minmax_rat.head())

    #     timestamp lifetime
    #     min max
    # userId
    # 1 964980499 965719662 739163
    # 2 1445714835 1445715340 505
    # 3 1306463323 1306464293 970
    # 4 945078428 1007574542 62496114
    # 5 847434747 847435337 590

    rzd = pd.DataFrame(
        {
            'client_id': [111, 112, 113, 114, 115],
            'rzd_revenue': [1093, 2810, 10283, 5774, 981]
        }
    )
    auto = pd.DataFrame(
        {
            'client_id': [113, 114, 115, 116, 117],
            'auto_revenue': [57483, 83, 912, 4834, 98]
        }
    )
    air = pd.DataFrame(
        {
            'client_id': [115, 116, 117, 118],
            'air_revenue': [81, 4, 13, 173]
        }
    )
    client_base = pd.DataFrame(
        {
            'client_id': [111, 112, 113, 114, 115, 116, 117, 118],
            'address': ['Комсомольская 4', 'Энтузиастов 8а', 'Левобережная 1а', 'Мира 14', 'ЗЖБИиДК 1',
                        'Строителей 18', 'Панфиловская 33', 'Мастеркова 4']
        }
    )

    full_table = client_base.merge(air, on='client_id', how='left')\
        .merge(auto, on='client_id', how='left').merge(rzd, on='client_id', how='left')
    print(full_table.head(10))

    # client_id address air_revenue auto_revenue rzd_revenue
    # 0 111 Комсомольская 4 NaN NaN 1093.0
    # 1 112 Энтузиастов 8а NaN NaN 2810.0
    # 2 113 Левобережная 1а NaN 57483.0 10283.0
    # 3 114 Мира 14 NaN 83.0 5774.0
    # 4 115 ЗЖБИиДК 1 81.0 912.0 981.0
    # 5 116 Строителей 18 4.0 4834.0 NaN
    # 6 117 Панфиловская 33 13.0 98.0 NaN
    # 7 118 Мастеркова 4 173.0 NaN NaN

    f_table = air.merge(auto, on='client_id', how='outer').merge(rzd, on='client_id', how='outer')
    print(f_table.sort_values('client_id').head(10))

    #    client_id  air_revenue  auto_revenue  rzd_revenue
    # 6        111          NaN           NaN       1093.0
    # 7        112          NaN           NaN       2810.0
    # 4        113          NaN       57483.0      10283.0
    # 5        114          NaN          83.0       5774.0
    # 0        115         81.0         912.0        981.0
    # 1        116          4.0        4834.0          NaN
    # 2        117         13.0          98.0          NaN
    # 3        118        173.0           NaN          NaN
