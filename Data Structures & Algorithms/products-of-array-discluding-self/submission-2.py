class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Everything to the left of i (indices 0 to i-1)
        Everything to the right of i (indices i+1 to n-1)
        Prefix/suffix product trick: prefix[i] = product of everything strictly left of i (stops before i by definition), suffix[k] = product of everything from k onward (includes k) — so to exclude nums[i] from both sides, multiply prefix[i] * suffix[i+1], since the suffix has to start one index past i to avoid including it.

        [1,2,3,4] => [1,  1,  2,  6,  24]
        [1,2,3,4] => [24, 24, 12, 4,  1]
                     [24,12,8,6]

        """
        l = len(nums)+1 # 5
        prefix, suffix = [1 for i in range(l)], [1 for i in range(l)]

        for i in range(1, l):  # i, range(1,5)
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(l-2, -1, -1): # i, range(3,-1,-1)
            suffix[i] = suffix[i+1] * nums[i]

        ans = [1 for i in range(l-1)]
        for i in range(l-1):
            ans[i] = prefix[i] * suffix[i+1]
        return ans