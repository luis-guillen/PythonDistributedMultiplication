import random

class MatrixMultiplication:
    @staticmethod
    def generate_matrix(rows, cols, min_val, max_val):
        """
        Generates a matrix with random values within a specified range.

        Args:
            rows (int): Number of rows in the matrix.
            cols (int): Number of columns in the matrix.
            min_val (int): Minimum value for random numbers.
            max_val (int): Maximum value for random numbers.

        Returns:
            list[list[int]]: Generated matrix with random values.
        """
        return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

    @staticmethod
    def basic_matrix_multiplication(A, B):
        """
        Performs basic matrix multiplication of two matrices A and B.

        Args:
            A (list[list[int]]): First matrix.
            B (list[list[int]]): Second matrix.

        Returns:
            list[list[int]]: Resultant matrix after multiplication.
        """
        rows = len(A)
        cols = len(B[0])
        C = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                for k in range(len(A[0])):
                    C[i][j] += A[i][k] * B[k][j]

        return C