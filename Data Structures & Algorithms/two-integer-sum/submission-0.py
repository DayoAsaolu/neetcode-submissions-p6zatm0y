class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        numsDict = {3:0}
        """
        numsDict = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in numsDict:
                return [ numsDict[diff], i ]
            numsDict[n] = i
        