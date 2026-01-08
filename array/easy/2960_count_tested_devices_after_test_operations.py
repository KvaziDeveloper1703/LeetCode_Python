'''
You are given a 0-indexed integer array batteryPercentages of length n, where batteryPercentages[i] represents the battery percentage of the i-th device.

Your task is to test the devices one by one, in order from index 0 to n − 1, by performing the following operations for each device i:
    - If batteryPercentages[i] is greater than 0:
        - Increase the count of tested devices by 1;
        - Decrease the battery percentage of all devices with indices j in the range [i + 1, n − 1] by 1;
        - Ensure that no battery percentage becomes negative, i.e. batteryPercentages[j] = max(0, batteryPercentages[j] − 1);
        - Proceed to the next device.
    - If batteryPercentages[i] is equal to 0:
        - Skip testing this device and proceed to the next one.

Return an integer representing the total number of devices that are tested after performing all operations.

Examples:
Input: batteryPercentages = [1, 1, 2, 1, 3]
Output: 3

Input: batteryPercentages = [0, 1, 2]
Output: 2

Дан целочисленный массив batteryPercentages длины n с нумерацией элементов с нуля, где batteryPercentages[i] обозначает уровень заряда батареи i-го устройства.

Необходимо последовательно протестировать устройства с индексами от 0 до n − 1, выполняя следующие действия для каждого устройства i:
    - Если batteryPercentages[i] больше 0:
        - Увеличить счётчик протестированных устройств на 1;
        - Уменьшить уровень заряда всех устройств с индексами j в диапазоне [i + 1, n − 1] на 1;
        - При этом уровень заряда не может стать отрицательным: batteryPercentages[j] = max(0, batteryPercentages[j] − 1);
        - Перейти к следующему устройству.
    - Если batteryPercentages[i] равен 0:
        - Пропустить тестирование этого устройства и перейти к следующему.

Верните целое число - общее количество устройств, которые будут протестированы после выполнения всех операций.

Примеры:
Ввод: batteryPercentages = [1, 1, 2, 1, 3]
Вывод: 3

Ввод: batteryPercentages = [0, 1, 2]
Вывод: 2
'''

from typing import List

def count_tested_devices(batteryPercentages: List[int]) -> int:
    tested = 0
    decrement = 0

    for battery in batteryPercentages:
        if battery - decrement > 0:
            tested += 1
            decrement += 1

    return tested