"""
Aim: To find a contiguous subarray with length k that has the maximum average, and return said average

Strategy:
* use a fixed sliding window (with the sum of said window saved and calcuate the initial average)
* moving right, add the next value in the array and remove the first in the window, and recalculate the average
* check to see if it is greater than the maximum at each point
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        maxAverage = window_sum / k

        for right in range(k, len(nums)):
            window_sum += nums[right] - nums[right - k]
            avg = window_sum / k
            maxAverage = max(maxAverage, avg)

        return maxAverage
        
