'''
A truck has two fuel tanks: a main tank and an additional tank.

You are given two integers:
    - mainTank - the amount of fuel in the main tank,
    - additionalTank - the amount of fuel in the additional tank.

The truck consumes fuel at a rate of 10 kilometers per liter.

Whenever 5 liters of fuel are consumed from the main tank, if the additional tank contains at least 1 liter of fuel, then 1 liter of fuel is instantly transferred from the additional tank to the main tank.

Your task is to calculate and return the maximum distance (in kilometers) that the truck can travel.

Input: mainTank = 5, additionalTank = 10
Output: 60

Input: mainTank = 1, additionalTank = 2
Output: 10

Грузовик имеет два топливных бака: основной бак и дополнительный бак.

Вам даны два целых числа:
    - mainTank - количество топлива в основном баке,
    - additionalTank - количество топлива в дополнительном баке.

Расход топлива грузовика составляет 10 километров на 1 литр топлива.

Каждый раз, когда из основного бака расходуется 5 литров топлива, если в дополнительном баке есть хотя бы 1 литр топлива, 1 литр топлива мгновенно переливается из дополнительного бака в основной.

Необходимо вычислить и вернуть максимальное расстояние (в километрах), которое может проехать грузовик.

Примеры:
Ввод: mainTank = 5, additionalTank = 10
Вывод: 60

Ввод: mainTank = 1, additionalTank = 2
Вывод: 10
'''

def distance_traveled(mainTank: int, additionalTank: int) -> int:
    total_distance = 0

    while mainTank >= 5 and additionalTank > 0:
        mainTank -= 5
        total_distance += 50
        additionalTank -= 1
        mainTank += 1

    total_distance += mainTank * 10
    return total_distance