from concurrent.futures import ThreadPoolExecutor
import atexit

class HazelcastManager:
    """
    Manages a thread pool to simulate Hazelcast functionality in Python.
    Provides a simple interface for initializing, accessing, and shutting down the executor service.
    """

    _executor = None

    @staticmethod
    def initialize(max_workers=None):
        """
        Initializes the thread pool executor.
        Args:
            max_workers (int): The maximum number of threads in the pool.
                               If None, it defaults to the number of processors.
        """
        if HazelcastManager._executor is None:
            HazelcastManager._executor = ThreadPoolExecutor(max_workers=max_workers)
            atexit.register(HazelcastManager.shutdown)

    @staticmethod
    def get_executor_service():
        """
        Returns the thread pool executor.

        Returns:
            ThreadPoolExecutor: The initialized thread pool executor.
        """
        if HazelcastManager._executor is None:
            raise RuntimeError("HazelcastManager is not initialized.")
        return HazelcastManager._executor

    @staticmethod
    def shutdown():
        """
        Shuts down the thread pool executor gracefully.
        """
        if HazelcastManager._executor:
            HazelcastManager._executor.shutdown(wait=True)
            HazelcastManager._executor = None