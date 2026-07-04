class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        [1,2,2,2,3,3,3], k = 1  - create bucket list
        1.create dict to count occure - k=num, v=occurance
        1.create bucket of len(nums) [[]... []] or use append
        2.loop thr dict, put into bucker[occur].append(num) 
         [[],[1],[2],[3]]
        3. if i do [[]... []] loop thr buck from n-1, avoid [], but if append, loop normal
        count the (num), once equal to k, return

        """
        numsDict = {}
        for n in nums:
            if n not in numsDict:
                numsDict[n] = 1
            else:
                numsDict[n] +=1
            
        bucket = [[] for i in range(len(nums)+1)]
        for number, occur in numsDict.items():
            bucket[occur].append(number)
        
        need = k
        ans = []
        print(bucket)
        for i in range(len(nums),-1, -1):
            buc = bucket[i]
            print(buc)
            have = len(buc)
            if have == 0:
                continue
            need -= have
            if need == 0:
                ans += buc
                return ans
            elif need >0:
                ans += buc
            else:
                ans += buc[:need+1]
                return ans
        return ans