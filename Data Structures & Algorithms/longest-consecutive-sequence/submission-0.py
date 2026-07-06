class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        ans = 0
        for n in unique:
            if n-1 in unique:
                continue
            head = n
            while head in unique:
                head +=1
            ans = max(ans, head-n)
        
        return ans
        