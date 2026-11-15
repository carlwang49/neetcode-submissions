class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        # memo to avoid recomputation
        pacific_memo = {}
        atlantic_memo = {}

        def go_pacific(r, c, visited):
            # Reach Pacific (top or left border)
            if r == 0 or c == 0:
                return True

            if (r, c) in pacific_memo:
                return pacific_memo[(r, c)]

            visited.add((r, c))

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    # Can only flow to lower or equal height
                    if heights[nr][nc] <= heights[r][c] and (nr, nc) not in visited:
                        if go_pacific(nr, nc, visited):
                            pacific_memo[(r, c)] = True
                            return True

            pacific_memo[(r, c)] = False
            return False

        def go_atlantic(r, c, visited):
            # Reach Atlantic (bottom or right border)
            if r == m - 1 or c == n - 1:
                return True

            if (r, c) in atlantic_memo:
                return atlantic_memo[(r, c)]

            visited.add((r, c))

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if heights[nr][nc] <= heights[r][c] and (nr, nc) not in visited:
                        if go_atlantic(nr, nc, visited):
                            atlantic_memo[(r, c)] = True
                            return True

            atlantic_memo[(r, c)] = False
            return False

        ans = []
        for r in range(m):
            for c in range(n):
                if go_pacific(r, c, set()) and go_atlantic(r, c, set()):
                    ans.append([r, c])

        return ans