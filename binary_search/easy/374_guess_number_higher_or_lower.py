'''
We are playing the Guess Game:
    - I pick a number from 1 to n;
    - You need to guess which number I picked;
    - After each wrong guess, I will tell you whether the picked number is higher or lower than your guess.

You are given a pre-defined API: int guess(int num).

It returns:
    - -1 if your guess is higher than the picked number (num > pick);
    - 1 if your guess is lower than the picked number (num < pick);
    - 0 if your guess is equal to the picked number (num == pick).

Return the number that I picked.

Examples:
Input: n = 10, pick = 6
Output: 6

Input: n = 1, pick = 1
Output: 1

Мы играем в игру Guess Game:
    - Я загадываю число от 1 до n;
    - Твоя задача - угадать, какое число я выбрал;
    - После каждой неправильной попытки я скажу, загаданное число больше или меньше, чем твой вариант.

Тебе дана заранее определённая функция: int guess(int num).

Она возвращает:
    - -1, если твоё число больше загаданного (num > pick);
    - 1, если твоё число меньше загаданного (num < pick);
    - 0, если числа равны (num == pick).

Верни число, которое я загадал.

Примеры:
Ввод: n = 10, pick = 6
Вывод: 6

Ввод: n = 1, pick = 1
Вывод: 1
'''

picked_number = 6

def guess(num: int) -> int:
    global picked_number
    if num > picked_number:
        return -1
    if num < picked_number:
        return 1
    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            middle = (left + right) // 2
            result = guess(middle)

            if result == 0:
                return middle
            elif result == -1:
                right = middle - 1
            else:
                left = middle + 1


if __name__ == "__main__":
    solution = Solution()
    n = 10
    answer = solution.guessNumber(n)
    print(answer)