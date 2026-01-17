'''
You are given two positive integers x and y, where:
    - x is the number of coins worth 75;
    - y is the number of coins worth 10.

Alice and Bob play a game with these coins. They take turns, starting with Alice.

On each turn, a player must pick coins whose total value is exactly 115.
If a player cannot make a total value of 115 using the remaining coins, that player loses.

Return the name of the winner assuming both players play optimally.

Examples:
Input: x = 2, y = 7
Output: "Alice"

Input: x = 4, y = 11
Output: "Bob"

Даны два положительных целых числа x и y, где:
    - x это количество монет номиналом 75;
    - y это количество монет номиналом 10.

Алиса и Боб играют в игру. Ходы делаются по очереди, первым ходит Алиса.

В каждый ход игрок обязан выбрать несколько монет так, чтобы их суммарная стоимость была ровно 115.
Если игрок не может набрать сумму 115 из оставшихся монет, он проигрывает.

Верните имя победителя, если оба играют оптимально.

Примеры:
Ввод: x = 2, y = 7
Вывод: "Alice"

Ввод: x = 4, y = 11
Вывод: "Bob"
'''

def winning_player(x: int, y: int) -> str:
    possibleTurns = min(x, y // 4)
    return "Alice" if possibleTurns % 2 == 1 else "Bob"