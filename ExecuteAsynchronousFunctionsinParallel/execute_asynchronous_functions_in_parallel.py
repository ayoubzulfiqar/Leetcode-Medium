```python
import asyncio

async def promiseAll(functions):
    n = len(functions)
    
    # If the input array is empty, resolve immediately with an empty list.
    if n == 0:
        return []

    # This future will represent the overall result of promiseAll.
    # It will be resolved with the array of results or rejected with the first error.
    main_future = asyncio.Future()

    # This array will store the results in the correct order.
    # Initialize with None placeholders.
    results = [None] * n
    
    # Counter for successfully completed tasks.
    completed_count = 0

    # Callback function to be executed when each individual task completes.
    def _task_done_callback(task, index):
        nonlocal completed_count

        # If the main_future has already been resolved or rejected,
        # subsequent task completions (success or failure) should not affect it.
        if main_future.done():
            return

        try:
            # Get the result of the task. This will re-raise any exception
            # that occurred in the task.
            result = task.result()
            
            # Store the successful result in the correct order.
            results[index] = result
            completed_count += 1

            # If all tasks have completed successfully, resolve the main_future
            # with the collected results.
            if completed_count == n:
                main_future.set_result(results)
        except Exception as e:
            # If any task fails, reject the main_future with its exception.
            # Because `set_exception` can only be called once on a Future,
            # this naturally handles the "first rejection" requirement.
            main_future.set_exception(e)

    # Create and start all individual tasks.
    # Each task will run the corresponding function and return its promise/awaitable.
    tasks = []
    for i, func in enumerate(functions):
        # asyncio.create_task schedules the coroutine to run in the event loop.
        # It returns a Task object, which is a Future-like object.
        task = asyncio.create_task(func())
        
        # Attach the callback to be executed when this task finishes (success or failure).
        # We use a lambda to capture the `index` for the callback.
        task.add_done_callback(lambda t, idx=i: _task_done_callback(t, idx))
        tasks.append(task)

    # Await the main_future. This will pause the `promiseAll` coroutine
    # until `main_future` is resolved with a result or rejected with an exception
    # by one of the `_task_done_callback` calls.
    return await main_future
```