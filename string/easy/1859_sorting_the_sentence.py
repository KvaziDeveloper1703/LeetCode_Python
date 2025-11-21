'''
A sentence is a sequence of words separated by a single space, with no leading or trailing spaces.
Each word contains only lowercase or uppercase English letters.

A sentence can be shuffled by appending a 1-indexed word position to each word and then rearranging the words in any order.

For example, the sentence "This is a sentence" can become "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".

You are given a shuffled sentence s that contains no more than 9 words.
Your task is to reconstruct and return the original sentence.

Предложение - это последовательность слов, разделённых одним пробелом, без пробелов в начале и конце.
Каждое слово состоит только из строчных или заглавных английских букв.

Предложение можно перемешать, если приписать каждому слову его порядковый номер, а затем переставить слова в любом порядке.

Например, предложение "This is a sentence" может стать "sentence4 a3 is2 This1" или "is2 sentence4 This1 a3".

Дана перемешанная строка s, содержащая не более 9 слов.
Ваша задача - восстановить и вернуть исходное предложение.
'''

def sort_sentence(s: str) -> str:
    words = s.split()
    ordered = [""] * len(words)

    for word in words:
        index = int(word[-1]) - 1
        ordered[index] = word[:-1]

    return " ".join(ordered)