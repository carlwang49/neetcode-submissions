class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # curr_longest_len = 0
        # for i in range(len(s)):
        #     freq = defaultdict(int)
        #     for j in range(i, len(s)):
        #         freq[s[j]] += 1
        #         substring_len = j - i + 1
        #         most_freq_char_num = max(freq.values())
        #         replace_num = substring_len - most_freq_char_num # 
        #         if replace_num <= k:
        #             curr_longest_len = max(curr_longest_len, substring_len)

        # return curr_longest_len
        cur_freq = defaultdict(int)
        for i in range(len(s)):
            cur_freq[s[i]] += 1

        curr_longest_len = 0
        i , j = 0, 0
        freq = defaultdict(int)
        while j < len(s):       
            freq[s[j]] += 1
            substring_len = j - i + 1
            most_freq_char_num = max(freq.values())
            replace_num = substring_len - most_freq_char_num 
            if replace_num > k:
                freq[s[i]] -= 1
                i += 1
            else: # replace_num <= k:
                curr_longest_len = max(curr_longest_len, substring_len)
            j += 1
        return curr_longest_len
           