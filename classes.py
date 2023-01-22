import requests
from pprint import pprint


# Задание 1
class Money:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(url)
        self.resp_json = self.response.json()

    def show_currency(self):
        valutes = self.resp_json['Valute']
        pprint(valutes)

    def most_valuable(self):
        valutes = self.resp_json['Valute']
        valutes_tuple = tuple()
        for item in valutes.values():
            valutes_tuple = valutes_tuple + ((item.get('Name'), item.get('Value')),)
        sorted_tuple = sorted(valutes_tuple, key=lambda x: x[1], reverse=True)
        return f'{sorted_tuple[0][0]}: {sorted_tuple[0][1]}'

    def usd(self, diff=False):
        valutes = self.resp_json['Valute']
        if diff:
            return f"{valutes.get('USD').get('Name')}: {valutes.get('USD').get('Previous') - valutes.get('USD').get('Value')}"
        else:
            return f"{valutes.get('USD').get('Name')}: {valutes.get('USD').get('Value')}"

    def eur(self, diff=False):
        valutes = self.resp_json['Valute']
        if diff:
            return f"{valutes.get('EUR').get('Name')}: {valutes.get('EUR').get('Previous') - valutes.get('EUR').get('Value')}"
        else:
            return f"{valutes.get('EUR').get('Name')}: {valutes.get('EUR').get('Value')}"

    def gbp(self, diff=False):
        valutes = self.resp_json['Valute']
        if diff:
            return f"{valutes.get('GBP').get('Name')}: {valutes.get('GBP').get('Previous') - valutes.get('GBP').get('Value')}"
        else:
            return f"{valutes.get('GBP').get('Name')}: {valutes.get('GBP').get('Value')}"


# Задание 2
class Rate:
    def __init__(self, format_='value', diff=False):
        self.format = format_
        self.diff = diff

    def exchange_rates(self):
        """
        Возвращает ответ сервиса с информацией о валютах в виде:

        {
            'AMD': {
                'CharCode': 'AMD',
                'ID': 'R01060',
                'Name': 'Армянских драмов',
                'Nominal': 100,
                'NumCode': '051',
                'Previous': 14.103,
                'Value': 14.0879
                },
            ...
        }
        """
        self.r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return self.r.json()['Valute']

    def make_format(self, currency):
        """
        Возвращает информацию о валюте currency в двух вариантах:
        - полная информация о валюте при self.format = 'full':
        Rate('full').make_format('EUR')
        {
            'CharCode': 'EUR',
            'ID': 'R01239',
            'Name': 'Евро',
            'Nominal': 1,
            'NumCode': '978',
            'Previous': 79.6765,
            'Value': 79.4966
        }

        Rate('value').make_format('EUR')
        79.4966
        """
        response = self.exchange_rates()

        if currency in response:
            if self.format == 'full':
                return response[currency]

            if self.format == 'value':
                return response[currency]['Value']

        return 'Error'

    def eur(self):
        """Возвращает курс евро на сегодня в формате self.format"""
        if self.diff is True and self.format == 'value':
            response = self.exchange_rates()
            return f"Изменение курса: {response['EUR']['Value'] - response['EUR']['Previous']}"
        return self.make_format('EUR')

    def usd(self):
        """Возвращает курс доллара на сегодня в формате self.format"""
        return self.make_format('USD')

    def brl(self):
        """Возвращает курс бразильского реала на сегодня в формате self.format"""
        return self.make_format('BRL')


# Задание 3
class Employee:
    def __init__(self, name, seniority):
        self.name = name
        self.seniority = seniority
        self.grade = 1

    def grade_up(self):
        """Повышает уровень сотрудника"""
        self.grade += 1

    def publish_grade(self):
        """Публикация результатов аккредитации сотрудников"""
        print(self.name, self.grade)


class Developer(Employee):
    def __init__(self, name, seniority):
        super().__init__(name, seniority)

    def check_if_it_is_time_for_upgrade(self):
        # для каждой аккредитации увеличиваем счетчик на 1
        # пока считаем, что все разработчики проходят аккредитацию
        self.seniority += 1

        # условие повышения сотрудника из презентации
        if self.seniority % 5 == 0:
            self.grade_up()

        # публикация результатов
        return self.publish_grade()


class Designer(Employee):
    def __init__(self, name, seniority):
        super().__init__(name, seniority)

    def check_if_it_is_time_for_upgrade(self):
        self.seniority += 1

        if self.seniority % 7 == 0:
            self.grade_up()

        return self.publish_grade()

    def getting_international_trophy(self):
        self.seniority += 2

        if self.seniority % 7 == 0:
            self.grade_up()

        return self.publish_grade()


if __name__ == "__main__":
    cbr = Money('https://www.cbr-xml-daily.ru/daily_json.js')
    cbr.show_currency()
    print(cbr.most_valuable())
    print(cbr.usd(diff=True))
    print(cbr.eur(diff=True))
    print('\n================================')
    test_rate = Rate(format_='value', diff=True)
    print(test_rate.eur())
    test_rate_1 = Rate(format_='full', diff=True)
    print(test_rate_1.eur())
    test_rate_2 = Rate(format_='value', diff=False)
    print(test_rate_2.eur())
