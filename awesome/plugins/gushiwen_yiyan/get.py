
#def get_wenyan():
#   url = "https://v1.jinrishici.com/all"
#    r = requests.get(url,timeout=1)
#    j = r.json()
#    try:
#        return f'{j["content"]}\n---{j["author"]}'
#    except Timeout:
#        return "API请求超时！"
#    except:
#        return "未知错误！"

import aiohttp
async def get_wenyan():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://v1.jinrishici.com/all") as resp:
            j = await resp.json()
            return f'{j["content"]}\n---{j["author"]}'