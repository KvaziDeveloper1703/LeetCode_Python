'''
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses in order to make the input string valid.

Return a list of unique valid strings that can be obtained by performing the minimum number of removals.
You may return the answer in any order.

Examples:
Input:  s = "()())()"
Output: ["(())()", "()()()"]

Input:  s = "(a)())()"
Output: ["(a())()", "(a)()()"]

Дана строка s, которая содержит скобки и буквы.
Нужно удалить минимальное количество некорректных скобок, чтобы сделать строку валидной (правильно сбалансированной).

Верните список уникальных валидных строк, которые можно получить при минимальном количестве удалений.
Ответ можно вернуть в любом порядке.

Примеры:
Ввод:  s = "()())()"
Вывод: ["(())()", "()()()"]

Ввод:  s = "(a)())()"
Вывод: ["(a())()", "(a)()()"]
'''

from typing import List
from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0
        
        result = []
        visited = set()
        queue = deque([s])
        found_level = False
        
        while queue:
            current = queue.popleft()
            
            if is_valid(current):
                result.append(current)
                found_level = True
            
            if found_level:
                continue
            
            for i in range(len(current)):
                if current[i] not in ('(', ')'):
                    continue
                next_state = current[:i] + current[i+1:]
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append(next_state)
        
        return result