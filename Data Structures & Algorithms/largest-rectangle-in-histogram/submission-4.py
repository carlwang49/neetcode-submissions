class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 計算每一個柱子他左邊邊界和右邊界

        largest = 0
        left_stack = []
        for i in range(len(heights)):
            if not left_stack:
                left_stack.append(i)
            elif heights[i] >= heights[left_stack[-1]]:
                left_stack.append(i)
            else:
                while left_stack and heights[i] < heights[left_stack[-1]]:
                    curr_height_idx = left_stack.pop()
                    left_height_idx = left_stack[-1] if left_stack else (-1)
                    largest = max(largest, heights[curr_height_idx]*(i-left_height_idx-1))
                left_stack.append(i)

        # 若還有剩下
        while len(left_stack) > 1:
            curr_height_idx = left_stack.pop()
            largest = max(largest, heights[curr_height_idx] * (len(heights) - left_stack[-1] - 1))
        
        # 處理最矮的
        largest = max(largest, heights[left_stack[0]]* (len(heights) - (-1) - 1))
        
        return largest


