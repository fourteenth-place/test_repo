from asyncio.exceptions import TimeoutError
import aiohttp


class Client:
    """
    Async client for making requests
    """
    def __init__(self):
        self.session = None

    async def get_session(self) -> aiohttp.ClientSession:
        if self.session is None:
            self.session = aiohttp.ClientSession()
        return self.session


async def failing_function():
    url = "https://httpstat.us/200?sleep=1"
    client = Client()
    # session = await client.get_session()
    async with await client.get_session() as session:
        try:
            response = await session.post(url, timeout=3)
            print('retreiving data')
            data = await response.text()
            print(data)
        except TimeoutError as e:
            print("TIMEOUT ERROR!")
            raise e
        except Exception as e:
            print("failing_function caught")
            raise e
        
    return data

