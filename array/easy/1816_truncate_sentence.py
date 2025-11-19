'''
A sentence is defined as a sequence of words separated by a single space, with no leading or trailing spaces. Each word contains only English letters, and there is no punctuation.

Given a sentence s and an integer k, your task is to truncate s so that it contains only the first k words. Return the truncated sentence.

Examples:
Input: s = "Hello how are you Contestant", k = 4
Output: "Hello how are you"

Input: s = "What is the solution to this problem", k = 4
Output: "What is the solution"

Предложение - это последовательность слов, разделённых одним пробелом, без пробелов в начале и в конце. Каждое слово состоит только из английских букв, без знаков препинания.

Дано предложение s и целое число k. Необходимо обрезать строку s, оставив в ней только первые k слов. Верните получившееся укороченное предложение.

Примеры:
Ввод: s = "Hello how are you Contestant", k = 4
Вывод: "Hello how are you"

Ввод: s = "What is the solution to this problem", k = 4
Вывод: "What is the solution"
'''

def truncate_sentence(s: str, k: int) -> str:
    words = s.split()
    result = []
    for i in range(k):
        result.append(words[i])
    return " ".join(result)