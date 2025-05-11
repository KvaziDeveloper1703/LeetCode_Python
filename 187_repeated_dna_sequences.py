'''
You're given a DNA string s made up of characters 'A', 'C', 'G', and 'T'.
When analyzing DNA, it's useful to find repeated sequences. Your task is to return all 10-letter-long substrings (sequences) that appear more than once in the DNA string.

Return the result as a list of strings, in any order.

Examples:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC", "CCCCCAAAAA"]

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]

Дана строка s, представляющая ДНК-последовательность, содержащую символы 'A', 'C', 'G' и 'T'.
Нужно найти все подстроки длиной 10 символов, которые встречаются более одного раза в строке s.

Верните список таких подстрок в любом порядке.

Примеры:
Ввод: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Вывод: ["AAAAACCCCC", "CCCCCAAAAA"]

Ввод: s = "AAAAAAAAAAAAA"
Вывод: ["AAAAAAAAAA"]
'''

def findRepeatedDnaSequences(s: str) -> list[str]:
    seen = set()
    repeated = set()

    for i in range(len(s) - 9):
        sequence = s[i:i+10]
        if sequence in seen:
            repeated.add(sequence)
        else:
            seen.add(sequence)

    return list(repeated)