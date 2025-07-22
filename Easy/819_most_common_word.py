'''
Given a string paragraph containing a block of text, and an array of strings banned listing words that should be ignored.

Find the word that appears most frequently in paragraph and is not present in the banned list. 
Punctuation marks are not considered part of words and must be removed. 
Words are case-insensitive, so "Ball" and "ball" are treated the same. 

The result should be returned in lowercase.

Examples:
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"

Input: paragraph = "a.", banned = []
Output: "a"

Дана строка paragraph, содержащая текст, и массив строк banned, включающий слова, которые необходимо игнорировать.

Нужно определить слово, которое встречается чаще всего среди всех слов в paragraph, не входящих в список banned.
Пунктуационные символы не считаются частью слов и должны быть удалены.
Слова нечувствительны к регистру, то есть "Ball" и "ball" считаются одинаковыми.

Результат следует вернуть в нижнем регистре.

Примеры:
Ввод: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Вывод: "ball"

Ввод: paragraph = "a.", banned = []
Вывод: "a"
'''

from typing import List
import re
from collections import Counter

def most_common_word(paragraph: str, banned: List[str]) -> str:
    words = re.findall(r'\w+', paragraph.lower())
    banned_set = set(banned)
    count = Counter(word for word in words if word not in banned_set)
    return count.most_common(1)[0][0]