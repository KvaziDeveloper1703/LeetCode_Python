'''
You are given an integer money, which represents the total amount of money (in dollars) that you have, and another integer children, which represents the number of children among whom the money must be distributed.

You must distribute the money according to the following rules:
    - All the money must be distributed;
    - Each child must receive at least 1 dollar;
    - No child may receive exactly 4 dollars.

Return the maximum number of children who can receive exactly 8 dollars while satisfying the rules above. If it is not possible to distribute the money according to these rules, return -1.

Examples:
Input: money = 20, children = 3
Output: 1

Input: money = 16, children = 2
Output: 2

Дано целое число money, обозначающее общую сумму денег (в долларах), и целое число children, обозначающее количество детей, которым нужно распределить деньги.

Необходимо распределить деньги, соблюдая следующие правила:
    - Вся сумма денег должна быть распределена;
    - Каждый ребёнок должен получить как минимум 1 доллар;
    - Никто не может получить ровно 4 доллара.

Верните максимальное количество детей, которые могут получить ровно 8 долларов, при соблюдении всех перечисленных правил. Если распределить деньги по правилам невозможно, верните -1.

Примеры:
Ввод: money = 20, children = 3
Вывод: 1

Ввод: money = 16, children = 2
Вывод: 2
'''

def distribute_money(money: int, children: int) -> int:
    if money < children:
        return -1

    money -= children

    count = min(money // 7, children)
    money -= count * 7
    children -= count

    if children == 0 and money > 0:
        count -= 1
    elif children == 1 and money == 3:
        count -= 1

    return count