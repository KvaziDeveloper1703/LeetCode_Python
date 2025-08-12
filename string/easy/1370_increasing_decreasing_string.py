'''
Given a string S. You must reorder it using the following algorithm:
    1) Remove the smallest character from S and append it to the result;
    2) Remove the smallest character from S that is greater than the last appended character, and append it to the result;
    3) Repeat step 2 until no more characters can be removed;
    4) Remove the largest character from S and append it to the result;
    5) Remove the largest character from S that is smaller than the last appended character, and append it to the result;
    6) Repeat step 5 until no more characters can be removed;
    7) Repeat steps 1–6 until all characters from S have been removed.

If the smallest or largest character occurs more than once, you may pick any occurrence to append to the result.

Return the resulting string after applying this algorithm.

Examples:
Input:  S = "aaaabbbbcccc"
Output: "abccbaabccba"

Input:  S = "rat"
Output: "art"

Вам дана строка S. Необходимо упорядочить её, используя следующий алгоритм:
    1) Удалите из S наименьший символ и добавьте его в результат;
    2) Удалите из S наименьший символ, который больше последнего добавленного символа, и добавьте его в результат;
    3) Повторяйте шаг 2, пока нельзя удалить больше символов;
    4) Удалите из S наибольший символ и добавьте его в результат;
    5) Удалите из S наибольший символ, который меньше последнего добавленного символа, и добавьте его в результат;
    6) Повторяйте шаг 5, пока нельзя удалить больше символов;
    7) Повторяйте шаги 1–6, пока все символы из S не будут удалены.

Если наименьший или наибольший символ встречается несколько раз, можно выбрать любое его вхождение для добавления в результат.

Верните строку, полученную после выполнения алгоритма.

Примеры:
Ввод:  S = "aaaabbbbcccc"
Вывод: "abccbaabccba"

Ввод:  S = "rat"
Вывод: "art"
'''

from collections import Counter

def sort_string(S: str) -> str:
    counter = Counter(S)
    result = []

    while len(result) < len(S):
        for character in sorted(counter.keys()):
            if counter[character] > 0:
                result.append(character)
                counter[character] -= 1

        for character in sorted(counter.keys(), reverse=True):
            if counter[character] > 0:
                result.append(character)
                counter[character] -= 1

    return "".join(result)