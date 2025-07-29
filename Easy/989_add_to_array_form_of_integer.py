'''
The array-form of an integer number is an array representing its digits in left to right order.

Given number, the array-form of an integer, k, an integer.

Return the array-form of the integer number + k.

Examples:
Input: number = [1, 2, 0, 0], k = 34
Output: [1, 2, 3, 4]

Input: number = [2, 7, 4], k = 181
Output: [4, 5, 5]

Формат массива числа — это массив, представляющий цифры числа слева направо.

Например, для числа number = 1321 его массивная форма — [1, 3, 2, 1].

Вам даны number — массивная форма целого числа, k — целое число.

Ваша задача вернуть массивную форму числа number + k.

Примеры:
Ввод: number = [1, 2, 0, 0], k = 34
Вывод: [1, 2, 3, 4]

Ввод: number = [2, 7, 4], k = 181
Вывод: [4, 5, 5]
'''

def add_to_array_form(number: List[int], k: int) -> List[int]:
    result = []
    i = len(number) - 1
    while i >= 0 or k > 0:
        if i >= 0:
            k += number[i]
        result.append(k % 10)
        k //= 10
        i -= 1
    return result[::-1]