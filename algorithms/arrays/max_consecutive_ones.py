"""
    Inputs: nums (list) which is an array of 1's and 0's, k (int) which is the maximum number of 0's to be flipped

    Outputs: int - max number of contiguous 1's

    Aim: to find the maximum number of consecutive 1's in an array within the limit, k

    Possible Pattern: sliding window

    Edge case: 
        - All 0's
        - All 1's

    Pseudocode: 
        left = 0
        count_zeros = 0
        max_len = 0

        for right from left to length(nums) do:
            if nums[right] == 0 then:
                count_zeros++

            if count_zeros > k then:
                if nums[left] == 0 then:
                    count_zeros--
                left++

            max_len = max(max_len, right - left + 1)

        return max_len
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        count_zeros = 0
        max_len = 0

        for right in range(left, len(nums)):
            if nums[right] == 0:
                count_zeros+=1

            if count_zeros > k:
                if nums[left] == 0:
                    count_zeros-=1
                left+=1

            max_len = max(max_len, right - left + 1)

        return max_len