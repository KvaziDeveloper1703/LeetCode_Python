'''
You are given a positive integer arrivalTime, which represents the scheduled arrival time of a train in hours, and another positive integer delayedTime, which represents the delay duration in hours.

Determine the new arrival time of the train after the delay.

The time is given in 24-hour format. If the resulting time is greater than or equal to 24, it should wrap around starting from 0.

Return the final arrival time as an integer.

Examples:
Input: arrivalTime = 15, delayedTime = 5
Output: 20

Input: arrivalTime = 13, delayedTime = 11
Output: 0

Дано положительное целое число arrivalTime, обозначающее время прибытия поезда в часах, и другое положительное целое число delayedTime, обозначающее величину задержки в часах.

Определите новое время прибытия поезда с учётом задержки.

Время задаётся в 24-часовом формате. Если итоговое время больше либо равно 24, необходимо выполнить переход через сутки, начиная с 0.

Верните итоговое время прибытия в виде целого числа.

Примеры:
Ввод: arrivalTime = 15, delayedTime = 5
Вывод: 20

Примеры:
Ввод: arrivalTime = 13, delayedTime = 11
Вывод: 0
'''

def find_delayed_arrival_time(arrivalTime: int, delayedTime: int) -> int:
    final_arrival_time = arrivalTime + delayedTime
    return final_arrival_time % 24