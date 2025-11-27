'''
There are n people standing in a line to buy tickets.
The person at position 0 is at the front, and the person at position n - 1 is at the back.

You are given a 0-indexed integer array tickets of length n, where tickets[i] represents how many tickets the i-th person wants to buy.

Each person needs exactly 1 second to buy one ticket.
After buying one ticket, the person goes to the end of the line instantly if they still need more tickets.
If a person has bought all their tickets, they leave the queue.

Return the total time it takes for the person who was originally at position k to finish buying all their tickets.

Examples:
Input: tickets = [2,3,2], k = 2
Output: 6

Input: tickets = [5,1,1,1], k = 0
Output: 8

В очереди стоят n человек, где человек с индексом 0 - в начале очереди, а человек с индексом n - 1 - в конце.

Дан 0-индексированный массив tickets длины n, где tickets[i] - это количество билетов, которое хочет купить человек с индексом i.

Каждому человеку требуется 1 секунда, чтобы купить один билет.
После покупки билета человек, если ему нужно купить ещё, моментально встаёт в конец очереди.
Если все билеты куплены, человек покидает очередь.

Верните время, за которое человек, который изначально стоял на позиции k, полностью купит все свои билеты.

Примеры:
Ввод: tickets = [2,3,2], k = 2
Вывод: 6

Ввод: tickets = [5,1,1,1], k = 0
Вывод: 8
'''

from typing import List

def time_required_to_buy(tickets: List[int], k: int) -> int:
    total_time = 0
    target_tickets = tickets[k]

    for index in range(len(tickets)):
        if index <= k:
            total_time += min(tickets[index], target_tickets)
        else:
            total_time += min(tickets[index], target_tickets - 1)

    return total_time