'''
A biker is going on a road trip that includes n + 1 points, each at a different altitude. The biker starts at point 0, and the altitude at this point is 0.

You are given an integer array gain of length n, where each gain[i] represents the change in altitude when moving from point i to point i + 1.

Using this information, determine and return the highest altitude the biker reaches during the trip.

Мотоциклист отправляется в поездку, которая состоит из n + 1 точек на разной высоте. Он начинает в точке 0 с высотой 0.

Дан массив gain длиной n, где каждый элемент gain[i] обозначает изменение высоты при переходе от точки i к точке i + 1.

На основе этих изменений нужно определить и вернуть наибольшую высоту, которую мотоциклист достигает за всю поездку.
'''

from typing import List

def largest_altitude(gain: List[int]) -> int:
    max_altitude = 0
    current_altitude = 0

    for altitude_change in gain:
        current_altitude += altitude_change
        max_altitude = max(max_altitude, current_altitude)

    return max_altitude