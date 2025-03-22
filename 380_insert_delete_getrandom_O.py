'''
Design and implement a class RandomizedSet that supports inserting, removing, and retrieving random elements—all in average O(1) time complexity.
+ The class should be initialized using RandomizedSet().
+ The insert(val) method inserts an element val into the set if it is not already present. It returns true if the element was successfully inserted and false if it already exists.
+ The remove(val) method removes the element val from the set if it is present. It returns true if the element was removed and false if it was not found.
+ The getRandom() method returns a random element from the current set. It is guaranteed that at least one element exists when this method is called, and each element must have an equal probability of being returned.

All operations must run in average O(1) time.

Example:
Input:
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]

Output:
[null, true, false, true, 2, true, false, 2]
'''

import random

class RandomizedSet:

    def __init__(self):
        self.val_to_index = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.values.append(val)
        self.val_to_index[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        index_to_remove = self.val_to_index[val]
        last_element = self.values[-1]
        self.values[index_to_remove] = last_element
        self.val_to_index[last_element] = index_to_remove
        self.values.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)