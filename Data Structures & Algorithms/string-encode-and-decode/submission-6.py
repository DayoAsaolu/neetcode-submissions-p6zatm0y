class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        ["he:llo", "world:wide:web"] = ":6:he:llo:12:world:wide:web"

        ["","he:llo", "world:wide:web", "pan al", ":::", ": :45"] =
          ":0::6:he:llo:14:world:wide:web:6:pan al:3:::::5:: :45"

        rule - the starting is always ":", 
        then i keep till i find the nxt colon which closes it,
         if the number in between is 0, then it empty string, 
         else the len of the next string
        """
        s = ":"
        for w in strs:
            if len(w) == 0:
                s += "0::"
            else:
                w_len = len(w)
                s += str(w_len) + ":" + w + ":"
        return s

    def decode(self, s: str) -> List[str]:
        """

        """
        ans, r = [], 0
        while r+1 < len(s):
            if s[r+1] == "0":
                ans.append("")
                r += 3
            else:
                # find the closing delimiter
                strCount = r + 1
                while s[strCount] != ":":
                    strCount += 1
                w_len = int(s[r + 1:strCount])
                ans.append(s[strCount+1: w_len+strCount+1])
                r = w_len+strCount+1
        # :5:Hello:5:World:
           
        return ans
