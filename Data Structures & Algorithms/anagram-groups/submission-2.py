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
            wordList = [0] * 26
            for i,char in enumerate(word):
                wordList[ord(char) - 97] +=1
            wordTuple = tuple(wordList)
            if wordTuple in strsDict:
                strsDict[wordTuple].append(word)
            else:
                strsDict[wordTuple] = [word]

        ans = []
        
        for k,v in strsDict.items():
            ans.append(v)

        return ans