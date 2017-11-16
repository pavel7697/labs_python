# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно
# Пример из ex_4.py:
# @print_result
# def test_1():
#     return 1
#
# @print_result
# def test_2():
#     return 'iu'
#
# @print_result
# def test_3():
#     return {'a': 1, 'b': 2}
#
# @print_result
# def test_4():
#     return [1, 2]
#
# test_1()
# test_2()
# test_3()
# test_4()
#
# На консоль выведется:
# test_1
# 1
# test_2
# iu
# test_3
# a = 1
# b = 2
# test_4
# 1
# 2

def return_func():
    def func_inside():
        print("I'm inside")
    print("I'm outside")
    return func_inside

def Print(func, value):
    print(func.__name__)
    res=type(value).__name__
    if res == 'list':
        [print(i) for i in value]
    if res == 'dict':
        [print('{0} = {1}'.format(key, val)) for key, val in value.items()]
    else:
        print(value)
def print_result(func):
    def decor_func(*args, **kwargs):
        value=func(*args,**kwargs)
        Print(func, value)
        return value
    return decor_func