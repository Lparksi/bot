import aiohttp
import asyncio
import ssl

async def get_weather_of_city():
    async with aiohttp.ClientSession() as session:
        async with session.get(url="https://v1.jinrishici.com/all.json") as resp:
            ret = await resp.json()
            try:
                print(f"{ret['content']}-{ret['author']}")
                return f"{ret['content']}-{ret['author']}"
            except:
                return "Erroe!"
if __name__ =='__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_weather_of_city())