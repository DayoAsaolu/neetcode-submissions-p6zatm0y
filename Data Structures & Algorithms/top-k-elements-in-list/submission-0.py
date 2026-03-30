class Solution:
    def quickSort(self, arr):
        if len(arr) <= 1:
            return arr
        l,r = 0, len(arr)-1
        mid = (l+r)//2
        pivot = arr[mid]
        left  = [ i for i in arr if i[1] <= pivot[1]]
        right =  [ i for i in arr if i[1] > pivot[1]]
        return self.quickSort(left) + [pivot] + self.quickSort(right)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        sort based on occuremc, return top k
        generate a [ [num, occ], ... ] array
        write quicksort on it, return k top
        """
        numsDict = {}
        for i,n in enumerate(nums):
            if n in numsDict:
                numsDict[n] += 1
            else:
                numsDict[n] = 1
        
        num_occurance_Array = []
        for key,val in numsDict.items():
            num_occurance_Array.append([key,val])

        ans = []
        # sortedNums = self.quickSort(num_occurance_Array)
        sortedNums = sorted(num_occurance_Array, key=lambda x: x[1], reverse=True)
        print(sortedNums)
        for i in range(k):
            print("i:", i)
            ans.append(sortedNums[i][0])

        return ans
        