'''
You are playing the Bulls and Cows game with your friend.

You write down a secret number, and your friend tries to guess what it is.
When your friend makes a guess, you provide a hint that includes:

The number of "bulls", which are digits in the guess that are in the correct position.

The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position.
More precisely, these are non-bull digits in the guess that could be rearranged to become bulls.

Given two strings secret and guess, return the hint in the format: "xAyB", where x is the number of bulls and y is the number of cows.

Examples:
Input:  secret = "1807", guess = "7810"
Output: "1A3B"

Input:  secret = "1123", guess = "0111"
Output: "1A1B"

Вы играете с другом в игру "Быки и коровы".

Вы загадываете секретное число, а ваш друг пытается его угадать.
После каждой попытки вы даёте подсказку, которая включает:

Количество "быков" — это цифры, которые угаданы точно и стоят на правильном месте.

Количество "коров" — это цифры, которые есть в секретном числе, но стоят не на том месте, где должны.
Иными словами, это такие цифры из предположения, которые не стали быками, но могли бы ими стать при перестановке.

Даны две строки secret и guess. Верните подсказку в формате: "xAyB", где x — количество быков, а y — количество коров.

Примеры:
Ввод:  secret = "1807", guess = "7810"
Вывод: "1A3B"

Ввод:  secret = "1123", guess = "0111"
Вывод: "1A1B"
'''

from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0

        secret_counter = Counter()
        guess_counter = Counter()

        for s_digit, g_digit in zip(secret, guess):
            if s_digit == g_digit:
                bulls += 1
            else:
                secret_counter[s_digit] += 1
                guess_counter[g_digit] += 1

        for digit in guess_counter:
            cows += min(secret_counter.get(digit, 0), guess_counter[digit])

        return f"{bulls}A{cows}B"