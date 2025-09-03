"""
Aim: Move all the 0's to the end of the array while preserving the order of everything else
Strategy:
* Using bubble sort as inspiration, if an element is 0, then bubble it down to the end of the array by swapping elements
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

        
        
