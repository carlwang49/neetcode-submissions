class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(j, i, grid, visited):
            print("hi")
            if i < 0 or i >= len(grid[0]):
                return
            if j < 0 or j >= len(grid):
                return
            if grid[j][i] == "0":
                return
            if (j, i) in visited:
                return 
            else:            
                visited.add((j, i))
                # right
                i += 1
                dfs(j, i, grid, visited)
                i -= 1

                # down
                j += 1
                dfs(j, i, grid, visited)
                j -= 1

                # left
                i -= 1
                dfs(j, i, grid, visited)
                i += 1

                # up
                j -= 1
                dfs(j, i, grid, visited)
                j += 1


        land_num = 0
        visited = set()
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                print(j, i)
                if grid[j][i] == "1" and (j, i) not in visited:
                    dfs(j, i, grid, visited)
                    print("****")
                    land_num += 1
                    print(land_num)
                    print(visited)
        
        return land_num
                    

        