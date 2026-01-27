'''
Alice is trying to type a certain string on her computer. However, she is somewhat clumsy and may accidentally hold a key for too long, causing a character to be typed multiple times in a row.
Alice believes that this mistake could have happened at most once while typing.
You are given a string word, which represents the final text shown on Alice’s screen.
Your task is to determine how many different original strings Alice could have intended to type.

Examples:
Input: word = "abbcccc"
Output: 5

Input: word = "abcd"
Output: 1

Алиса пытается набрать некоторую строку на компьютере. Однако она может случайно зажать клавишу слишком долго, из-за чего один и тот же символ может появиться несколько раз подряд.
Алиса считает, что такая ошибка могла произойти не более одного раза за всё время печати.
Вам дана строка word, которая представляет собой итоговый текст на экране.
Необходимо определить, сколько различных исходных строк Алиса могла намереваться напечатать.

Примеры:
Ввод: word = "abbcccc"
Вывод: 5

Ввод: word = "abcd"
Вывод: 1
'''

def possible_string_count(word: str) -> int:
    result = 1
    index = 0

    while index < len(word):
        start = index
        while index < len(word) and word[index] == word[start]:
            index += 1

        group_length = index - start
        if group_length > 1:
            result += group_length - 1

    return result