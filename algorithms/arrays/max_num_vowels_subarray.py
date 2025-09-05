"""
Aim: To calculate the maximum number of vowels in any substring with the length k

Strategy:
* Sliding window: Count the number of vowels in the window space, and keep moving the window across the array (removing any that are taken out) and calculate the maximum in each iteration.
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']

        left = 0
        countVowels = 0
        maxVowels = 0

        for right in range(len(s)):
            if s[right] in vowels:
                countVowels+=1

            if (right - left) >= k:
                if s[left] in vowels:
                    countVowels-=1

                left+=1

            maxVowels = max(maxVowels, countVowels)

        return maxVowels
