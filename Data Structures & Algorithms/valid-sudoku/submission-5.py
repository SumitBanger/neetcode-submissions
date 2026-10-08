class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for row in range(9):
            for col in range(9):
                element = board[row][col]
                if element != ".":
                    if element in rows[row] or element in cols[col] or element in squares[(row//3,col//3)]:
                        return False
                    rows[row].add(element)
                    cols[col].add(element)
                    squares[(row//3,col//3)].add(element)

        return True
        