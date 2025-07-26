'''
Given two strings: name and typed. Your friend intended to type the string name, but due to possible long key presses, some characters may appear more than once in a row in typed.

Return True if typed could be a valid result of typing name with some characters long-pressed. Otherwise, return False.

Examples:
Input: name = "alex", typed = "aaleex"
Output: True

Input: name = "saeed", typed = "ssaaedd"
Output: False

Даны две строки: name и typed. Ваш друг пытался ввести строку name, но из-за случайных долгих нажатий клавиш некоторые символы могли быть напечатаны несколько раз подряд в typed.

Верните True, если typed может быть результатом ввода name с возможными долгими нажатиями клавиш. Иначе — False.

Примеры:
Ввод: name = "alex", typed = "aaleex"
Вывод: True

Ввод: name = "saeed", typed = "ssaaedd"
Вывод: False
'''

def is_long_pressed_name(name: str, typed: str) -> bool:
    i = 0
    j = 0

    while j < len(typed):
        if i < len(name) and name[i] == typed[j]:
            i += 1
            j += 1
        elif j > 0 and typed[j] == typed[j - 1]:
            j += 1
        else:
            return False

    return i == len(name)