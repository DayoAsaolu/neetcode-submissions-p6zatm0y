class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        shadow = []
        for word in strs:
            signature = [0 for i in range(26)]
            for char in word:
                signature[ord(char)-ord('a')] +=1
            shadow.append(signature)

        strsDict = {}
        for i,s in enumerate(shadow):
            signHash = tuple(s)
            if signHash not in strsDict:
                strsDict[signHash] = [strs[i]]
            else:
                strsDict[signHash].append(strs[i])
                
        return list(strsDict.values())
        
