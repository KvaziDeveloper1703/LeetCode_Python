'''
There are n available seats and n students in a room.
You are given an array seats of length n, where seats[i] is the position of the i-th seat.
You are also given an array students of length n, where students[j] is the position of the j-th student.

You may perform the following move any number of times: Increase or decrease the position of the i-th student by 1 (that is, move a student from position x to x + 1 or x − 1).

Return the minimum number of moves required so that each student occupies a seat, and no two students sit in the same seat.

В комнате есть n свободных мест и n стоящих студентов.
Дан массив seats длины n, где seats[i] - координата i-го сиденья.
Также дан массив students длины n, где students[j] - координата j-го студента.

Разрешено выполнять следующий ход любое количество раз: Увеличить или уменьшить координату j-го студента на 1.

Нужно вернуть минимальное количество ходов, чтобы рассадить всех студентов по местам так, чтобы никакие два студента не заняли одно и то же место.
'''

from typing import List

def min_moves_to_seat(seats: List[int], students: List[int]) -> int:
    seats_sorted = sorted(seats)
    students_sorted = sorted(students)

    total_moves = 0
    for index in range(len(seats_sorted)):
        total_moves += abs(seats_sorted[index] - students_sorted[index])

    return total_moves