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
    client = Client()
    session = await client.get_session()
    url = "https://httpstat.us/200?sleep=5000"
    try:
        async with session.post(url, timeout=0.01) as response:
            try:
                print('retreiving data')
                data = await response.text
            except Exception as e:
                print("failing_function caught")
                raise e
    except Exception as e:
        print("failing_function outer caught")
        raise e
        
    return data