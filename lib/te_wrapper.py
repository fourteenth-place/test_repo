import asyncio

from te_fail import failing_function


async def new_function():
    try:
        await failing_function()
    except asyncio.exceptions.TimeoutError:
        print('TimeoutError caught')
    except Exception as e:
        print("new_function caught")
        raise e

asyncio.run(new_function())
asyncio.run(new_function())
asyncio.run(new_function())