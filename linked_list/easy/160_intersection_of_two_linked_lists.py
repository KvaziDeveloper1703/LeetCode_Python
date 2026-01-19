'''
Given the heads of two singly linked lists headA and headB, return the node where the two lists intersect.

If the lists do not intersect, return null.

Important notes:
    - The linked lists do not contain cycles;
    - After the function returns, both lists must keep their original structure;
    - Intersection means both lists share the same node reference in memory, not just the same value.

Examples:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'

Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'

Даны головы двух односвязных списков headA и headB. Нужно вернуть узел, в котором эти два списка пересекаются.

Если пересечения нет, верни null.

Важные условия:
    - В списках нет циклов;
    - После выполнения функции структура списков должна остаться без изменений;
    - Пересечение означает, что оба списка указывают на один и тот же узел в памяти, а не просто имеют одинаковое значение.

Примеры:
Ввод: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Вывод: Intersected at '8'

Ввод: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Вывод: Intersected at '2'
'''

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None

        pointerA = headA
        pointerB = headB

        while pointerA != pointerB:
            if pointerA is None:
                pointerA = headB
            else:
                pointerA = pointerA.next

            if pointerB is None:
                pointerB = headA
            else:
                pointerB = pointerB.next

        return pointerA