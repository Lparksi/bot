import requests

def get_yiyan():
    url = "https://international.v1.hitokoto.cn"
    payload = {
        "c" : "d"
    }
    r =requests.get(url,params=payload)
    y_dict = r.json()
    try:
        return f'{y_dict["hitokoto"]} --{y_dict["from"]}'
    except:
        return "API返回失败,错误未知."