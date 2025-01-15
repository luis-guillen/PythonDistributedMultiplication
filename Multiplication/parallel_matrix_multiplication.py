from concurrent.futures import ThreadPoolExecutor

class ParallelMatrixMultiplication:
    @staticmethod
    def multiply_matrices_parallel(matrixA, matrixB):
        """
        Performs matrix multiplication in parallel by calculating each row in a separate thread.

        Args:
            matrixA (list[list[int]]): The first matrix.
            matrixB (list[list[int]]): The second matrix.

        Returns:
            list[list[int]]: The result of the matrix multiplication.
        """
        rowsA = len(matrixA)
        colsB = len(matrixB[0])

        def calculate_row(row):
            return [sum(matrixA[row][k] * matrixB[k][col] for k in range(len(matrixB))) for col in range(colsB)]

        result = [None] * rowsA

        with ThreadPoolExecutor() as executor:
            futures = {executor.submit(calculate_row, row): row for row in range(rowsA)}
            for future in futures:
                row_index = futures[future]
                result[row_index] = future.result()

        return result