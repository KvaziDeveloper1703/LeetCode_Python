'''
There are n gas stations arranged in a circle. Each station i provides gas[i] units of gas. It costs cost[i] units of gas to travel from station i to the next station (i + 1) % n.
You have a car with an unlimited gas tank but start with an empty tank. You can begin your journey at any gas station, and your goal is to complete one full circle in the clockwise direction.
Given two integer arrays gas and cost, return the index of the gas station where you should start to successfully complete the circuit. If it is not possible to complete the circuit from any station, return -1.
It is guaranteed that if a solution exists, it is unique.

Examples:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
'''

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0
        current_tank = 0
        start_station = 0

        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            total_tank += gain
            current_tank += gain

            if current_tank < 0:
                start_station = i + 1
                current_tank = 0

        return start_station if total_tank >= 0 else -1