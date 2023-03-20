#
# from functools import wraps
# def decorator_header(func):
#     @wraps(func)
#     def inner(*args, **kwargs):
#         print('<hi>')
#         func(*args, **kwargs)
#         print('</h1>')
#     return inner
#
# @decorator_header
# def say(name, surname):
#     '''
#     This function print string Hellow name and surname
#     :param name: str
#     :param surname: str
#     :return: str
#     '''
#     print(f'Hellow {name}, {surname}')
#
#
# say('Ivan', 'Zhdaniuk')



# # Напишите определение декоратора validate_args
# from functools import wraps
#
# def validate_args(func):
#     @wraps
#     def inner(*args):
#         if len(args)< 2:
#             print('1')
#             return 'Not enough arguments'
#
#         elif len(args)>2:
#             print('2')
#             return 'Too many arguments'
#
#         elif len(args) ==2:
#             print(len(args))
#             a, b = args
#             if type(a) == int and type(b) == int:
#                 c = func(args)
#                 print(c)
#                 return c
#             else:
#                 print('4')
#                 return 'Wrong types'
#     return inner
#
#
# # Код ниже не удаляйте, он нужен для проверки
# @validate_args
# def add_numbers(x, y):
#     """Return sum of x and y"""
#     return x + y
#
#
#
# assert add_numbers(4) == 'Not enough arguments'
# assert add_numbers() == 'Not enough arguments'
# assert add_numbers('hello') == 'Not enough arguments'
# assert add_numbers(3, 5, 6) == 'Too many arguments'
# assert add_numbers('a', 'b', 'c') == 'Too many arguments'
# assert add_numbers(4.5, 5.1) == 'Wrong types'
# assert add_numbers('hello', 4) == 'Wrong types'
# assert add_numbers(9, 'hello') == 'Wrong types'
# assert add_numbers([1, 3], {}) == 'Wrong types'
# assert add_numbers.__name__ == 'add_numbers'
# assert add_numbers.__doc__.strip() == 'Return sum of x and y'
# print('Good')

# import calendar
# x = calendar.TextCalendar()
# print(x.formatyear(2023))
# import math
import pprint
# pprint.pprint(dir(math))
# pprint.pprint(math.e)
# print('-------------__________________________--')

# import os
# pprint.pprint(dir(os))
# print('-------------__________________________--')
# print(os.name)
# help(os)
# pprint.pprint(dir(os))
# pprint.pprint(os.environ["HOME"])

from string import Template
values = {'one': 'Привет', 'copter': 'Квадракоптер'}

t = Template("""
Ну что, мои хорошие, всем $one
Это шаблонная строка
В нее можно вставлять значения по ключам
Хочу сюда вставлю слово $copter, хочу сюда $copter
""")

print(t.substitute(values))

import sys




