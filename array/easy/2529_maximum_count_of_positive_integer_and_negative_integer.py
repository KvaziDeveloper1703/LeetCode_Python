'''
You are given a list numbers sorted in non-decreasing order.

Define:
    - first_non_negative_index - the index of the first element in numbers that is greater than or equal to 0;
    - first_positive_index - the index of the first element in numbers that is strictly greater than 0;
    - negative_count - the number of negative elements in the list, equal to first_non_negative_index;
    - positive_count - the number of positive elements in the list, equal to len(numbers) - first_positive_index.

Return the maximum of negative_count and positive_count.

Дан список numbers, отсортированный в неубывающем порядке.

Обозначим:
    - first_non_negative_index - индекс первого элемента массива numbers, который больше либо равен 0;
    - first_positive_index - индекс первого элемента массива numbers, который строго больше 0;
    - negative_count - количество отрицательных элементов, равное first_non_negative_index;
    - positive_count - количество положительных элементов, равное len(numbers) - first_positive_index.

Необходимо вернуть максимум из negative_count и positive_count.
'''

from bisect import bisect_left, bisect_right

def maximumCount(numbers):
    first_non_negative_index = bisect_left(numbers, 0)
    first_positive_index = bisect_right(numbers, 0)
    
    negative_count = first_non_negative_index
    positive_count = len(numbers) - first_positive_index
    
    return max(negative_count, positive_count)