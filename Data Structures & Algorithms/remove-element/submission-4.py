class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i, n in enumerate(nums):
            if n == val:
                k+=1
                nums[i] = float('inf')
        nums.sort()
        return len(nums)-k

        