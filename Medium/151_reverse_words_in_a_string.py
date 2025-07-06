'''
Given a string S, reverse the order of the words.
+ A word is a sequence of non-space characters;
+ Words are separated by at least one space;
+ The output should contain the words in reverse order, joined by a single space;
+ Remove any extra spaces — no leading, trailing, or multiple spaces between words.

Examples:
Input: S = "the sky is blue"
Output: "blue is sky the"

Input: S = " hello world "
Output: "world hello"

Дана строка S. Необходимо изменить порядок слов на обратный.

Условия:
+ Слово — это последовательность символов, не содержащих пробелов;
+ Слова разделяются одним или несколькими пробелами;
+ В результате слова должны быть в обратном порядке, соединены одним пробелом;
+ Удалите лишние пробелы — не должно быть ведущих, конечных или подряд идущих пробелов.

Примеры:
Вход: S = "the sky is blue"
Выход: "blue is sky the"

Вход: S = " hello world "
Выход: "world hello"
'''

def reverse_words(S: str) -> str:
    return ' '.join(S.strip().split()[::-1])