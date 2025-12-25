'''
There are n people standing in a line, labeled from 1 to n. Initially, the first person in the line is holding a pillow.

Every second, the person holding the pillow passes it to the next person in the line. When the pillow reaches the end of the line, the direction of passing reverses, and the pillow continues to be passed in the opposite direction.

You are given two positive integers n and time. Return the index of the person who is holding the pillow after time seconds.

Examples:
Input: n = 4, time = 5
Output: 2

Input: n = 3, time = 2
Output: 3

Есть n человек, стоящих в очереди и пронумерованных от 1 до n. В начале первый человек держит подушку.

Каждую секунду человек, держащий подушку, передаёт её следующему человеку в очереди. Когда подушка достигает конца очереди, направление передачи меняется, и подушка начинает передаваться в обратную сторону.

Даны два положительных целых числа n и time. Верните номер человека, который будет держать подушку спустя time секунд.

Примеры:
Ввод: n = 4, time = 5
Вывод: 2

Ввод: n = 3, time = 2
Вывод: 3
'''

def pass_the_pillow(n: int, time: int) -> int:
    cycle = 2 * (n - 1)
    t = time % cycle

    if t < n:
        return 1 + t
    else:
        return n - (t - (n - 1))