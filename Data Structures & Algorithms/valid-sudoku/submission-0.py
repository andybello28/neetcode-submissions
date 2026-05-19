class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = {}
        # Each one represents a different 3x3 grid
        #i is current row
        for i in range(9):
            row = set()
            if i % 3 == 0:
                grid = {1: set(), 2: set(), 3: set()}
            #j is current column
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if j < 3:
                    grid_counter = 1
                elif j < 6:
                    grid_counter = 2
                elif j < 9:
                    grid_counter = 3
                if board[i][j] not in grid[grid_counter]:
                    grid[grid_counter].add(board[i][j])
                else:
                    return False


                if j not in columns:
                    columns[j] = set()
                if board[i][j] not in columns[j]:
                    columns[j].add(board[i][j])
                else:
                    return False


                if board[i][j] not in row:
                    row.add(board[i][j])
                else:
                    return False
            row = set()
        return True