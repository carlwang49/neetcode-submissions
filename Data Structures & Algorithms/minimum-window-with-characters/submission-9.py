class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if len(t) > len(s):
        #     return ""
        
        # shortest = ""
        # t_set = set(t)
        # for i in range(len(s)): 
        #     s_set = set()  
        #     for j in range(i, len(s)):
        #         if s[j] in t_set:
        #             s_set.add(s[j])
        #         if t_set == s_set:
        #             if shortest == "":
        #                 shortest = s[i:j+1]
        #             elif (j - i + 1) < len(shortest):
        #                 shortest = s[i:j+1]

        # return shortest

        freq = defaultdict(int)
        for char in t:
            freq[char] += 1

        shortest = ""

        def update(i: int, j: int, shortest):
            if shortest == "":
                shortest = s[i:j+1]
            elif (j - i + 1) < len(shortest):
                shortest = s[i:j+1]
            return shortest

        slide = defaultdict(int)
        i = 0
        formed = 0
        for j in range(len(s)):
            slide[s[j]] += 1
            if s[j] in freq.keys() and slide[s[j]] == freq[s[j]]:
                formed += 1
            while formed == len(freq):
                shortest = update(i, j, shortest)
                if s[i] in freq.keys() and slide[s[i]] == freq[s[i]]:
                    formed -= 1
                slide[s[i]] -= 1
                i += 1  

        return shortest



        