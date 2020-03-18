import aiohttp

async def get_yiyan():
    async with aiohttp.ClientSession() as session:
        async with session.get(url="https://v1.jinrishici.com/all.json") as resp:
            ret = await resp.json()
            try:
                return f"{ret['content']}-{ret['author']}"
            except:
                return "Erroe!"