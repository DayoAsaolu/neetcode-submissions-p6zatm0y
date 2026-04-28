class Solution:
    def product(self, nums):
        a = 1
        for i in nums:
            a *= i
        return a

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1,2,4,6]
        >. [1, 1, 2,8,48] l->r
        > [48,48,24,6,1] 

        """

        l = len(nums) +1
        lr = [1]*l
        rl = [1]*l
        for i in range(1,l):
            lr[i] =lr[i-1]*nums[i-1]

        for i in range(l-2,-1,-1):
            print(f'{rl[i+1]}, {nums[i]}')
            rl[i] = rl[i+1] * nums[i]

        print(lr)
        print(rl)

        ans = []
        for i in range(len(nums)):
            ans.append(lr[i]* rl[i+1])

        return ans
