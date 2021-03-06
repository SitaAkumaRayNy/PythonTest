# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

print("Задание 1")

def func_1(a, b):
    if b != 0:
        return a / b
    else:
        return "Деление на ноль!"

a = float(input("Введите a: "))
b = float(input("Введите b: "))
print("Результат деления a на b: ", func_1(a, b))

# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

print("Задание 2")

def func_2(name, lastname, year, city, email, phone):
    print(
        f"Имя = {name}, Фамилия = {lastname}, Год рождения = {year}, Город проживания = {city}, email = {email}, Телефон = {phone}")

func_2(name="Сергей", lastname="Иванов", year=1995, city="Новгород", email="dfghj@dfgh.com", phone=89088000000)

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

print("Задание 3")

def func_3(a, b, c):
    temp_list = [a, b, c]
    temp_list.sort()
    return temp_list[2] + temp_list[1]

a = float(input("Введите первое значение: "))
b = float(input("Введите второе значение: "))
c = float(input("Введите третье значение: "))

print("Сумма двух наибольших значений: ", func_3(a, b, c))

# 4. Программа принимает действительное положительное число x и
# целое отрицательное число y. Необходимо выполнить возведение
# числа x в степень y. Задание необходимо реализовать в виде
# функции my_func(x, y). При решении задания необходимо обойтись
# без встроенной функции возведения числа в степень.

print("Задание 4")

"""Решение через **"""
def func_4(x, y):
    return x ** y


"""Решение через цикл"""
def func_4_2(x, y):
    ind = 0
    pw = 1
    while ind < abs(y):
        pw *= x
        ind += 1
    if y < 0:
        return 1 / pw
    else:
        return pw


x = float(input("Введите x: "))
y = float(input("Введите y: "))
print(f"{x} в степени {y} равен ", func_4(x, y))
print("А через цикл: ", func_4_2(x, y))

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму
# этих чисел к полученной ранее сумме и после этого завершить программу.

print("Задание 5")

def func_5():
    summa = 0
    spl = 0

    while spl == 0:
        list1 = input("Введите значения через пробел и/или '!' для окончания ввода: ").split(" ")
        if "!" in list1:
            spl = 1
            list1.remove("!")
        summa += sum(map(int, list1))
    return summa

print("Итоговая сумма: ", func_5())

#6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

print("Задание 6")

def int_func(text):
    s = f"{text}"
    return s.title()

text_list = input("Введите слова через пробел: ").split(" ")
print(list(map(int_func, text_list)))
