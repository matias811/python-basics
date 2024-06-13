class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def get_older_cat(cat1, cat2, cat3):
    cats = [cat1, cat2, cat3]
    oldest_cat_name = ''
    oldest_cat_age = 0
    for cat in cats:
        if cat.age > oldest_cat_age:
            oldest_cat_name = cat.name
            oldest_cat_age = cat.age

    print(f'{oldest_cat_name} is the oldest cat, at {oldest_cat_age} years old')
