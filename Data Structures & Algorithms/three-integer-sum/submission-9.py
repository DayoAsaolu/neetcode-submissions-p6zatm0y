class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        [-1,0,1,2,-1,-4]
        [-4,-1,-1,0,1,2]
        """
        nums, ans = sorted(nums), []
        for i,n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                two_pairs = nums[l] + nums[r]
                total = two_pairs + n
                if total == 0:
                    ans.append([n,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return ans