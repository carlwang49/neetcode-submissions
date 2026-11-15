class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        max_len = 0
        for c in s:
            if c in window:
                # 有重複的
                # 把重複的下一個當作開頭, 重新算最長的 sequence
                idx = window.index(c)
                window = window[idx+1:]
            window.append(c)
            max_len = max(max_len, len(window))
            
        return max_len
                