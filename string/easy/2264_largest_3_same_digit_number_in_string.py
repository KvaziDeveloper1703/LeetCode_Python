'''
You are given a string number representing a large integer.

An integer is considered good if:
    - It is a substring of number with length 3;
    - All three characters in the substring are the same digit.

Your task is to return the largest good integer as a string.
If no such substring exists, return an empty string "".

Вам дана строка number, представляющая большое целое число.

Число считается хорошим, если:
    - Это подстрока длиной 3 в строке number;
    - Все три символа этой подстроки - одинаковые цифры.

Нужно вернуть наибольшее хорошее число в виде строки.
Если такой подстроки нет, верните пустую строку "".
'''

def largest_good_integer(number: str) -> str:
    largest_good = ""

    for i in range(len(number) - 2):
        substring = number[i:i+3]
        if substring[0] == substring[1] == substring[2]:
            if substring > largest_good:
                largest_good = substring

    return largest_good