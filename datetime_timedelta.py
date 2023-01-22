from datetime import datetime, timedelta


def dateformat(date, format_):
    if format_ == 'The Moscow Times':
        return datetime.strptime(date, '%A, %B %d, %Y')
    elif format_ == 'The Guardian':
        return datetime.strptime(date, '%A, %d.%m.%y')
    elif format_ == 'Daily News':
        return datetime.strptime(date, '%A, %d %B %Y')
    else:
        return 'Error'


def date_check(date):
    try:
        datetime.strptime(date, '%Y - %m - %d')
        return True
    except:
        return False


def date_range(start_date, end_date):
    try:
        start_date_dt = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')
        if start_date_dt < end_date_dt:
            result = []
            current_date = start_date_dt
            while current_date < end_date_dt:
                result.append(current_date.strftime('%Y-%m-%d'))
                current_date = current_date + timedelta(days=1)
            return result
        else:
            return 'Дата начала отсчета позже даты конца отсчета!'
    except ValueError as exception:
        return f"Неверный формат даты! {exception}"


if __name__ == "__main__":
    print(dateformat('Wednesday, October 2, 2002', 'The Moscow Times').weekday())
    print(dateformat('Friday, 11.10.13', 'The Guardian'))
    print(dateformat('Thursday, 18 August 1977', 'Daily News'))

    stream = ['2018 - 04 - 02', '2018 - 02 - 29', '2018 - 19 - 02']
    for item in stream:
        print(date_check(item))

    print(date_range('2018-07-09', '2018-07-19'))