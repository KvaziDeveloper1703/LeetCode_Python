'''
You are given a string s of even length.

Split this string into two halves of equal length:
    - Let a be the first half,
    - Let b be the second half.

Two strings are considered alike if they contain the same number of vowels.

The vowels are: 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'.

Return True if a and b are alike. Otherwise, return False.

Examples:
Input: s = "book"
Output: True

Input: s = "textbook"
Output: False

Дана строка s чётной длины.

Раздели её на две равные половины:
    - a - первая половина,
    - b - вторая половина.

Две строки считаются похожими, если в них одинаковое количество гласных букв.

Гласные: 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'.

Верни True, если строки a и b похожи. Иначе верни False.

Примеры:
Ввод: s = "book"
Вывод: True

Ввод: s = "textbook"
Вывод: False
'''

def halves_are_alike(s: str) -> bool:
    vowel_characters = set("aeiouAEIOU")
    total_length = len(s)
    first_half_substring = s[:total_length // 2]
    second_half_substring = s[total_length // 2:]

    first_half_vowel_count = sum(1 for character in first_half_substring if character in vowel_characters)
    second_half_vowel_count = sum(1 for character in second_half_substring if character in vowel_characters)

    return first_half_vowel_count == second_half_vowel_count