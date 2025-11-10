'''
You are given a circular array code of length n and an integer key k.
To decrypt the code, you must replace each number in the array according to the following rules (all replacements happen simultaneously):
    - If k > 0, replace the i-th number with the sum of the next k numbers in the array;
    - If k < 0, replace the i-th number with the sum of the previous |k| numbers in the array;
    - If k == 0, replace every number with 0.

Because the array is circular,
    - the element after code[n-1] is code[0], and
    - the element before code[0] is code[n-1].

Return the resulting decrypted array.

Examples:
Input: code = [5, 7, 1, 4], k = 3
Output: [12, 10, 16, 13]

Input: code = [1, 2, 3, 4], k = 0
Output: [0, 0, 0, 0]

Дан циклический массив code длиной n и целое число k.

Чтобы расшифровать код, нужно заменить каждый элемент массива по следующим правилам (все замены происходят одновременно):
- Если k > 0, то i-й элемент заменяется суммой следующих k элементов массива;
- Если k < 0, то i-й элемент заменяется суммой предыдущих |k| элементов массива;
- Если k == 0, то все элементы заменяются нулями.

Так как массив циклический,
- элемент, следующий за code[n-1], — это code[0],
- элемент, предшествующий code[0], — это code[n-1].

Нужно вернуть получившийся расшифрованный массив.

Примеры:
Ввод: code = [5, 7, 1, 4], k = 3
Вывод: [12, 10, 16, 13]

Ввод: code = [1, 2, 3, 4], k = 0
Вывод: [0, 0, 0, 0]
'''

from typing import List

def decrypt(code: List[int], k: int) -> List[int]:
    n = len(code)
    result = [0] * n

    if k == 0:
        return result

    for i in range(n):
        total = 0
        if k > 0:
            for j in range(1, k + 1):
                total += code[(i + j) % n]
        else:
            for j in range(1, -k + 1):
                total += code[(i - j) % n]
        result[i] = total

    return result