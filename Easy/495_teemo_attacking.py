'''
Our hero Teemo is attacking an enemy Ashe with poison attacks!

When Teemo attacks Ashe, she becomes poisoned for exactly duration seconds. More precisely, an attack at time t will poison Ashe during the inclusive interval [t, t + duration - 1].
If Teemo attacks again before the current poison effect ends, the poison timer resets, and Ashe will be poisoned for duration more seconds from the new attack time.

You are given a non-decreasing integer array time_series, where time_series[i] denotes that Teemo attacks at second time_series[i], and an integer duration.
Return the total number of seconds that Ashe is poisoned.

Examples:
Input: time_series = [1, 4], duration = 2
Output: 4

Input: time_series = [1, 2], duration = 2
Output: 3

Наш герой Тимо атакует вражескую Эш своими ядовитыми атаками!

Когда Тимо атакует Эш, она получает эффект яда ровно на duration секунд. Иными словами, атака в момент времени t означает, что Эш будет отравлена в течение интервала [t, t + duration - 1] включительно.
Если Тимо атакует снова до того, как закончится текущий эффект яда, таймер обновляется, и яд продлевается ещё на duration секунд с момента новой атаки.

Дан массив целых чисел time_series, где time_series[i] означает, что Тимо атакует в секунду time_series[i], и целое число duration.
Верните общее количество секунд, в течение которых Эш была отравлена.

Примеры:
Ввод: time_series = [1, 4], duration = 2
Вывод: 4

Ввод: time_series = [1, 2], duration = 2
Вывод: 3
'''

from typing import List

def find_poisoned_duration(time_series: List[int], duration: int) -> int:
    if not time_series:
        return 0
        
    total = 0
    for i in range(1, len(time_series)):
        total += min(duration, time_series[i] - time_series[i - 1])
        
    total += duration
        
    return total