'''
A sentence is defined as a sequence of words separated by a single space, with no leading or trailing spaces.
    - Each word consists only of uppercase and lowercase English letters;
    - Uppercase and lowercase letters are considered different characters.

A sentence is called circular if the following conditions are satisfied:
    - The last character of each word is equal to the first character of the next word;
    - The last character of the last word is equal to the first character of the first word.

Given a string sentence, return True if the sentence is circular. Otherwise, return False.

Examples:
Input: sentence = "leetcode exercises sound delightful"
Output: True

Input: sentence = "eetcode"
Output: True

Предложение - это последовательность слов, разделённых одним пробелом, без начальных и конечных пробелов.
    - Каждое слово состоит только из заглавных и строчных латинских букв;
    - Заглавные и строчные буквы считаются разными символами.

Предложение называется циклическим, если выполняются следующие условия:
    - Последний символ каждого слова совпадает с первым символом следующего слова;
    - Последний символ последнего слова совпадает с первым символом первого слова.

Дана строка sentence. Верните True, если предложение является циклическим, иначе верните False.

Примеры:
Ввод: sentence = "leetcode exercises sound delightful"
Вывод: True

Ввод: sentence = "eetcode"
Вывод: True
'''

def is_circular_sentence(sentence: str) -> bool:
    words = sentence.split()

    for i in range(len(words)):
        if words[i][-1] != words[(i + 1) % len(words)][0]:
            return False
        
    return True