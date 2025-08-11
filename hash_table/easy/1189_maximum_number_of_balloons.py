'''
Given a string text. You want to use the characters from text to form as many instances of the word "balloon" as possible.
Each character in text can be used at most once.

Return the maximum number of instances of the word "balloon" that can be formed.

Examples:
Input: text = "nlaebolko"
Output: 1

Input: text = "loonbalxballpoon"
Output: 2

Дана строка text. Нужно использовать символы из text, чтобы составить как можно больше слов "balloon".
Каждый символ из text можно использовать не более одного раза.

Верните максимальное количество слов "balloon", которые можно составить.

Примеры:
Ввод: text = "nlaebolko"
Вывод: 1

Ввод: text = "loonbalxballpoon"
Вывод: 2
'''

def max_number_of_balloons(text: str) -> int:
    word = "balloon"

    need = {}
    for ch in word:
        if ch in need:
            need[ch] += 1
        else:
            need[ch] = 1

    have = {}
    for ch in text:
        if ch in have:
            have[ch] += 1
        else:
            have[ch] = 1

    min_count = float('inf')
    for ch, required in need.items():
        available = have.get(ch, 0)
        if available == 0:
            return 0
        possible = available // required
        if possible < min_count:
            min_count = possible

    if min_count == float('inf'):
        return 0

    return min_count