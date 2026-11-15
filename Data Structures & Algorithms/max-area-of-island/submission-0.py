class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(i, j):
            # Boundary check
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0

            # Water or already visited
            if grid[i][j] == 0:
                return 0

            # Mark as visited
            grid[i][j] = 0

            area = 1  # Current cell

            # Explore 4 directions
            area += dfs(i + 1, j)  # down
            area += dfs(i - 1, j)  # up
            area += dfs(i, j + 1)  # right
            area += dfs(i, j - 1)  # left

            return area

        max_len = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # Start tracing one island
                    max_len = max(max_len, dfs(i, j))

        return max_len