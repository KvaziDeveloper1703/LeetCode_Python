'''
You are given a positive integer n, which is initially placed on a board.

Every day, for 10^9 days, you perform the following procedure:
    - For each number x currently present on the board, find all integers i such that 1 ≤ i ≤ n and x % i == 1;
    - Place all such numbers i onto the board.

Return the number of distinct integers present on the board after 10^9 days have passed.

Examples:
Input: n = 5
Output: 4

Input: n = 3
Output: 2

Дано положительное целое число n, которое изначально размещается на доске.

Каждый день в течение 10^9 дней выполняется следующая процедура:
    - Для каждого числа x, находящегося на доске, находятся все целые числа i, такие что 1 ≤ i ≤ n и x % i == 1;
    - Все такие числа i добавляются на доску.

Необходимо вернуть количество различных чисел, находящихся на доске после 10^9 дней.

Примеры:
Ввод: n = 5
Вывод: 4

Ввод: n = 3
Вывод: 2
'''

def distinct_integers(n: int) -> int:
    if n == 1:
        return 1
    return n - 1