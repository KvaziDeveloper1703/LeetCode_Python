'''
You are given an integer array score of size n, where score[i] represents the score of the i-th athlete in a competition.
All the scores are guaranteed to be unique.

Athletes are ranked based on their scores:
    + The athlete with the highest score gets 1st place.
    + The athlete with the 2nd highest score gets 2nd place, and so on.

The ranking rules are:
    + The 1st place athlete's rank is "Gold Medal".
    + The 2nd place athlete's rank is "Silver Medal".
    + The 3rd place athlete's rank is "Bronze Medal".
    + For the 4th place to the nth place athletes, their rank is simply their placement number as a string (for example "4").

Return an array answer of size n where answer[i] is the rank of the i-th athlete.

Examples:
Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]

Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]

Дан массив целых чисел score размера n, где score[i] — это количество баллов, набранное i-м спортсменом в соревновании.
Все значения в массиве гарантированно уникальны.

Спортсмены ранжируются по их баллам:
    + Спортсмен с наибольшим количеством баллов получает 1-е место.
    + Спортсмен со 2-м по величине баллом получает 2-е место, и так далее.

Правила присвоения рангов:
    + Спортсмен на 1-м месте получает ранг "Gold Medal".
    + Спортсмен на 2-м месте получает ранг "Silver Medal".
    + Спортсмен на 3-м месте получает ранг "Bronze Medal".
    + Спортсмены с 4-го по n-е место получают в качестве ранга их номер места в виде строки (например, "4").

Верните массив answer размера n, где answer[i] — это ранг i-го спортсмена.

Примеры:
Ввод: score = [5,4,3,2,1]
Вывод: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]

Ввод: score = [10,3,8,9,4]
Вывод: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
'''

from typing import List

def find_relative_ranks(self, score: List[int]) -> List[str]:
    sorted_indices = sorted(range(len(score)), key=lambda i: -score[i])

    result = [""] * len(score)

    for rank, idx in enumerate(sorted_indices):
        if rank == 0:
            result[idx] = "Gold Medal"
        elif rank == 1:
            result[idx] = "Silver Medal"
        elif rank == 2:
            result[idx] = "Bronze Medal"
        else:
            result[idx] = str(rank + 1)

    return result