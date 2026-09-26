import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    pairs = []
    for n in nums:
        pairs.append((-n, n))
    heapq.heapify(pairs)
    return [-1*heapq.heappop(pairs)[0] for _ in range(len(pairs))]



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
