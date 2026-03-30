class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        for each w in strs - create {(0,0,....0) = [word]}
        for k,v in dict.items
        """
        strsDict = {}
        for word in strs:
            tmp = [0] * 26
            for char in word:
                tmp[97 - ord(char)] += 1
            t = tuple(tmp)
            if t in strsDict:
                strsDict[t].append(word)
            else:
                strsDict[t] = [word]

        ans = []
        for k,v in strsDict.items():
            ans.append(v)

        return ans
        