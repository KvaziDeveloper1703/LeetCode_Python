'''
You are given a string s and a character letter. Your task is to calculate the percentage of characters in s that are equal to letter, rounded down to the nearest whole percent.

Return this percentage as an integer.

Examples:
Input: s = "foobar", letter = "o"
Output: 33

Input: s = "jjjj", letter = "k"
Output: 0

Вам дана строка s и символ letter. Необходимо вычислить процент символов в строке s, которые равны letter, округлив результат в меньшую сторону до ближайшего целого процента.

Верните полученное значение в виде целого числа.

Примеры:
Ввод: s = "foobar", letter = "o"
Вывод:33

Ввод: s = "jjjj", letter = "k"
Вывод: 0
'''

def percentageLetter(s: str, letter: str) -> int:
    count = s.count(letter)
    return (count * 100) // len(s)