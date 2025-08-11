class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def getIndicies(len, index):
            if (len > 1):
                if (index == 0):
                    return index + 1
                elif (index == len-1):
                    return index - 1
                else:
                    return [index - 1, index + 1]
            else:
                return index


        count = 0

        for i in range(len(flowerbed)):
            if (flowerbed[i] == 0):
                indicies = getIndicies(len(flowerbed), i)
                if (type(indicies) == type(flowerbed)):
                    if flowerbed[indicies[0]] == 0 and flowerbed[indicies[1]] == 0:
                        count += 1
                        flowerbed[i] = 1
                else:
                    if flowerbed[indicies] == 0:
                        count += 1
                        flowerbed[i] = 1

        return count >= n
