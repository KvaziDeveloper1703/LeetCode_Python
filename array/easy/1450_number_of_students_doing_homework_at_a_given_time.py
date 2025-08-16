'''
Given two integer arrays startTime and endTime, and an integer queryTime.

The i-th student started doing homework at time startTime[i] and finished at time endTime[i].

You need to return the number of students who are doing homework exactly at time queryTime.

Formally, count how many students satisfy the condition startTime[i] ≤ queryTime ≤ endTime[i].

Examples:
Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
Output: 1

Input: startTime = [4], endTime = [4], queryTime = 4
Output: 1

Даны два массива целых чисел startTime и endTime, а также целое число queryTime.

i-й студент начал делать домашнее задание в момент времени startTime[i] и закончил в момент endTime[i].

Нужно вернуть количество студентов, которые выполняют домашнее задание в момент времени queryTime.

Формально это количество студентов, для которых выполняется условие startTime[i] ≤ queryTime ≤ endTime[i].

Примеры:
Ввод: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
Вывод: 1

Ввод: startTime = [4], endTime = [4], queryTime = 4
Вывод: 1
'''

from typing import List

def busy_student(startTime: List[int], endTime: List[int], queryTime: int) -> int:
    count = 0
    n = len(startTime)

    for i in range(n):
        start = startTime[i]
        end = endTime[i]
        if start <= queryTime <= end:
            count += 1

    return count