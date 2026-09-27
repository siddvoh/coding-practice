class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        mid = len
        return nums[len(nums)//2]
        