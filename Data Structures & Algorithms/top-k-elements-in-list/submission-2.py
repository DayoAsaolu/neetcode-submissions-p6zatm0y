class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        [1,2,2,3,3,3], k = 2 - { 1:1, 2:2, 3:3 }
        1. dict - { 1:1, 2:2, 3:3 }
        2. convert to list numsList = [ [1,1], [2,2], [3,3] ]
        3. sort - greater>lower by i[2]
        4. return numsList[:k]

        """
        numsDict = {}
        for n in nums:
            if n not in numsDict:
                numsDict[n] = 1
            else:
                numsDict[n] +=1
        
        numsList = []
        for key,val in numsDict.items():
            numsList.append([key,val])
        
        print(numsList)
        
        numsList = sorted(numsList, key=lambda x: x[1], reverse=True)
        ans = [ i[0] for i in numsList]

        return ans[:k]
        