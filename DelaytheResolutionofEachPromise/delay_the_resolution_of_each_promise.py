import asyncio

async def delayed_resolution(value, delay):
    """
    Simulates a promise that resolves after a specified delay.
    """
    print(f"Promise for '{value}' starting, will resolve in {delay} seconds...")
    await asyncio.sleep(delay)
    print(f"Promise for '{value}' resolved after {delay} seconds.")
    return value

async def main():
    """
    Creates and waits for multiple delayed promises.
    """
    promise_specs = [
        ("Task A", 2),
        ("Task B", 1),
        ("Task C", 3),
        ("Task D", 1.5)
    ]

    promises = [delayed_resolution(value, delay) for value, delay in promise_specs]

    print("--- Starting to wait for all promises ---")
    results = await asyncio.gather(*promises)
    print("--- All promises resolved ---")

    print("\nFinal Results:")
    for result in results:
        print(f"- {result}")

if __name__ == "__main__":
    asyncio.run(main())