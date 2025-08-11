class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = []
        
        left = [1]
        right = [1]

        for i in range(1, len(nums)):
            currProd = left[i-1] * nums[i-1]
            left.append(currProd)

        for i in range(len(nums) - 1, 0, -1):
            currProd = right[len(nums) - i - 1] * nums[i]
            right.append(currProd)

        right.reverse()

        for i in range(len(nums)):
            prods.append(left[i] * right[i])
        
        return prods
                

                
