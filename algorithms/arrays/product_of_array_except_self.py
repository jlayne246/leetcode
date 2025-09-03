"""
    Aim: To return an array where each element is a product of everything else except itself

    Strategy:
    * Start multiplying products from the left whereby the first will be effectively 1, and append to the left array so that it continually multiplies the previous product by the previous number. So in effect, it stores the product of all values to the current index's left
    * Do the same for the right, but start from the other side
    * Reverse the right, and multiply the elements of each in order
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = []
        
        left = [1]
        right = [1]

        for i in range(1, len(nums)): # determining left prefix
            currProd = left[i-1] * nums[i-1]
            left.append(currProd)

        #print(left)

        for i in range(len(nums) - 1, 0, -1): # determining right suffix
            currProd = right[len(nums) - i - 1] * nums[i]
            right.append(currProd)

        #print(right)

        right.reverse()

        for i in range(len(nums)):
            prods.append(left[i] * right[i])
        
        return prods
                

                
