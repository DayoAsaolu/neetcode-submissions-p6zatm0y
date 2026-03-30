class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')':'(',
            '}':'{',
            ']': '['
        }
        if len(s) % 2 != 0: return False
        i =0
        stack = []

        while i<len(s):
            curr = s[i]
            if curr not in brackets:
                stack.append(curr)
            else:
                if not stack:
                    return False
                else:
                    if stack.pop() != brackets[curr]:
                        return False
            i+=1
        
        return not stack

