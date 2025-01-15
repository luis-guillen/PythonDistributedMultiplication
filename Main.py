import os
import psutil
import time
from multiprocessing import cpu_count


from Multiplication.matrix_multiplication import MatrixMultiplication
from Multiplication.distributed_matrix_multiplication import distributed_matrix_multiplication
from Multiplication.parallel_matrix_multiplication import ParallelMatrixMultiplication
from ResultsWriter.results_writer_utiliity import ResultsWriterUtility


class ExecutionType:
    SEQUENTIAL = "SEQUENTIAL"
    PARALLEL = "PARALLEL"
    DISTRIBUTED = "DISTRIBUTED"


from concurrent.futures import ThreadPoolExecutor

def main():
    matrix_sizes = [64, 128, 256, 512, 1024, 2048, 4096]
    result_headers = ["Size", "Execution Time (ms)", "Memory Usage (MB)", "CPU (%)", "Nodes", "Network Latency (ms)", "Transfer Time (ms)"]

    def benchmark(size):
        matrix_a = MatrixMultiplication.generate_matrix(size, size, 1, 9)
        matrix_b = MatrixMultiplication.generate_matrix(size, size, 1, 9)

        execute_benchmark("sequential_results.txt", result_headers, size, ExecutionType.SEQUENTIAL, matrix_a, matrix_b)
        execute_benchmark("parallel_results.txt", result_headers, size, ExecutionType.PARALLEL, matrix_a, matrix_b)
        execute_benchmark("distributed_results.txt", result_headers, size, ExecutionType.DISTRIBUTED, matrix_a, matrix_b)

    with ThreadPoolExecutor() as executor:
        executor.map(benchmark, matrix_sizes)

def execute_benchmark(output_file, headers, size, exec_type, matrix_a, matrix_b):
    # Collect initial memory and CPU stats
    process = psutil.Process(os.getpid())
    memory_before = process.memory_info().rss
    start_time = time.time()

    result = None
    cpu_usage = 0
    execution_time = 0
    memory_usage = 0

    if exec_type == ExecutionType.SEQUENTIAL:
        result = MatrixMultiplication.basic_matrix_multiplication(matrix_a, matrix_b)
    elif exec_type == ExecutionType.PARALLEL:
        result = ParallelMatrixMultiplication.multiply_matrices_parallel(matrix_a, matrix_b)
    elif exec_type == ExecutionType.DISTRIBUTED:
        start_transfer_time = time.time()
        nodes = cpu_count()  # Simulating nodes as number of CPUs
        transfer_time = (time.time() - start_transfer_time) * 1000  # Simulated latency in ms

        result = distributed_matrix_multiplication(matrix_a, matrix_b)

        execution_time = (time.time() - start_time) * 1000
        memory_usage = process.memory_info().rss - memory_before
        cpu_usage = process.cpu_percent(interval=1)

        ResultsWriterUtility.write_to_text(output_file, headers, [
            str(size),
            str(execution_time),
            f"{memory_usage / (1024 * 1024):.2f}",
            f"{cpu_usage:.2f}",
            str(nodes),
            f"{transfer_time:.2f}",
            f"{transfer_time:.2f}"
        ])
        return

    # Measure execution time and memory usage
    execution_time = (time.time() - start_time) * 1000
    memory_usage = process.memory_info().rss - memory_before
    cpu_usage = process.cpu_percent(interval=1)

    ResultsWriterUtility.write_to_text(output_file, headers, [
        str(size),
        str(execution_time),
        f"{memory_usage / (1024 * 1024):.2f}",
        f"{cpu_usage:.2f}",
        "N/A",
        "N/A",
        "N/A"
    ])


if __name__ == "__main__":
    main()