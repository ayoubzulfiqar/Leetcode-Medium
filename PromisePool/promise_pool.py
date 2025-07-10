import concurrent.futures
import time

class PromisePool:
    """
    A pool for executing tasks concurrently, returning a Future (promise) for each task.
    """
    def __init__(self, max_workers: int):
        """
        Initializes the PromisePool with a specified number of worker threads.

        Args:
            max_workers: The maximum number of threads that can be used to execute tasks.
        """
        if not isinstance(max_workers, int) or max_workers <= 0:
            raise ValueError("max_workers must be a positive integer")
        self._executor = concurrent.futures.ThreadPoolExecutor(max_workers=max_workers)

    def submit(self, fn, *args, **kwargs) -> concurrent.futures.Future:
        """
        Submits a callable to the pool for execution and returns a Future object.

        The Future object represents the eventual result of the callable's execution.
        You can use .result() to get the result (which blocks until available),
        or .done() to check if it's finished.

        Args:
            fn: The function to be executed.
            *args: Positional arguments to pass to the function.
            **kwargs: Keyword arguments to pass to the function.

        Returns:
            A concurrent.futures.Future object representing the promise of the task's result.
        """
        return self._executor.submit(fn, *args, **kwargs)

    def shutdown(self, wait: bool = True):
        """
        Shuts down the pool, freeing up resources.

        Args:
            wait: If True, blocks until all submitted futures are done.
                  If False, immediately returns and shuts down the pool.
        """
        self._executor.shutdown(wait=wait)

def _example_task(task_id: str, duration_seconds: float) -> str:
    """
    A sample task function to demonstrate PromisePool usage.
    Simulates work by sleeping for a given duration.
    """
    print(f"Task {task_id}: Starting (duration={duration_seconds}s)...")
    time.sleep(duration_seconds)
    result = f"Task {task_id} completed successfully after {duration_seconds} seconds."
    print(f"Task {task_id}: Finished.")
    return result

if __name__ == "__main__":
    pool = PromisePool(max_workers=3)

    promises = []
    promises.append(pool.submit(_example_task, "A", 2.0))
    promises.append(pool.submit(_example_task, "B", 1.0))
    promises.append(pool.submit(_example_task, "C", 3.0))
    promises.append(pool.submit(_example_task, "D", 0.5))
    promises.append(pool.submit(_example_task, "E", 2.5))

    for i, promise in enumerate(promises):
        try:
            result = promise.result()
            print(f"Result of Promise {chr(65+i)}: {result}")
        except Exception as e:
            print(f"Promise {chr(65+i)} raised an exception: {e}")

    new_promises = []
    new_promises.append(pool.submit(_example_task, "F", 1.5))
    new_promises.append(pool.submit(_example_task, "G", 0.8))

    for future in concurrent.futures.as_completed(new_promises):
        try:
            result = future.result()
            print(f"As completed result: {result}")
        except Exception as e:
            print(f"As completed promise raised an exception: {e}")

    pool.shutdown(wait=True)