"""
You have buckets buckets, and exactly one of them is poisonous. You need to figure out which one it is using the smallest number of pigs.
Each pig can be fed a custom combination of bucket contents at any time, but once a pig drinks from the poisonous bucket, it will die exactly minutesToDie minutes later.
You are allowed to test for up to minutesToTest minutes total.
Each time you test, you must wait minutesToDie minutes to observe which pigs die.
You cannot test again until the minutesToDie time has passed.
Your goal is to determine the minimum number of pigs needed to identify the poisonous bucket within the given time.

Input:
    + buckets: total number of buckets
    + minutesToDie: time after which a pig dies once it consumes poison
    + minutesToTest: total time available for testing

Output:
    + Minimum number of pigs needed to identify the poisonous bucket within the given time.

У вас есть buckets ведер с жидкостью, и только одно из них ядовито. Необходимо определить, какое именно ведро содержит яд, используя минимальное количество свиней.
Каждая свинья может быть накормлена любой комбинацией жидкости из ведер. Если свинья выпьет яд, она умрёт ровно через minutesToDie минут.
Общий лимит времени на проведение экспериментов — minutesToTest минут.
После каждой кормёжки нужно ждать minutesToDie минут, чтобы увидеть, кто из свиней выживет.
Нельзя кормить свиней снова до истечения этого времени.
Найдите минимальное количество свиней, достаточное для того, чтобы определить ядовитое ведро в рамках отведённого времени.

Входные данные:
    + buckets — количество ведер
    + minutesToDie — время, через которое умирает свинья, выпив яд
    + minutesToTest — общее время на эксперименты

Выходные данные:
    + Минимальное количество свиней, необходимых для определения ядовитого ведра.
"""

import math

def poorPigs(buckets: int, minutesToDie: int, minutesToTest: int) -> int:
    times = minutesToTest // minutesToDie
    pigs = 0
    while (times + 1) ** pigs < buckets:
        pigs += 1
    return pigs