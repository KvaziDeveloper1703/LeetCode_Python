'''
Given a string S, reverse the order of the words.

Conditions:
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
Ввод: S = "the sky is blue"
Вывод: "blue is sky the"

Ввод: S = " hello world "
Вывод: "world hello"
'''

def reverse_words(S: str) -> str:
    S = S.strip()
    words = []
    word = ''

    for character in S:
        if character != ' ':
            word += character
        else:
            if word != '':
                words.append(word)
                word = ''

    if word != '':
        words.append(word)

    reversed_words = []

    for i in range(len(words) - 1, -1, -1):
        reversed_words.append(words[i])

    result = ''

    for i in range(len(reversed_words)):
        result += reversed_words[i]
        if i != len(reversed_words) - 1:
            result += ' '

    return result