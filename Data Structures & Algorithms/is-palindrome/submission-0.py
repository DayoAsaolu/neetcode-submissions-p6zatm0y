class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = ""
        s = s.lower()
        for char in s:
            if not char.isalnum():
                continue
            n += char

        print(n)
        return n[::-1] == n