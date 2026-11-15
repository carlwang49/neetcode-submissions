class Solution:
    def trap(self, height: List[int]) -> int:
        # min(height[l], height[r]) - height[i]
        
        # 找每一個位置的左邊牆和右牆
        # 0 -> 0, 2
        # 1 -> 0, 3
        # 2 -> 2, 3
        # 3 -> 0, 0
        # 4 -> 3, 3
        # 5 -> 3, 3
        # 6 -> 3, 3
        # 7 -> 0, 0
        # 8 -> 3, 0
        # 9 -> 3, 0
        left_wall = []
        max_left = 0
        for l in range(len(height)):
            left_wall.append(max_left)
            max_left = max(max_left, height[l])

        right_wall = []
        max_right = 0
        for r in range(len(height)-1, -1, -1):
            right_wall.append(max_right)
            max_right = max(max_right, height[r])
        
        right_wall.reverse()

        res = 0
        for i in range(len(height)):
            trapped = min(left_wall[i], right_wall[i]) - height[i]
            if trapped >= 0:
                res += trapped
        
        return res

                