'''
You are given a string word that contains digits and lowercase English letters.

Replace every non-digit character in the string with a space. For example, "a123bc34d8ef34" becomes " 123 34 8 34".

After this replacement, the string will contain several integers separated by one or more spaces - in the example above: "123", "34", "8", and "34".

Your task is to return the number of distinct integers that appear after the replacement.

Two integers are considered different if their decimal representations without leading zeros are different.

Examples:
Input: word = "a123bc34d8ef34"
Output: 3

Input: word = "leet1234code234"
Output: 2

Дана строка word, состоящая из цифр и строчных латинских букв.

Замените каждый нецифровой символ на пробел. Например, строка "a123bc34d8ef34" превратится в " 123 34 8 34".

После такой замены в строке останутся несколько целых чисел, разделённых одним или более пробелами - в примере это "123", "34", "8" и "34".

Нужно вернуть количество различных целых чисел, которые появляются после такой обработки строки.

Два числа считаются разными, если их десятичные представления без ведущих нулей отличаются.

Примеры:
Ввод: word = "a123bc34d8ef34"
Вывод: 3

Ввод: word = "leet1234code234"
Вывод: 2
'''

def number_of_different_integers(word: str) -> int:
    replaced_string = ""
    for character in word:
        if character.isdigit():
            replaced_string += character
        else:
            replaced_string += " "

    split_numbers = replaced_string.split()

    normalized_numbers = {number.lstrip("0") or "0" for number in split_numbers}

    return len(normalized_numbers)