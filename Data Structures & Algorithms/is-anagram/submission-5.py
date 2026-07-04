class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sign = [0 for i in range(26)]

        for char in s:
            sign[ord(char)- ord('a')] +=1

        for char in t:
            sign[ord(char)- ord('a')] -=1

        for n in sign:
            if n != 0:
                return False

    
        return True