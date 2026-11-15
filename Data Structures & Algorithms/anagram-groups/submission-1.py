class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        default_dict = defaultdict()
        for str in strs:
            sorted_str_lst = sorted(str)
            sorted_str = ''.join(sorted_str_lst)
            if sorted_str not in default_dict.keys():
                default_dict[sorted_str] = [str]
            else:
                default_dict[sorted_str].append(str)
        output = []
        for lst in default_dict.values():
            output.append(lst)
        return output