'''
Alice and Bob have a different total number of candies.

You are given two integer arrays:
    + alice_sizes[i] is the number of candies in Alice's i-th box;
    + bob_sizes[j] is the number of candies in Bob's j-th box.

Since they are friends, they would like to exchange one candy box each, so that after the exchange they both have the same total amount of candy.

Return an array answer = [a, b] where:
    + a is the number of candies in the box Alice gives;
    + b is the number of candies in the box Bob gives.

If multiple answers exist, you may return any one of them. It is guaranteed that at least one valid answer exists.

Examples:
Input: alice_sizes = [1,1], bob_sizes = [2,2]
Output: [1,2]

Input: alice_sizes = [1,2], bob_sizes = [2,3]
Output: [1,2]

У Алисы и Боба разное общее количество конфет.

Вам даны два целочисленных массива:
    + alice_sizes[i] — количество конфет в i-й коробке Алисы;
    + bob_sizes[j] — количество конфет в j-й коробке Боба.

Поскольку они друзья, они хотят обменяться по одной коробке так, чтобы общее количество конфет у обоих стало одинаковым после обмена.

Верните массив из двух чисел [a, b], где:
    + a — количество конфет в коробке, которую должна отдать Алиса;
    + b — количество конфет в коробке, которую должен отдать Боб.

Если существует несколько решений, можно вернуть любое из них. Гарантируется, что хотя бы одно решение существует.

Примеры:
Ввод: alice_sizes = [1,1], bob_sizes = [2,2]
Вывод: [1,2]

Ввод: alice_sizes = [1,2], bob_sizes = [2,3]
Вывод: [1,2]
'''

from typing import List

def fair_candy_swap(alice_sizes: List[int], bob_sizes: List[int]) -> List[int]:
    total_alice = sum(alice_sizes)
    total_bob = sum(bob_sizes)

    target_difference = (total_alice - total_bob) // 2

    bob_candies = set(bob_sizes)

    for alice_candy in alice_sizes:
        bob_candy = alice_candy - target_difference
        if bob_candy in bob_candies:
            return [alice_candy, bob_candy]