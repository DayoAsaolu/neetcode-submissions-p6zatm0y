class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = {}
        for num in nums:
            if num in unique:
                return True
            unique[num] = num

        return False