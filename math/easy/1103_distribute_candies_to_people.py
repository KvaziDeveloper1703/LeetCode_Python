'''
We have some number of candies and n people sitting in a row. We distribute the candies as follows:
    1) On the first round, give 1 candy to the first person, 2 candies to the second person, and so on, until giving n candies to the last person;
    2) Then, start again from the first person, but now increase the candy count: give n + 1 candies to the first person, n + 2 to the second person, and so on, until the last person gets 2 * n candies;
    3) Repeat this process, increasing the number of candies given each time by 1;
    4) If there aren’t enough candies for the next full amount, give all the remaining candies to the current person and stop.

Return an array of length n where each element is the total candies that person received.

Examples:
Input: candies = 7, n = 4
Output: [1, 2, 3, 1]

Input: candies = 10, n = 3
Output: [5, 2, 3]

У нас есть некоторое количество конфет и n человек, сидящих в ряд. Мы раздаём конфеты следующим образом:
    1) На первом круге раздачи даём 1 конфету первому человеку, 2 конфеты второму, и так далее, пока не дадим n конфет последнему;
    2) Затем начинаем раздачу снова с первого человека, но теперь увеличиваем количество конфет: первому даём n + 1 конфету, второму — n + 2 конфеты, и так далее, пока последнему не достанется 2 * n конфет;
    3) Процесс повторяется — каждый раз количество конфет, которое даём, увеличивается на 1;
    4) Если конфет не хватает для следующего полного количества, то оставшиеся конфеты отдаём текущему человеку и завершаем раздачу.

Нужно вернуть массив длины n, где каждый элемент — это общее количество конфет, полученных соответствующим человеком.

Примеры:
Ввод: candies = 7, n = 4
Вывод: [1, 2, 3, 1]

Ввод: candies = 10, n = 3
Вывод: [5, 2, 3]
'''

from typing import List

def distribute_candies(candies: int, n: int) -> List[int]:
    result = [0] * n
    give = 1
    i = 0

    while candies > 0:
        take = min(give, candies)
        result[i] += take
        candies -= take
        give += 1
        i = (i + 1) % n

    return result