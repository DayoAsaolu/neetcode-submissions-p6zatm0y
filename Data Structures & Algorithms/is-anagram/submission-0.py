class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        1st i compare the len of the char - is diff - fasle
        seperate loop, seperate dict - calcuale the count of char
        """
        if len(s) != len(t): return False

        Stringdict = {}
        tDict = {}
        for i in range(len(s)):
            s_char = s[i]

            if s_char not in Stringdict:
                Stringdict[s_char] = 1
            else:
                 Stringdict[s_char] +=1
        
        for i in range(len(t)):
            t_char = t[i]

            if t_char not in Stringdict:
                return False
            else:
                Stringdict[t_char] -= 1
        
        for k,v in Stringdict.items():
            if v != 0:
                return False

        return True
        