class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l, r = 0,len(s)-1

        while l < r:
            char_l, char_r = s[l], s[r]
            if not char_l.isalnum():
                l +=1
                continue
            if not char_r.isalnum():
                r -=1
                continue
            if char_l.lower() != char_r.lower():
                return False
            else:
                l +=1
                r -=1
        
        return True
            
        