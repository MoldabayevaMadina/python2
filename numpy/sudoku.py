import numpy as np
class Sudoku:
    def __init__(self, s):
        self.s = s
    def board(self):
        list1 = []
        for i in range(9):
            l = [self.s[j] for j in range(9 * i, 9 * i + 9)]
            list1.append(l)
        self.arr = np.asarray(list1)
        return self.arr
    def get_row(self, n):
        return self.arr[n]
    def get_col(self, m):
        return self.arr.T[m]
    def get_sqr(self, n, m):
        n //= 3
        m //= 3
        l1 = []
        l2 = []
        for i in range(n * 3 , n * 3 + 3):
            for j in range(m * 3 , m * 3 + 3):
                l2.append(self.arr[i, j])
            self.arr1 = np.asarray(l2)
        return self.arr1
game = Sudoku("417950030000000700060007000050009106800600000000003400900005000000430000200701580")
game1 = Sudoku("667051100086000790060007000050009106800607000500003400900005000000430000200701580")
board = game.board()
board1 = game1.board()
print(board1)
#print(game.get_col(0))
print(game.get_row(5))
print(game1.get_row(0))
#print(game.get_sqr(8, 3))

