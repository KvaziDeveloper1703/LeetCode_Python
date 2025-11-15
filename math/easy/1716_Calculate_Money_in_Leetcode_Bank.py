'''
Hercy wants to save money to buy his first car. He deposits money into the LeetCode bank every day following a specific pattern:
    - On the first Monday, he deposits $1;
    - From Tuesday to Sunday of the same week, he deposits $1 more than the previous day;
    - Starting from the next Monday, he again increases the deposit: every new Monday he deposits $1 more than the Monday of the previous week;
    - For the rest of each week (Tuesday to Sunday), he continues increasing the amount by $1 each day.

Given an integer n, return the total amount of money Hercy has saved after n days.

Герси хочет накопить деньги на свою первую машину. Он кладёт деньги в банк LeetCode каждый день по следующему правилу:
    - В первый понедельник он кладёт 1 доллар;
    - Со вторника по воскресенье той же недели он кладёт на 1 доллар больше, чем в предыдущий день;
    - Каждый следующий понедельник он начинает с суммы, которая на 1 доллар больше, чем в предыдущий понедельник;
    - В остальные дни недели (со вторника по воскресенье) он снова увеличивает сумму каждый день на 1 доллар.

По данному числу n нужно вернуть, сколько денег он накопит за n дней.
'''

def total_money(n: int) -> int:
    total = 0
    week_start = 1

    for i in range(1, n + 1):
        day_of_week = (i - 1) % 7
        total += week_start + day_of_week

        if day_of_week == 6:
            week_start += 1

    return total