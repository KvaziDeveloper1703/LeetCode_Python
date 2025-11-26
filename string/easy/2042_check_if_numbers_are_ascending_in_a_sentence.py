'''
A sentence is a list of tokens separated by single spaces, with no leading or trailing spaces.

Each token is either:
    - a positive integer, or
    - a word made of lowercase English letters.

For example, the sentence "a puppy has 2 eyes 4 legs" contains seven tokens; “2” and “4” are numbers, and the rest are words.

You are given a string s representing a sentence.
Your task is to determine whether all numbers in s are strictly increasing from left to right - meaning every number must be smaller than the next number that appears after it.

Return True if this condition holds, and False otherwise.

Предложение - это набор токенов, разделённых одним пробелом, без пробелов в начале и в конце.

Каждый токен может быть:
    - положительным числом, состоящим из цифр 0–9 без ведущих нулей, или
    - словом, состоящим из строчных английских букв.

Например, предложение "a puppy has 2 eyes 4 legs" содержит семь токенов; «2» и «4» — это числа, остальные — слова.

Дана строка s, представляющая собой предложение.
Необходимо определить, возрастают ли все числа в s строго слева направо, то есть каждое число должно быть меньше следующего встреченного числа.

Верните True, если условие выполняется, и False - если нет.
'''

def are_numbers_ascending(s: str) -> bool:
    previous_number = -1

    for token in s.split():
        if token.isdigit():
            current_number = int(token)
            if current_number <= previous_number:
                return False
            previous_number = current_number

    return True