"""
Aim: Return whether there are three indicies with three values in ascending order (not necessarily consecutive)

Strategy: 
* three nested loops branching from each point to determine truth (too much time)
* track the smallest in the array, find the next largest, and then see if there is another one that is greater after that (by seeing if there is nothing less than the second number)

Edge case:
* less than three elements in array
"""

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] < nums[j] < nums[k]:
                        return True
        """

        i = j = 999999999999999999999999999999999

        for num in nums:
            if num <= i:
                i = num 
            elif num <= j:
                j = num
            else:
                # Found a possible value greater than j, hence k 
                return True

        return False
