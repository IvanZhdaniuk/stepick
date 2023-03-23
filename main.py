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

# from string import Template
# values = {'one': 'Привет', 'copter': 'Квадракоптер'}
#
# t = Template("""
# Ну что, мои хорошие, всем $one
# Это шаблонная строка
# В нее можно вставлять значения по ключам
# Хочу сюда вставлю слово $copter, хочу сюда $copter
# """)
#
# print(t.substitute(values))
#
# import sys
# print(sys.getrecursionlimit())
#
# from string import ascii_lowercase, ascii_uppercase, punctuation
#
# print(punctuation)
# print(ascii_lowercase)
# print(ascii_uppercase)
#
#
# def file_n_lines(file_name: str, n: int) -> None:
#     my_file = open(file_name, encoding='utf-8')
#     for i in range(n):
#         text= my_file.readline()
#         print(text.strip())
#
# file_n_lines('111.txt', 3)

# def create_file_with_numbers(n):
#     my_file = open(f'range_{n}.txt', 'a', encoding='utf-8')
#     for i in range(1,n+1):
#         my_file.write(str(i)+'\n')
#
# create_file_with_numbers(5)

from string import punctuation

# def longest_word_in_file(file_name):
#     max_word = []
#     count = 0
#     my_file = open(file_name, 'r', encoding='utf-8')
#     text = my_file.read()
#     for i in punctuation:
#         text = text.replace(i, '')
#
#     text = text.split()
#     for i in text:
#         i = i.strip(punctuation)
#         if len(i)>= count:
#             count = len(i)
#             max_word = i
#     return max_word
#
# longest_word_in_file('range_5.txt')

# def count_namber(file_name:str)->str:
#     sum_nambers_two_digit = 0
#     count_nambers_three_digit = 0
#     my_file =open(file_name, 'r',encoding='utf-8')
#     text = my_file.read().strip()
#     text = text.split('\n')
#     print(text)
#     for i in text:
#         if len(i) == 2:
#             sum_nambers_two_digit +=int(i)
#         elif len(i) ==3:
#             count_nambers_three_digit +=1
#     print(count_nambers_three_digit, sum_nambers_two_digit)
#
# count_namber('numbers.txt')

#
# def find_lines_len_more_6(file_name:str) -> int:
#
#     with open(file_name, 'r') as f:
#         count = 0
#         for line in f:
#             if len(line) > 6:
#                 count += 1
#         return count

#
#
# find_lines_len_more_6('numbers.txt')

def count_words(file_name:str)->int:
    '''Эта функция подсчитывает оригинальное
    количество слов в файле не зависимо от регистра'''
    with open(file_name, 'r', encoding='utf-8') as f:
        text = set(f.read().strip().lower().split())
        print(len(text))


count_words('lorem.txt')