class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        maxAverage = window_sum / k

        for right in range(k, len(nums)):
            window_sum += nums[right] - nums[right - k]
            avg = window_sum / k
            maxAverage = max(maxAverage, avg)

        return maxAverage
        