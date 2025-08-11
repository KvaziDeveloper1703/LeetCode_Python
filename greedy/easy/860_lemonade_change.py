'''
You are selling lemonade at a stand where each cup costs $5. Customers stand in a queue and buy lemonade one at a time. Each customer pays with either a $5, $10, or $20 bill.

You must give back the correct change so that each customer effectively pays exactly $5. You start with no money in hand.

Given an integer array bills, where bills[i] is the bill the i-th customer pays, return True if you can give the correct change to every customer. Otherwise, return False.

Examples:
Input: bills = [5,5,5,10,20]
Output: True

Input: bills = [5,5,10,10,20]
Output: False

Вы продаёте лимонад по $5 за стакан. Покупатели стоят в очереди и покупают лимонад по одному. Каждый платит либо $5, $10 или $20.

Ваша задача — выдавать сдачу так, чтобы каждый клиент фактически заплатил ровно $5. Вы начинаете с пустой кассой, то есть без сдачи.

Дан массив целых чисел bills, где bills[i] — это купюра, которой платит i-й покупатель. Верните True, если вы можете дать сдачу всем покупателям, иначе — False.

Примеры:
Ввод: bills = [5,5,5,10,20]
Вывод: True

Ввод: bills = [5,5,10,10,20]
Вывод: False
'''

from typing import List

def lemonade_change(bills: List[int]) -> bool:
    five_dollar = 0
    ten_dollar = 0

    for bill in bills:
        if bill == 5:
            five_dollar += 1
        elif bill == 10:
            if five_dollar == 0:
                return False
            five_dollar -= 1
            ten_dollar += 1
        else:
            if ten_dollar > 0 and five_dollar > 0:
                ten_dollar -= 1
                five_dollar -= 1
            elif five_dollar >= 3:
                five_dollar -= 3
            else:
                return False

    return True