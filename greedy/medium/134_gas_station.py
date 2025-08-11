'''
There are N gas stations arranged in a circle. Each station i provides gas[i] units of gas. It costs cost[i] units of gas to travel from station i to the next station (i + 1) % n.
You have a car with an unlimited gas tank but start with an empty tank. You can begin your journey at any gas station, and your goal is to complete one full circle in the clockwise direction.

Given two integer arrays gas and cost, return the index of the gas station where you should start to successfully complete the circuit. If it is not possible to complete the circuit from any station, return -1. It is guaranteed that if a solution exists, it is unique.

Examples:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1

Имеется N автозаправочных станций, расположенных по кругу. Каждая станция i предоставляет gas[i] единиц бензина. Чтобы доехать от станции i до следующей станции (i + 1) % N, требуется потратить cost[i] единиц бензина.
У вас есть автомобиль с неограниченным объёмом бензобака, но вы начинаете поездку с пустым баком. Вы можете начать путешествие с любой станции, и ваша цель — совершить один полный круг по часовой стрелке, вернувшись в начальную точку.

Даны два массива целых чисел gas и cost. Верните индекс станции, с которой нужно начать, чтобы успешно завершить весь маршрут. Если совершить круг невозможно ни с одной станции, верните -1. Гарантируется, что если решение существует, то оно единственное.

Примеры:
Ввод: gas = [1, 2, 3, 4, 5], cost = [3, 4, 5, 1, 2]
Вывод: 3

Ввод: gas = [2, 3, 4], cost = [3, 4, 3]
Вывод: -1
'''

from typing import List

def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    total_fuel_balance = 0
    current_fuel_balance = 0
    starting_station_index = 0

    for station_index in range(len(gas)):
        fuel_gain = gas[station_index] - cost[station_index]
        total_fuel_balance += fuel_gain
        current_fuel_balance += fuel_gain

        if current_fuel_balance < 0:
            starting_station_index = station_index + 1
            current_fuel_balance = 0

    return starting_station_index if total_fuel_balance >= 0 else -1