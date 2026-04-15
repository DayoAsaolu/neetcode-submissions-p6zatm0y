class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        ["act","pots","tops","cat","stop","hat"]

        [["hat"],["act", "cat"],["stop", "pots", "tops"]]

        n*mlogm
        0(n)

        """
        strsDict = {}
        for word in strs:
            k = "".join(sorted(word))
            if k in strsDict:
                strsDict[k].append(word)
            else:
                strsDict[k] = [word]

        ans = []
        
        for k,v in strsDict.items():
            ans.append(v)

        return ans