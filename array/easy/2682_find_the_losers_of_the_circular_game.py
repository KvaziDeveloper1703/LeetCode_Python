'''
There are n friends playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. More formally:
    - Moving clockwise from friend i brings you to friend (i + 1) for 1 ≤ i < n;
    - Moving clockwise from friend n brings you back to friend 1.

Game Rules:
    - The 1st friend starts the game by receiving the ball;
    - On the i-th turn, the friend who currently has the ball passes it to the friend who is i × k steps away from them in the clockwise direction;
    - The game continues until some friend receives the ball for the second time.

The losers of the game are the friends who never received the ball during the entire game.

Given two integers n and k, return an array answer containing the numbers of the losing friends in ascending order.

Examples:
Input: n = 5, k = 2
Output: [4, 5]

Input: n = 4, k = 4
Output: [2, 3, 4]

Есть n друзей, которые играют в игру. Друзья сидят по кругу и пронумерованы от 1 до n по часовой стрелке. Формально:
    - Переход по часовой стрелке от друга i ведёт к другу (i + 1) при 1 ≤ i < n;
    - Переход по часовой стрелке от друга n ведёт обратно к другу 1.

Правила игры:
    - Игра начинается с того, что 1-й друг получает мяч;
    - На i-м ходу друг, у которого находится мяч, передаёт его другу, который находится на i × k шагов по часовой стрелке от него;
    - Игра продолжается до тех пор, пока какой-то друг не получит мяч во второй раз.

Проигравшими считаются друзья, которые ни разу не получили мяч за всю игру.

По заданным целым числам n и k необходимо вернуть массив answer, содержащий номера проигравших друзей в возрастающем порядке.

Примеры:
Ввод: n = 5, k = 2
Вывод: [4, 5]

Ввод: n = 4, k = 4
Вывод: [2, 3, 4]
'''

from typing import List

def circular_game_losers(number_of_friends: int, step_size: int) -> List[int]:
    received_ball = [False] * number_of_friends
    current_friend = 0
    turn_number = 1

    while not received_ball[current_friend]:
        received_ball[current_friend] = True
        current_friend = (current_friend + turn_number * step_size) % number_of_friends
        turn_number += 1

    return [friend_index + 1 for friend_index in range(number_of_friends) if not received_ball[friend_index]]