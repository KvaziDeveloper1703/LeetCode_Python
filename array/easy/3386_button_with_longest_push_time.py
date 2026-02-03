'''
You are given a 2D integer array events, which represents a sequence of keyboard button presses made by a child.
Each element events[i] = [indexᵢ, timeᵢ] means that the button with index indexᵢ was pressed at time timeᵢ.
The array events is sorted by time in increasing order.

The time spent pressing a button is calculated as the difference between the time of the current press and the previous press.
For the first button, the time spent is simply its recorded time.

Your task is to return the index of the button that took the longest time to press.
If several buttons share the same maximum press time, return the smallest index among them.

Examples:
Input: events = [[1,2], [2,5], [3,9], [1,15]]
Output: 1

Input: events = [[10,5], [1,7]]
Output: 10

Дан двумерный массив целых чисел events, который описывает последовательность нажатий кнопок на клавиатуре ребёнком.
Каждый элемент events[i] = [indexᵢ, timeᵢ] означает, что кнопка с номером indexᵢ была нажата в момент времени timeᵢ.

Массив events отсортирован по времени по возрастанию.
Время нажатия кнопки считается как разница между временем текущего нажатия и предыдущего.
Для первой кнопки время нажатия равно её времени.

Нужно вернуть индекс кнопки, нажатие которой заняло больше всего времени.
Если несколько кнопок имеют одинаковое максимальное время нажатия, вернуть кнопку с наименьшим индексом.

Примеры:
Ввод: events = [[1,2], [2,5], [3,9], [1,15]]
Вывод: 1

Ввод: events = [[10,5], [1,7]]
Вывод: 10
'''

from typing import List

def button_with_longest_time(events: List[List[int]]) -> int:
    max_duration = events[0][1]
    answer_index = events[0][0]

    previous_time = events[0][1]

    for i in range(1, len(events)):
        current_index = events[i][0]
        current_time = events[i][1]

        duration = current_time - previous_time

        if duration > max_duration or (duration == max_duration and current_index < answer_index):
            max_duration = duration
            answer_index = current_index

        previous_time = current_time

    return answer_index