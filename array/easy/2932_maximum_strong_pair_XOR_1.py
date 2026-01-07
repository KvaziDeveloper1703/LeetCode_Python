'''
You are given a 0-indexed integer array called numbers.

A pair of integers (x, y) is called a strong pair if the absolute difference between x and y is less than or equal to the smaller of the two numbers.

Your task is to choose two integers from the array numbers such that:
    - they form a strong pair, and
    - the bitwise XOR of the two numbers is as large as possible.

You are allowed to choose the same number twice, so a pair like (x, x) is valid.

Return the maximum XOR value that can be obtained from any strong pair in the array.

Examples:
Input: numbers = [1, 2, 3, 4, 5]
Output: 7

Input: numbers = [10, 100]
Output: 0

Дан целочисленный массив numbers с индексацией с нуля.

Пара целых чисел (x, y) называется сильной парой, если модуль разности между числами меньше либо равен меньшему из них.

Необходимо выбрать два числа из массива numbers так, чтобы:
    - они образовывали сильную пару, и
    - их побитовое исключающее ИЛИ (XOR) было максимальным.

Разрешается выбирать одно и то же число дважды, поэтому пара вида (x, x) считается допустимой.

Нужно вернуть максимальное значение XOR, которое можно получить среди всех сильных пар в массиве.

Примеры:
Ввод: numbers = [1, 2, 3, 4, 5]
Вывод: 7

Ввод: numbers = [10, 100]
Вывод: 0
'''

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert_number(self, number: int):
        current_node = self.root
        for bit_index in range(31, -1, -1):
            bit = (number >> bit_index) & 1
            if bit not in current_node.children:
                current_node.children[bit] = TrieNode()
            current_node = current_node.children[bit]
    
    def get_maximum_xor(self, number: int) -> int:
        current_node = self.root
        maximum_xor_value = 0
        
        for bit_index in range(31, -1, -1):
            bit = (number >> bit_index) & 1
            opposite_bit = 1 - bit
            
            if opposite_bit in current_node.children:
                maximum_xor_value |= (1 << bit_index)
                current_node = current_node.children[opposite_bit]
            else:
                current_node = current_node.children[bit]
        
        return maximum_xor_value


class Solution:
    def maximumStrongPairXor(self, numbers: List[int]) -> int:
        numbers.sort()
        
        maximum_result = 0
        left_index = 0
        binary_trie = Trie()
        
        for right_index in range(len(numbers)):
            while numbers[right_index] > 2 * numbers[left_index]:
                left_index += 1
                binary_trie = Trie()
                for index in range(left_index, right_index):
                    binary_trie.insert_number(numbers[index])
            
            binary_trie.insert_number(numbers[right_index])
            current_xor = binary_trie.get_maximum_xor(numbers[right_index])
            maximum_result = max(maximum_result, current_xor)
        
        return maximum_result