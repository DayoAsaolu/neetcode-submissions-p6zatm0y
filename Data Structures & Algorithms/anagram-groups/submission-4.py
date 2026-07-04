class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsDict = {}
        for i,strWord in enumerate(strs):
            signature = [0 for i in range(26)]
            for char in strWord:
                signature[ord(char)-ord('a')] +=1

            signHash = tuple(signature)
            if signHash not in strsDict:
                strsDict[signHash] = [strs[i]]
            else:
                strsDict[signHash].append(strs[i])

        return list(strsDict.values())
        
