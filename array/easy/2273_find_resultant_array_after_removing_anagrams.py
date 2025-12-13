'''
You are given a 0-indexed array of strings words, where each words[i] consists only of lowercase English letters.

In one operation, you may choose an index i such that 0 < i < words.length and words[i] and words[i - 1] are anagrams. Then, delete words[i] from the array.

You may repeat this operation as long as there exists an index that satisfies these conditions.

Return the array words after performing all possible operations. It can be shown that the final result does not depend on the order in which the valid indices are chosen.

An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all original letters exactly once. For example, "dacb" is an anagram of "abdc".

Вам дан массив строк words с нулевой индексацией, где каждая строка words[i] состоит только из строчных букв английского алфавита.

За одну операцию вы можете выбрать индекс i такой, что 0 < i < words.length, и строки words[i] и words[i - 1] являются анаграммами. После этого строка words[i] удаляется из массива.

Эту операцию можно повторять до тех пор, пока существует индекс, удовлетворяющий указанным условиям.

Необходимо вернуть массив words после выполнения всех возможных операций. Гарантируется, что конечный результат не зависит от порядка, в котором выбираются индексы для удаления.

Анаграмма - это слово или фраза, полученная путём перестановки букв другого слова или фразы с использованием всех исходных букв ровно один раз. Например, строка "dacb" является анаграммой строки "abdc".
'''

def remove_anagrams(words: list[str]) -> list[str]:
    result = []
    previous_signature = None

    for word in words:
        signature = ''.join(sorted(word))

        if signature != previous_signature:
            result.append(word)
            previous_signature = signature

    return result