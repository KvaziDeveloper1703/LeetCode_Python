'''
Given a DNA string S made up of characters 'A', 'C', 'G', and 'T'. When analyzing DNA, it's useful to find repeated sequences.

Return all 10-letter-long substrings that appear more than once in the DNA string. Return the result as a list of strings, in any order.

Examples:
Input: S = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC", "CCCCCAAAAA"]

Input: S = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]

Дана строка S, представляющая ДНК-последовательность, содержащую символы 'A', 'C', 'G' и 'T'.

Нужно найти все подстроки длиной 10 символов, которые встречаются более одного раза в строке S. Верните список таких подстрок в любом порядке.

Примеры:
Ввод: S = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Вывод: ["AAAAACCCCC", "CCCCCAAAAA"]

Ввод: S = "AAAAAAAAAAAAA"
Вывод: ["AAAAAAAAAA"]
'''

def find_repeated_dna_sequences(S: str) -> list[str]:
    seen = set()
    repeated = set()

    for i in range(len(S) - 9):
        sequence = S[i:i+10]
        if sequence in seen:
            repeated.add(sequence)
        else:
            seen.add(sequence)

    return list(repeated)