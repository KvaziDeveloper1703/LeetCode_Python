'''
You are given a string s consisting of lowercase English letters and an integer k. Your task is to convert the string into an integer using a special procedure and then repeatedly transform it by summing its digits.

Follow these steps:
    - Convert the string: replace each letter with its position in the alphabet and concatenate the numbers;
    - Transform the number by replacing it with the sum of its digits;
    - Repeat step 2 exactly k times.

Return the final integer obtained after performing these operations.

Examples:
Input: s = "iiii", k = 1
Output: 36

Input: s = "leetcode", k = 2
Output: 6

Вам дана строка s, состоящая из строчных английских букв, и целое число k. Нужно преобразовать строку в число по особому правилу, а затем k раз преобразовать это число, суммируя его цифры.

Выполните следующие шаги:
    - Преобразование строки: замените каждую букву её номером в алфавите и соедините номера в одно число;
    - Преобразование числа: замените число суммой всех его цифр;
    - Повторите шаг 2 ровно k раз.

Верните итоговое число после всех преобразований.

Примеры:
Ввод: s = "iiii", k = 1
Вывод: 36

Ввод: s = "leetcode", k = 2
Вывод: 6
'''

def get_lucky(s: str, k: int) -> int:
    converted_string = ""
    for character in s:
        converted_string += str(ord(character) - ord('a') + 1)

    current_value = sum(int(digit) for digit in converted_string)

    for _ in range(k - 1):
        current_value = sum(int(digit) for digit in str(current_value))

    return current_value