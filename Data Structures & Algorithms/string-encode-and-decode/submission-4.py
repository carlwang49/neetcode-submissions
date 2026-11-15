class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs:
           code = str(len(s)) + "#" + s + code 
        return code

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = i
        while s:
            if s[j] != "#":
                j += 1
                continue
            else: # s[j] == "#"
                n = int(s[i:j])
                word = s[j+1:j+n+1]
                res.insert(0, word)
                s = s[j+n+1:] # slice
                i = 0
                j = i
        return res