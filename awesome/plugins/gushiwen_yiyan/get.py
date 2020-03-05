import requests

def get_wenyan():
    url = "https://v1.jinrishici.com/all"
    r = requests.get(url,timeout=1)
    j = r.json()
    try:
        return f'{j["content"]}\n---{j["author"]}'
    except Timeout:
        return "API请求超时！"
    except:
        return "未知错误！"