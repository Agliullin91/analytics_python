import pandas as pd

# Задание 1
# Скачайте с сайта датасет любого размера. Определите, какому фильму было выставлено больше всего оценок 5.0.


def most_rated(dataframe):
    return dataframe[ dataframe.rating == 5.0 ]['movieId'].value_counts().head(1)

# Задание 2
# По данным файла power.csv посчитайте суммарное потребление стран Прибалтики (Латвия, Литва и Эстония)
# категорий 4, 12 и 21 за период с 2005 по 2010 год. Не учитывайте в расчётах отрицательные значения quantity.


def most_consume(dataframe):
    baltic = dataframe[ (dataframe['country'] == 'Latvia') | (dataframe['country'] == 'Lithuania') |
                        (dataframe['country'] == 'Estonia')]
    return baltic[baltic['category'].isin([4, 12, 21]) & baltic['year'].isin(range(2005, 2011)) &
                  baltic['quantity'] > 0].head()
# Задание 3
# Выберите страницу любого сайта с табличными данными. Импортируйте таблицы в pandas DataFrame.
# Вы можете взять любые страницы.


if __name__ == '__main__':
    ratings = pd.read_csv('datasets/ratings.csv')
    print(ratings.info())
    print(most_rated(ratings))

    power = pd.read_csv('datasets/power.csv')
    print(power.info())
    print(most_consume(power))

    table = pd.read_html('https://fortrader.org/quotes')

    # ImportError: lxml not found, please install it

    # Successfully built lxml
    # Installing collected packages: lxml
    # Successfully installed lxml - 4.9.2
