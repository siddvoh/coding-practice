import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    nnums = [-1*n for n in nums]
    heapq.heapify(nnums)
    return [-1*heapq.heappop(nnums) for _ in range(len(nnums))]





# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
