class Solution:
    def direction(self, r,c):
        return [(r,1+c), (r,-1+c), (-1+r,c),(1+r,c)]
        
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
        gridQueue = [source]
        
        while gridQueue:
            curr = gridQueue.pop(0)
            cX, cY = curr[0], curr[1]
            grid[cX][cY] = "0"
            nei = self.direction(cX,cY)
            
            for nX,nY in nei:
                if nX <0 or nY<0 or nX >= ROWS or nY >= COLS or grid[nX][nY] == "0":
                    continue
                
                gridQueue.append((nX,nY))
                
        return