'''
We say the usage of capitals in a word is correct if one of the following conditions holds:
    + All the letters in the word are capitals, like "USA".
    + All the letters in the word are not capitals, like "leetcode".
    + Only the first letter in the word is capital (and the rest are lowercase), like "Google".

Given a string word, return true if its usage of capitals is correct according to the above rules. Otherwise, return false.

Examples:
Input: word = "USA"
Output: true

Input: word = "FlaG"
Output: false

Говорят, что использование заглавных букв в слове корректно, если выполняется одно из следующих условий:
    + Все буквы в слове заглавные, например: "USA".
    + Все буквы в слове строчные, например: "leetcode".
    + Только первая буква в слове заглавная (остальные строчные), например: "Google".

Дан строковый параметр word. Верните true, если использование заглавных букв в нём корректно в соответствии с описанными правилами. Иначе верните false.

Примеры:
Ввод: word = "USA"
Вывод: true

Ввод: word = "FlaG"
Вывод: false
'''

def detect_capital_use(self, word: str) -> bool:
    if word.isupper():
        return True
    elif word.islower():
        return True
    elif word[0].isupper() and word[1:].islower():
        return True
    else:
        return False