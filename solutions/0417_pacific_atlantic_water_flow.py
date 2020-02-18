from typing import List
import collections 

class Solution:
    def bfs(self, matrix, row, col, ocean):
        visited = set()
        queue = [(row, col)]
        ocean[row][col] = 1
        rows, cols = len(matrix), len(matrix[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        # 1 While queue not empty  
        while queue:
            curr_r, curr_c = queue.pop(0)
            prev_val = matrix[curr_r][curr_c]
            if (curr_r, curr_c) not in visited:
                visited.add((curr_r, curr_c))
                # Neighbors
                for direction in directions:
                    next_r, next_c = curr_r + direction[0], curr_c + direction[1]
                    try:
                        # 2 Check necessary conditions to add in queue
                        if 0 <= next_r < rows and 0 <= next_c < cols and matrix[next_r][next_c] >= prev_val:
                            queue.append((next_r, next_c))
                            ocean[next_r][next_c] = 1
                    except Exception as ex:
                        print(row)
                        print(col)
                        print(ex)

    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix  or not matrix[0]: 
            return []
        rows, cols = len(matrix), len(matrix[0])
        # 1 create two matrix one for Pacific one for Atlantic
        atlantic = [[0 for x in range(cols)] for y in range(rows)] 
        pacific = [[0 for x in range(cols)] for y in range(rows)] 
        # 2 Start from oceans and follow the flow from ocean to top
        # Loop top and bottom
        for col in range(len(matrix[0])):
            #pacific[0][col]=atlantic[rows-1][0] = 1
            self.bfs(matrix, 0,   col,    pacific)
            self.bfs(matrix, rows-1, col, atlantic)
        # Loop left and right
        for row in range(len(matrix)):
            #pacific[row][0]=atlantic[row][cols-1] = 1
            self.bfs(matrix, row, 0,      pacific)
            self.bfs(matrix, row, cols-1, atlantic)
        res = []
        # 3 Find the intersection of the two solutions groups and create the final solution
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if( atlantic[i][j] == 1 and pacific[i][j] == 1 ):
                    res.append((i,j))
        return res

    

sol = Solution() 
matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(sol.pacificAtlantic(matrix))