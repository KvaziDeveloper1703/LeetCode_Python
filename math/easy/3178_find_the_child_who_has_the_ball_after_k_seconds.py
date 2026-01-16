'''
You are given two positive integers n and k. There are n children numbered from 0 to n − 1 standing in a line from left to right.

At the beginning, child 0 has the ball, and the ball is passed to the right.

Every second, the child holding the ball passes it to the neighboring child in the current direction.
When the ball reaches either end of the line (child 0 or child n − 1), the passing direction reverses.

Return the number of the child who has the ball after k seconds.

Examples:
Input: n = 3, k = 5
Output: 1

Input: n = 5, k = 6
Output: 2

Даны два положительных целых числа n и k. В очереди стоят n детей, пронумерованных от 0 до n - 1, слева направо.

Изначально мяч находится у ребёнка 0, и направление передачи мяча идёт вправо.

Каждую секунду ребёнок, у которого мяч, передаёт его соседу в текущем направлении.
Когда мяч достигает одного из концов очереди (ребёнка 0 или n − 1), направление передачи меняется на противоположное.

Нужно вернуть номер ребёнка, у которого окажется мяч спустя k секунд.

Примеры:
Ввод: n = 3, k = 5
Вывод: 1

Ввод: n = 5, k = 6
Вывод: 2
'''

def number_of_child(n: int, k: int) -> int:
    period = 2 * (n - 1)
    time_in_period = k % period

    if time_in_period <= n - 1:
        return time_in_period
    else:
        return period - time_in_period