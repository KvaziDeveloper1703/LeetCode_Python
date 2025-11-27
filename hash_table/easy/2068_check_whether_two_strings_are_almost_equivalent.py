'''
Two strings word_1 and word_2 are considered almost equivalent if, for every letter from 'a' to 'z', the difference between its frequency in word_1 and in word_2 is at most 3.

Given two strings word_1 and word_2, both of length n, return True if they are almost equivalent, and False otherwise.

The frequency of a letter x is the number of times it appears in the string.

Examples:
Input: word_1 = "aaaa", word_2 = "bccb"
Output: False

Input: word_1 = "abcdeef", word_2 = "abaaacc"
Output: True

Две строки word_1 и word_2 считаются почти эквивалентными, если для каждой буквы от 'a' до 'z' разница между её количеством в word_1 и в word_2 составляет не более 3.

Даны две строки word_1 и word_2 длины n.

Нужно вернуть True, если строки почти эквивалентны, иначе - False.

Частота буквы x - это число её вхождений в строку.

Примеры:
Ввод: word_1 = "aaaa", word_2 = "bccb"
Вывод: False

Ввод: word_1 = "abcdeef", word_2 = "abaaacc"
Вывод: True
'''

def check_almost_equivalent(word_1: str, word_2: str) -> bool:
    frequency_word1 = {}
    frequency_word2 = {}

    for character in word_1:
        frequency_word1[character] = frequency_word1.get(character, 0) + 1

    for character in word_2:
        frequency_word2[character] = frequency_word2.get(character, 0) + 1

    for ascii_code in range(ord('a'), ord('z') + 1):
        letter = chr(ascii_code)
        count1 = frequency_word1.get(letter, 0)
        count2 = frequency_word2.get(letter, 0)
        if abs(count1 - count2) > 3:
            return False

    return True