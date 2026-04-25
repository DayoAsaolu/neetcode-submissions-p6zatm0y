from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    self.bfs([r,c],grid, ROWS, COLS)
                    count +=1
        
        return count
        
    def bfs(self, source, grid, ROWS, COLS):
        gridQueue = deque([source])
        
        while gridQueue:
            curr = gridQueue.popleft()
            cX, cY = curr[0], curr[1]
            directions = [(0,1), (0,-1), (-1,0),(1,0)]
        
            for pX,pY in directions:
                nX, nY = cX+pX, cY+pY
                if nX <0 or nY<0 or nX >= ROWS or nY >= COLS or grid[nX][nY] == "0":
                    continue
                
                gridQueue.append((nX,nY))
                grid[nX][nY] = "0"
                
        return