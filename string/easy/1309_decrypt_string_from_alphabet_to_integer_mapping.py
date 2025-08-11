'''
Given a string S consisting of digits and the # symbol. You need to convert it into a string of lowercase English letters based on the following rules:
    + Characters 'a' to 'i' are represented by '1' to '9' respectively;
    + Characters 'j' to 'z' are represented by '10#' to '26#' respectively.

Return the resulting string after decoding. It is guaranteed that the input string will always represent a unique mapping.

Examples:
Input: S = "10#11#12"
Output: "jkab"

Input: S = "1326#"
Output: "acz"

Дана строка S, состоящая из цифр и символов #. Требуется преобразовать её в строку из строчных букв английского алфавита по следующим правилам:
    + Символы 'a' до 'i' кодируются цифрами '1' до '9' соответственно;
    + Символы 'j' до 'z' кодируются подстроками '10#' до '26#' соответственно.

Верните строку, полученную после преобразования. Гарантируется, что для всех входных данных существует уникальное соответствие.

Примеры:
Ввод: S = "10#11#12"
Вывод: "jkab"

Ввод: S = "1326#"
Вывод: "acz"
'''

def frequency_alphabets(S: str) -> str:
    result = []
    i = 0
    while i < len(S):
        if i + 2 < len(S) and S[i + 2] == '#':
            number = int(S[i:i + 2])
            result.append(chr(ord('a') + number - 1))
            i += 3
        else:
            number = int(S[i])
            result.append(chr(ord('a') + number - 1))
            i += 1
    return ''.join(result)