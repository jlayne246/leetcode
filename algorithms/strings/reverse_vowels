class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(letter):
            vowels = "aeiouAEIOU"
            return letter in vowels

        myVowels = []
        result = ""

        for index, letter in enumerate(s):
            if isVowel(letter):
                myVowels.append(letter)

        for index, letter in enumerate(s):
            if isVowel(letter):
                result += myVowels.pop()
                continue
            result += letter
        
        return result
