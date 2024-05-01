class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        p=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 1):
                    p += 4 
                    if(i>0 and grid[i-1][j]==1):
                        p-=1
                    if(j>0 and grid[i][j-1]==1):
                        p-=1
                    if(j != (len(grid[0])-1) and grid[i][j+1]==1):
                        p-=1
                    if(i!=(len(grid)-1) and grid[i+1][j]==1):
                        p-=1            
        return p