class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = count1 = count2 = 0
        word3 = ""

        while (i < (len(word1) + len(word2))):
            if (count1 < len(word1)):
                word3 += word1[count1]
                count1 += 1 

            if (count2 < len(word2)):
                word3 += word2[count2]
                count2 += 1
                
            i += 1

        return word3