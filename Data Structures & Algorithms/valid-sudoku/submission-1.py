class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        blocks = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                num = board[col][row]
                if num != ".":
                    if row <= 2 and col <= 2:
                        if int(num) not in blocks[0]:
                            blocks[0].add(int(num))
                        else:
                            return False
                    if 2 < row <= 5 and col <= 2:
                        if int(num) not in blocks[1]:
                            blocks[1].add(int(num))
                        else:
                            return False
                    if 5 < row <= 8 and col <= 2:
                        if int(num) not in blocks[2]:
                            blocks[2].add(int(num))
                        else:
                            return False
                    
                    if row <= 2 and 2 < col <= 5:
                        if int(num) not in blocks[3]:
                            blocks[3].add(int(num))
                        else:
                            return False
                    if 2 < row <= 5 and 2 < col <= 5:
                        if int(num) not in blocks[4]:
                            blocks[4].add(int(num))
                        else:
                            return False
                    if 5 < row <= 8 and 2 < col <= 5:
                        if int(num) not in blocks[5]:
                            blocks[5].add(int(num))
                        else:
                            return False

                    if row <= 2 and 5 < col <= 8:
                        if int(num) not in blocks[6]:
                            blocks[6].add(int(num))
                        else:
                            return False
                    if 2 < row <= 5 and 5 < col <= 8:
                        if int(num) not in blocks[7]:
                            blocks[7].add(int(num))
                        else:
                            return False
                    if 5 < row <= 8 and 5 < col <= 8:
                        if int(num) not in blocks[8]:
                            blocks[8].add(int(num))
                        else:
                            return False
        print(blocks)
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                else:
                    # Check row
                    check_num = int(board[row][col])
                    check_row = board[row]
                    check_row[col] = "."
                    if str(check_num) in check_row:
                        return False
                    
                    # Check column
                    for i in range(9):
                        irow = board[i]
                        if i == row or irow[col] == ".":
                            continue
                        if check_num == int(irow[col]):
                            return False
        return True