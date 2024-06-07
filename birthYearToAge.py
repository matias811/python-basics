import datetime


def calculate_age(birth_year):
    return datetime.date.today().year - birth_year


print(calculate_age(1997))