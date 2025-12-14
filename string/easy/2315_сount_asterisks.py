'''
You are given a string s in which every two consecutive vertical bars '|' form a pair.

That is, the 1st and 2nd '|' characters make one pair, the 3rd and 4th make the next pair, and so on.

Each '|' character belongs to exactly one pair.

Your task is to return the number of asterisk characters '*' in the string, excluding those that appear between each pair of '|' characters.

Examples:
Input: s = "l|*e*et|c**o|*de|"
Output: 2

Input: s = "iamprogrammer"
Output: 0

Дана строка s, в которой каждые две последовательные вертикальные черты '|' образуют пару.

То есть 1-я и 2-я вертикальные черты образуют первую пару, 3-я и 4-я - вторую пару и так далее.

Каждый символ '|' принадлежит ровно одной паре.

Требуется определить количество символов '*' в строке, не учитывая те из них, которые находятся между каждой парой символов '|'.

Примеры:
Ввод:s = "l|*e*et|c**o|*de|"
Вывод:2

Ввод: s = "iamprogrammer"
Вывод: 0
'''

def count_asterisks(s: str) -> int:
    asterisk_count = 0
    inside_bar_pair = False

    for character in s:
        if character == '|':
            inside_bar_pair = not inside_bar_pair
        elif character == '*' and not inside_bar_pair:
            asterisk_count += 1

    return asterisk_count