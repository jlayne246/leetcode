"""
Aim: return all the words in the original string in reverse order without trailing or leading characters, and with only one space between them

Input: 
s - string with words

Output:
result - string with words reversed

Edge cases:
* There is only one character in the string

Strategy:
* Use a loop to traverse array to check for non space, if non-space found:
    * Store the whole word in dictionary or array
* At the end, reconstruct the string in reverse
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        """
        words = s.split()
        words.reverse()
        result = " ".join(words)
        """

        words = []
        word = ""
        result = ""

        for i in range(len(s) + 1):
            if i == len(s) or s[i].isspace() != False:
                if word != "":
                    words.append(word)
                    word = ""
                else:
                    continue
            else:
                word += s[i]

        for i in range(len(words) - 1, -1, -1):
            if i < len(words) - 1:
                result+= " "
            result += words[i]

        return result
