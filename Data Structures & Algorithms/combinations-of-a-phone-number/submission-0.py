class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not len(digits):
            return []
        
        dic = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }

        # Transfer
        remain = []
        for s in digits:
            remain.append(dic[int(s)])

        res = []
        def dfs(path, remain):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            
            for i in range(len(remain)):
                for j in range(len(remain[i])):
                    print(i, j)
                    path.append(remain[i][j])
                    dfs(path, remain[i+1:])
                    path.pop()

        dfs([], remain)

        return res