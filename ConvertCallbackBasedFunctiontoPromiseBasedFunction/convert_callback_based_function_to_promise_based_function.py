import asyncio
import functools

def callback_based_operation(data, success_callback, error_callback):
    """
    Simulates an asynchronous operation that uses callbacks.
    This function itself returns immediately. It schedules the
    execution of success_callback or error_callback after a delay
    using asyncio's event loop directly, mimicking a non-blocking I/O operation.
    """
    loop = asyncio.get_running_loop()

    def _complete_operation():
        if data == "success":
            success_callback(f"Operation completed successfully for '{data}'")
        else:
            error_callback(f"Operation failed for '{data}'")

    # Schedule the completion of the operation after a delay
    loop.call_later(0.1, _complete_operation)

def convert_callback_to_promise(callback_func, *args, **kwargs):
    """
    Converts a callback-based function into an async function that returns an asyncio.Future (promise-like).

    Args:
        callback_func: The original callback-based function. It must accept
                       (..., success_callback, error_callback) as its last arguments,
                       or as keyword arguments 'success_callback' and 'error_callback'.
        *args: Positional arguments to pass to the original callback_func.
        **kwargs: Keyword arguments to pass to the original callback_func.

    Returns:
        An awaitable asyncio.Future that will be resolved with the success result
        or rejected with an exception if the error callback is invoked.
    """
    loop = asyncio.get_running_loop()
    future = loop.create_future()

    def success_callback(result):
        if not future.done():
            loop.call_soon_threadsafe(future.set_result, result)

    def error_callback(error):
        if not future.done():
            loop.call_soon_threadsafe(future.set_exception, Exception(error))

    # Call the original callback-based function, passing our internal callbacks.
    # The original function is expected to return immediately and handle its
    # async nature internally (e.g., by scheduling tasks or using threads).
    callback_func(*args, success_callback=success_callback, error_callback=error_callback, **kwargs)

    return future

async def main():
    print("--- Testing Success Case ---")
    try:
        # Convert the callback-based operation for 'success' data
        # 'data' is passed as a positional argument here
        promise_for_success = convert_callback_to_promise(callback_based_operation, "success")
        result = await promise_for_success
        print(f"Promise resolved with: {result}")
    except Exception as e:
        print(f"Promise rejected with: {e}")

    print("\n--- Testing Failure Case ---")
    try:
        # Convert the callback-based operation for 'failure' data
        promise_for_failure = convert_callback_to_promise(callback_based_operation, "failure")
        result = await promise_for_failure
        print(f"Promise resolved with: {result}")
    except Exception as e:
        print(f"Promise rejected with: {e}")

    print("\n--- Testing Another Success Case (passing 'data' as keyword arg) ---")
    try:
        # Demonstrate passing 'data' as a keyword argument
        promise_for_another_success = convert_callback_to_promise(callback_based_operation, data="another_success_kwarg")
        result = await promise_for_another_success
        print(f"Promise resolved with: {result}")
    except Exception as e:
        print(f"Promise rejected with: {e}")

if __name__ == "__main__":
    asyncio.run(main())