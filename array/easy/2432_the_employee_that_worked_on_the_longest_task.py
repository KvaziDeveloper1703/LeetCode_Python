'''
There are n employees, each identified by a unique ID from 0 to n-1.

You are given a 2D integer array logs, where: logs[i] = [idᵢ, leaveTimeᵢ], and:
    - idᵢ is the ID of the employee who worked on the i-th task;
    - leaveTimeᵢ is the time at which the employee finished the i-th task;
    - All values leaveTimeᵢ are unique.

The i-th task starts immediately after the (i-1)-th task ends, and the 0-th task starts at time 0.

Return the ID of the employee who worked on the task that took the longest time.
If there is a tie, return the smallest employee ID among them.

Examples:
Input: n = 10, logs = [[0,3],[2,5],[0,9],[1,15]]
Output: 1

Input: n = 26, logs = [[1,1],[3,7],[2,12],[7,17]]
Output: 3

Есть n сотрудников, каждый из которых имеет уникальный идентификатор от 0 до n-1.

Дан двумерный массив целых чисел logs, где logs[i] = [idᵢ, leaveTimeᵢ], и:
    - idᵢ - идентификатор сотрудника, выполнявшего i-ю задачу;
    - leaveTimeᵢ - время, в которое сотрудник закончил i-ю задачу;
    - Все значения leaveTimeᵢ уникальны.

i-я задача начинается сразу после окончания (i-1)-й задачи, а 0-я задача начинается в момент времени 0.

Необходимо вернуть идентификатор сотрудника, который выполнял задачу с наибольшей продолжительностью.
Если таких сотрудников несколько, вернуть наименьший идентификатор.

Примеры:
Ввод: n = 10, logs = [[0,3],[2,5],[0,9],[1,15]]
Вывод: 1

Ввод: n = 26, logs = [[1,1],[3,7],[2,12],[7,17]]
Вывод: 3
'''

def hardest_worker(n: int, logs: list[list[int]]) -> int:
    previous_leave_time = 0
    longest_time = 0
    employee_id_with_longest_time = 0

    for employee_id, leave_time in logs:
        task_duration = leave_time - previous_leave_time
        previous_leave_time = leave_time

        if task_duration > longest_time or (
            task_duration == longest_time and employee_id < employee_id_with_longest_time
        ):
            longest_time = task_duration
            employee_id_with_longest_time = employee_id

    return employee_id_with_longest_time