class Solution:
    def isHappy(self, n: int) -> bool:
        hash_set = set()
        res = n
        while True:
            res = self.helper(res)
            if res == 1:
                return True
            if res in hash_set:
                return False
            hash_set.add(res)
                

    def helper(self, n):
        str_n = str(n)
        res = 0
        for c in str_n:
            res += int(c)**2
        return res