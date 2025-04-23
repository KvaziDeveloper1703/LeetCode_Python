'''
Given an input string s and a pattern p, implement regular expression matching with support for the following:
+ '.' Matches any single character;
+ '*' Matches zero or more of the preceding element.

The matching should cover the entire input string.

Examples:
Input: s = "aa", p = "a"
Output: false

Input: s = "aa", p = "a*"
Output: true

Дана строка s и шаблон p, необходимо реализовать сопоставление с регулярным выражением, поддерживающее символы:
'.' — соответствует любому одному символу;
'*' — соответствует нулю или более предыдущих символов.

Сопоставление должно охватывать всю строку, а не её часть.

Примеры:
Ввод: s = "aa", p = "a"
Вывод: false

Ввод: s = "aa", p = "a*"
Вывод: true
'''

def is_match(input_string: str, pattern: str) -> bool:
    input_length, pattern_length = len(input_string), len(pattern)
    dp_table = [[False] * (pattern_length + 1) for _ in range(input_length + 1)]
    dp_table[0][0] = True

    for pattern_index in range(1, pattern_length + 1):
        if pattern[pattern_index - 1] == '*':
            dp_table[0][pattern_index] = dp_table[0][pattern_index - 2]
    
    for input_index in range(1, input_length + 1):
        for pattern_index in range(1, pattern_length + 1):
            if pattern[pattern_index - 1] == input_string[input_index - 1] or pattern[pattern_index - 1] == '.':
                dp_table[input_index][pattern_index] = dp_table[input_index - 1][pattern_index - 1]
            elif pattern[pattern_index - 1] == '*':
                dp_table[input_index][pattern_index] = dp_table[input_index][pattern_index - 2] or \
                                                        (dp_table[input_index - 1][pattern_index] and 
                                                        (pattern[pattern_index - 2] == input_string[input_index - 1] or pattern[pattern_index - 2] == '.'))
    return dp_table[input_length][pattern_length]