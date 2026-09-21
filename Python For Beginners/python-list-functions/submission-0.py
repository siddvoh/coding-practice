from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    sum = 0
    for n in nums:
        sum+=n
    return sum

def get_max(nums: List[int]) -> int:
    maximum = nums[0]
    for n in nums:
        if n>maximum:
            maximum = n
    return maximum

def get_min(nums: List[int]) -> int:
    minimum = nums[0]
    for n in nums:
        if n<minimum:
            minimum = n
    return minimum

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
