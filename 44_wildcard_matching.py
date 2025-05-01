'''
Given an input string S and a pattern P, implement wildcard pattern matching with support for:
+ ? Matches any single character;
+ * Matches any sequence of characters.

The match must cover the entire input string, not just part of it.

Example:
Input: S = "aa", P = "a"
Output: false

Дана входная строка S и шаблон P, реализуйте сопоставление с шаблоном, поддерживающим следующие символы:
+ ? — соответствует одному любому символу;
+ * — соответствует любому количеству любых символов, включая ноль символов.

Сопоставление должно охватывать всю строку S, а не её часть.

Пример:
Ввод: S = "aa", P = "a"
Вывод: false
'''

def is_match(input_string: str, pattern: str) -> bool:
    length_input = len(input_string)
    length_pattern = len(pattern)

    dp_table = [[False] * (length_pattern + 1) for _ in range(length_input + 1)]
    dp_table[0][0] = True

    for pattern_index in range(1, length_pattern + 1):
        if pattern[pattern_index - 1] == '*':
            dp_table[0][pattern_index] = dp_table[0][pattern_index - 1]
    
    for input_index in range(1, length_input + 1):
        for pattern_index in range(1, length_pattern + 1):
            current_input_character = input_string[input_index - 1]
            current_pattern_character = pattern[pattern_index - 1]
            
            if current_pattern_character == current_input_character or current_pattern_character == '?':
                dp_table[input_index][pattern_index] = dp_table[input_index - 1][pattern_index - 1]
            elif current_pattern_character == '*':
                match_zero_characters = dp_table[input_index][pattern_index - 1]
                match_one_or_more_characters = dp_table[input_index - 1][pattern_index]
                dp_table[input_index][pattern_index] = match_zero_characters or match_one_or_more_characters
    
    return dp_table[length_input][length_pattern]