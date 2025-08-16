'''
Given a sentence consisting of words separated by a single space, and a string searchWord.

Check if searchWord is a prefix of any word in the sentence. A prefix of a string s is any leading contiguous substring of s.

Return the index of the word where searchWord is a prefix of that word. If searchWord is a prefix of more than one word, return the index of the first such word.

If no word in the sentence has searchWord as a prefix, return -1.

Examples:
Input: sentence = "i love eating burger", searchWord = "burg"
Output: 4

Input: sentence = "this problem is an easy problem", searchWord = "pro"
Output: 2

Дано предложение, состоящее из слов, разделённых одним пробелом, и строка searchWord.

Нужно проверить, является ли searchWord префиксом какого-либо слова в предложении. Префикс строки s — это любая начальная непрерывная подстрока строки s.

Верните индекс слова, для которого searchWord является префиксом. Если таких слов несколько, верните индекс первого.

Если ни одно слово не имеет searchWord в качестве префикса, верните -1.

Примеры:
Ввод: sentence = "i love eating burger", searchWord = "burg"
Вывод: 4

Ввод: sentence = "this problem is an easy problem", searchWord = "pro"
Вывод: 2
'''

def is_prefix_of_word(sentence: str, searchWord: str) -> int:
    words = sentence.split(" ")
    index = 1
    for word in words:
        if word.startswith(searchWord):
            return index
        index += 1
    return -1