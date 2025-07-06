'''
You are given a pattern and a string S consisting of words separated by spaces.
Determine if S follows the same pattern.
For S to follow the pattern, there must be a bijection between: each character in pattern, and each non-empty word in S.

This means:
+ Each letter in pattern maps to exactly one unique word in S;
+ Each word in S maps to exactly one unique letter in pattern;
+ No two letters can map to the same word, and no two words can map to the same letter.

Examples:
Input: pattern = "abba", S = "dog cat cat dog"
Output: true

Input: pattern = "abba", S = "dog cat cat fish"
Output: false

Даны строка pattern и строка S, состоящая из слов, разделённых пробелами.
Необходимо определить, соответствует ли строка S шаблону pattern.
Чтобы S соответствовала шаблону, должна быть выполнена биекция между: каждым символом в pattern, и каждым непустым словом в S.

Это означает:
+ Каждая буква из pattern должна отображаться в однозначное уникальное слово из S;
+ Каждое слово из S должно отображаться в однозначную уникальную букву из pattern;
+ Две разные буквы не могут соответствовать одному и тому же слову, и два разных слова не могут соответствовать одной и той же букве.

Примеры:
Ввод: pattern = "abba", S = "dog cat cat dog"
Вывод: true

Ввод: pattern = "abba", S = "dog cat cat fish"
Вывод: false
'''

def word_pattern(pattern: str, S: str) -> bool:
    word_list = S.split()

    if len(pattern) != len(word_list):
        return False

    pattern_char_to_word = {}
    word_to_pattern_char = {}

    for pattern_char, word in zip(pattern, word_list):
        if pattern_char in pattern_char_to_word:
            if pattern_char_to_word[pattern_char] != word:
                return False
        else:
            pattern_char_to_word[pattern_char] = word

        if word in word_to_pattern_char:
            if word_to_pattern_char[word] != pattern_char:
                return False
        else:
            word_to_pattern_char[word] = pattern_char

    return True