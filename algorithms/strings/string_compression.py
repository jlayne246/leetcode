"""
Aim: return the length of a produced array such that it lists the groups and the numbers

Strategy:
* use two pointers, one to determine the current position and the current write position
* have a tracker keeping track of the current letter
* have a counter keeping track of the letter's count if count > 1
* once the current letter != saved letter, then overwrite with the letter at the write place with the count after; reset current letter and count
* return size of the array

Edge cases:
* the count >= 10; convert it to individual digits, iterate over digits for overwrite
* only one element; the overwrite for the count would not happen
* all unique characters; the overwrite for the count would not happen
"""

class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        curr = chars[0]
        count = 1

        for read in range(1, len(chars) + 1):
            if read == len(chars) or curr != chars[read]:
                chars[write] = curr
                write+=1
                
                if count > 9:
                    digits = str(count)

                    for i in digits:
                        chars[write] = i
                        write+=1
                elif count > 1:
                    chars[write] = str(count)
                    write+=1
                
                if read != len(chars):
                    curr = chars[read]
                    count = 1
            else:
                count+=1

        return len(chars[:write])
