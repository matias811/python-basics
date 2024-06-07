"""
In this file we explore practical examples and exercises for basic Python Data Types
We will try to approach this course with a TDD mindset, therefore all the test files for the exercises in this file
will be in the file dataTypes_test.py
"""


"""
Printing name and new line
"""


def print_user_name(name):
    print(name)
    print()


print((5 + 4) * 10 / 2) # 9 * 10 / 2 = 45.0

print(((5 + 4) * 10) / 2) # 90 / 2 = 45.0

print((5 + 4) * (10 / 2)) #  9 * 5 = 45.0

print(5 + (4 * 10) / 2) # 5 + 20.0 = 25.0

print(5 + 4 * 10 // 2) # 5 + 20 = 25


def formatted_string(name):
    print(f'Hello {name}, how are you?')


formatted_string('Matias')