class MatrixMultiplicationTask:
    """
    A callable task that performs matrix multiplication for a specific range of rows.

    Args:
        A (list[list[int]]): The first matrix.
        B (list[list[int]]): The second matrix.
        start_row (int): The starting row for the multiplication.
        end_row (int): The ending row for the multiplication.
    """

    def __init__(self, A, B, start_row, end_row):
        self.A = A
        self.B = B
        self.start_row = start_row
        self.end_row = end_row

    def __call__(self):
        """
        Executes the task to compute a subset of the matrix multiplication.

        Returns:
            list[list[int]]: The resulting subset of the multiplication.
        """
        rows_A = self.end_row - self.start_row
        cols_B = len(self.B[0])
        result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(len(self.B)):
                    result[i][j] += self.A[self.start_row + i][k] * self.B[k][j]

        return result