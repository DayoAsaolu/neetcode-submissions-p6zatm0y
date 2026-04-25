

class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["Hello","World"]
        # "5,5"+"HelloWorld" "5,5,#HelloWorld"
        # "5,5"+"HelloWorld" -> ["Hello","World"]
	
        if len(strs) == 0:
            return ""
        
        sizeArr = []
        for word in strs:
            sizeArr.append(str(len(word)))
            sizeArr.append(",")
        sizeArr.append("#")
        
        # [5,”,”,5,”,”]
        wordArr = ["".join(strs)]
        res = "".join(sizeArr + wordArr)

        return res

    def decode(self, s: str) -> List[str]:
        if len(s) == 0: return []
        strSplit = s.split("#",1)
        sizeSeg = strSplit[0]
        wordSeg = strSplit[1]
        sizeArr = sizeSeg[:-1].split(",")

        
        ans = []
        lastPos = 0
        for count in sizeArr:
            c = int(count)
            if c == 0:
                ans.append("")
            else:
                ans.append(wordSeg[lastPos:c+lastPos])
                lastPos += c

        return ans