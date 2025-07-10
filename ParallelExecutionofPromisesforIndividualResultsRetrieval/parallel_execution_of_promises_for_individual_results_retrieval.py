import concurrent.futures
import time
import random

def perform_task(task_id):
    """Simulates an asynchronous task with variable delay."""
    delay = random.uniform(0.5, 2.0)
    print(f"Task {task_id}: Starting (delay {delay:.2f}s)")
    time.sleep(delay)
    result = f"Task {task_id} completed with delay {delay:.2f}s"
    print(f"Task {task_id}: Finished")
    return result

if __name__ == "__main__":
    task_inputs = list(range(1, 7))

    task_futures = {}

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        print("Submitting tasks...")
        for task_id in task_inputs:
            future = executor.submit(perform_task, task_id)
            task_futures[task_id] = future

        print("All tasks submitted. Retrieving results individually...")
        for task_id in task_inputs:
            future = task_futures[task_id]
            try:
                result = future.result()
                print(f"Retrieved result for {task_id}: {result}")
            except Exception as e:
                print(f"Task {task_id} encountered an error: {e}")

    print("All individual results retrieved.")