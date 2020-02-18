class Solution(object):
    def dfs(self,i,j,matrix,explored,prev):
        rows, cols = len(matrix),len(matrix[0])
        if i < 0 or i >= rows or j < 0 or j >= cols or (i,j) in explored or matrix[i][j] < prev:
            return
        explored.add((i,j))
        self.dfs(i-1,j,matrix,explored,matrix[i][j]) #up
        self.dfs(i+1,j,matrix,explored,matrix[i][j]) #down
        self.dfs(i,j-1,matrix,explored,matrix[i][j]) #left
        self.dfs(i,j+1,matrix,explored,matrix[i][j]) #right
        
    def pacificAtlantic(self, matrix):
        if not matrix: return []
        pacific,atlantic = set(),set()
        rows, cols = len(matrix),len(matrix[0])
        for i in range(cols):
            self.dfs(0,i,matrix,pacific,-1)
            self.dfs(rows-1,i,matrix,atlantic,-1)
        for i in range(rows):
            self.dfs(i,0,matrix,pacific,-1)
            self.dfs(i,cols-1,matrix,atlantic,-1)
        return list(pacific&atlantic)

sol = Solution()
matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
matrix =[]
matrix = [[1]]
print(sol.pacificAtlantic(matrix))