import asyncio

def timeLimit(fn, t):
    async def limited_fn(*args):
        try:
            result = await asyncio.wait_for(fn(*args), timeout=t / 1000)
            return result
        except asyncio.TimeoutError:
            raise "Time Limit Exceeded"
    return limited_fn