class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max = 0
        result = []

        for index, val in enumerate(candies):
            if val >= max:
                max = val
        
        for index, val in enumerate(candies):
            candiesGiven = val + extraCandies
            if (candiesGiven) >= max:
                result.append(True)
            else:
                result.append(False)

        return result