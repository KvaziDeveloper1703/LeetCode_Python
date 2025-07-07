'''
Given a string S, reverse the characters of each word in the sentence while still preserving the original word order and whitespace.
    + A word is defined as a sequence of non-space characters;
    + The order of the words in the sentence should remain the same; only the characters within each word are reversed.

Examples:
Input: S = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Input: S = "Mr Ding"
Output: "rM gniD"

Дана строка S. Необходимо перевернуть порядок символов в каждом слове этой строки, сохранив при этом исходный порядок слов и пробелов.
    + Слово определяется как последовательность символов без пробелов;
    + Порядок слов в предложении остаётся прежним, изменяется только порядок букв в каждом слове.

Примеры:
Ввод: S = "Let's take LeetCode contest"
Вывод: "s'teL ekat edoCteeL tsetnoc"

Ввод: S = "Mr Ding"
Вывод: "rM gniD"
'''

def reverse_words(S: str) -> str:
    words = S.split()
    reversed_words = []

    for word in words:
        reversed_word = word[::-1]
        reversed_words.append(reversed_word)

    return ' '.join(reversed_words)