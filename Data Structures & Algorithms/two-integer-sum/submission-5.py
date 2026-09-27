from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = defaultdict(int)
        for i,n in enumerate(nums):
            if target-n in diff:
                return [diff[target-n], i]
            else:
                diff[n] = i
        return []