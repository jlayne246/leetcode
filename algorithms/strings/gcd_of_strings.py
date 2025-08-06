class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if len(str1) >= len(str2):
            str1, str2 = str2, str1 # str1 would always be shorter

        for i in range(len(str1), 0, -1):
            if (len(str1) % i) or (len(str2) % i):
                print ("Not divisible by: ", i)
                continue

            n1 = len(str1) // i
            n2 = len(str2) // i
            print (n1, n2)

            base = str1[:i]
            print(base)

            if (str1 == n1 * base) and (str2 == n2 * base):
                return base
        
        return ""
        