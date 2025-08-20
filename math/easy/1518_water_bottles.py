'''
You have numBottles water bottles, all of them initially full.
At the market, you can exchange numExchange empty bottles for one full bottle.

When you drink a full bottle, it becomes empty.

Given two integers numBottles and numExchange.

Return the maximum number of water bottles you can drink.

Examples:
Input: numBottles = 9, numExchange = 3
Output: 13

Input: numBottles = 15, numExchange = 4
Output: 19

Есть numBottles бутылок с водой, которые изначально полные.
В магазине можно обменять numExchange пустых бутылок на одну полную бутылку.

Когда вы выпиваете полную бутылку, она превращается в пустую.

Даны два целых числа numBottles и numExchange.

Нужно вернуть максимальное количество бутылок воды, которое можно выпить.

Примеры:
Ввод: numBottles = 9, numExchange = 3
Вывод: 13

Ввод: numBottles = 15, numExchange = 4
Вывод: 19
'''

def number_of_water_bottles(numBottles: int, numExchange: int) -> int:
    drinks = numBottles
    empty = numBottles

    while empty >= numExchange:
        new_full = empty // numExchange
        drinks += new_full
        empty = empty % numExchange + new_full

    return drinks