import requests

def get_wenyan():
    url = "https://v1.jinrishici.com/all"
    r = requests.get(url)
    j = r.json()
    try:
        return f'{j["content"]}\n---{j["author"]}'
    except:
        return "未知错误！"