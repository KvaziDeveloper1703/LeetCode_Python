'''
You have a special typewriter with the lowercase English letters 'a' to 'z' arranged in a circle. A pointer indicates the current character, and you can only type the character the pointer is pointing at. Initially, the pointer is at 'a'.

Each second, you may do one of the following:
    - Move the pointer one position clockwise or counterclockwise;
    - Type the character the pointer is currently on.

Given a string word, return the minimum number of seconds needed to type all the characters in word.

Examples:
Input: word = "abc"
Output: 5

Input: word = "bza"
Output: 7

У вас есть специальная печатная машинка, на которой буквы 'a'–'z' расположены по кругу. Указатель показывает на текущую букву, и напечатать можно только ту букву, на которую он указывает. Изначально указатель стоит на букве 'a'.

Каждую секунду можно выполнить одно из действий:
    - Передвинуть указатель на одну букву по или против часовой стрелки;
    - Напечатать букву, на которую указывает указатель.

По заданной строке word нужно вернуть минимальное количество секунд, чтобы напечатать все её символы.

Примеры:
Ввод: word = "abc"
Вывод: 5

Ввод: word = "bza"
Вывод: 7
'''

def min_time_to_type(word: str) -> int:
    total_time = 0
    current_character = 'a'

    for next_character in word:
        distance = abs(ord(next_character) - ord(current_character))
        minimal_rotation = min(distance, 26 - distance)
        total_time += minimal_rotation + 1
        current_character = next_character

    return total_time