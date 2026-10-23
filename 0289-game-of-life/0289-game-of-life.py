class Solution:
    def abc(self, n: int, m: int, x: List[List[int]], i: int, j: int) -> int:
        if i < 0 or i >= n or j < 0 or j >= m:
            return 0
        return x[i][j]

    def gameOfLife(self, board: List[List[int]]) -> None:
        n = len(board)
        m = len(board[0])

        x = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                x[i][j] = board[i][j]
        for i in range(n):
            for j in range(m):
                z = 0
                for k1 in range(i - 1, i + 2):
                    for k2 in range(j - 1, j + 2):
                        if not (k1 == i and k2 == j):
                            z += self.abc(n, m, x, k1, k2)
                if x[i][j] == 1 and (z < 2 or z > 3):
                    board[i][j] = 0
                elif x[i][j] == 0 and z == 3:
                    board[i][j] = 1