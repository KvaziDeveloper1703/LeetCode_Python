'''
The school cafeteria offers circular and square sandwiches at lunch break, represented by numbers:
    - 0 → circular sandwich;
    - 1 → square sandwich.

All students stand in a queue, and each student has a preference for one of the two sandwich types.

The number of sandwiches equals the number of students. The sandwiches are arranged in a stack, where sandwiches[0] is the top of the stack.

At each step of the process:
    - If the student at the front of the queue prefers the top sandwich, they take it and leave the queue;
    - Otherwise, the student moves to the end of the queue.

This process continues until no student in the queue wants the top sandwich - meaning no more sandwiches can be taken.

You are given two integer arrays:
    - students, where students[j] is the preference of the j-th student (front = index 0),
    - sandwiches, where sandwiches[i] is the type of the i-th sandwich (top = index 0).

Return the number of students who are unable to eat.

Examples:
Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
Output: 0

Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
Output: 3

В школьной столовой подают круглые и квадратные сэндвичи, обозначенные числами:
    - 0 → круглый сэндвич;
    - 1 → квадратный сэндвич.

Все ученики стоят в очереди, и у каждого есть предпочтение - какой сэндвич он хочет.

Количество сэндвичей равно количеству учеников. Сэндвичи лежат в стопке, где sandwiches[0] - это верхний сэндвич.

Процесс проходит так:
    - Если ученик в начале очереди хочет верхний сэндвич, он его берёт и уходит;
    - Если не хочет - он переходит в конец очереди.

Процесс продолжается до тех пор, пока никто из учеников не захочет верхний сэндвич — тогда подача прекращается.

Даны два массива:
    - students - предпочтения учеников (0 или 1), где students[0] - первый в очереди;
    - sandwiches - типы сэндвичей (0 или 1), где sandwiches[0] - верхний сэндвич.

Нужно вернуть количество учеников, которые не смогли поесть.

Примеры:
Ввод: students = [1,1,0,0], sandwiches = [0,1,0,1]
Вывод: 0

Ввод: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
Вывод: 3
'''

from typing import List

def count_students(students: List[int], sandwiches: List[int]) -> int:
    remaining_square_lovers = students.count(1)
    remaining_circle_lovers = students.count(0)

    for top_sandwich in sandwiches:
        if top_sandwich == 0:
            if remaining_circle_lovers == 0:
                return remaining_square_lovers + remaining_circle_lovers
            remaining_circle_lovers -= 1
        else:
            if remaining_square_lovers == 0:
                return remaining_square_lovers + remaining_circle_lovers
            remaining_square_lovers -= 1

    return 0