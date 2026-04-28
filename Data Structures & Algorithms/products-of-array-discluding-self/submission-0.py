class Solution:
    def product(self, nums):
        a = 1
        for i in nums:
            a *= i
        return a

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
            [1,2,4,6]
            [48,24,12,8]

            [-1,0,1,2,3]
            [0,-6,0,0,0]
        """
        ans = []
        for i,n in enumerate(nums):
            subArr = nums[:i] + nums[i+1:]
            p = self.product(subArr)
            ans.append(p)

        return ans
