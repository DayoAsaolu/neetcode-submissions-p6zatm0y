class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        ans = [[intervals[0][0],intervals[0][1]]]
        curr, nxt = 0, 1

        while nxt < len(intervals):
            curr_in = ans[curr]
            nxt_in  = intervals[nxt]
            if curr_in[1] >= nxt_in[0]:
                curr_in[1] = max(curr_in[1],nxt_in[1])
                nxt +=1
            else:
                ans.append([intervals[nxt][0],intervals[nxt][1]])
                curr +=1
                nxt +=1
        return ans