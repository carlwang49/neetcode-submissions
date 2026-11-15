class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 維持長度為 3 的滑動窗口
        # 如果 substring 裡面的字母沒有在 s3 裡面出現過, 往右移動一格
        # def isEqual(s1, s2):
        #     stack = []
        #     for c in s1:
        #         stack.append(c)
        #     for c in s2:
        #         if c in stack:
        #             stack.remove(c)
        #     return True if not stack else False

        # i, j = 0, len(s1) - 1
        # ans = False
        # while j < len(s2):
        #     if isEqual(s1, s2[i:j+1]):
        #         ans = True
        #         break
        #     i += 1
        #     j += 1

        # return ans
        if len(s2) < len(s1):
            return False

        i, j = 0, len(s1) - 1
        freq_of_sub_s2 = defaultdict(int)
        freq_of_s1 = defaultdict(int)
        for k in range(0, len(s1)):
            freq_of_sub_s2[s2[k]] += 1
            freq_of_s1[s1[k]] += 1
        if freq_of_s1 == freq_of_sub_s2:
            return True
        freq_of_sub_s2[s2[i]] -= 1
        i += 1
        j += 1
        while j < len(s2):
            freq_of_sub_s2[s2[j]] += 1 
            print(freq_of_sub_s2, freq_of_s1)
            if Counter(freq_of_s1) == Counter(freq_of_sub_s2):
                return True
            freq_of_sub_s2[s2[i]] -= 1
            i += 1
            j += 1
            
        return False







            
        

