class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # i tracks total length; count1 tracks length of first word; count2 tracks length of second word
        i = count1 = count2 = 0
        # word3 declared as empty string to be appended onto for result
        word3 = ""

        # for loop iterating over length of combined string
        for i in range(len(word1) + len(word2)):
            # conditonal checking if all letters of word1 haven't been exhausted
            if (count1 < len(word1)):
                # if not, appends current letter of word1 to word3
                word3 += word1[count1]
                # increases the counter for word1
                count1 += 1 

            # conditonal checking if all letters of word2 haven't been exhausted
            if (count2 < len(word2)):
                # if not, appends current letter of word2 to word3
                word3 += word2[count2]
                # increases the counter for word2
                count2 += 1

        return word3