"""
    Using bubble sort as inspiration
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if (nums[j] == 0):
                    temp = nums[j]
                    nums[j] = nums [j+1]
                    nums[j+1] = temp

        
        
