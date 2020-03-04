import requests


def get_yiqing_of_city(city):
    url = "https://myapi.ihogu.com/public/?s=Whfy.city"
    payload = {
        'city': city
    }
    r = requests.get(url, params=payload)
    ret = r.json()
    code = ret['ret']
    if code == 200:
        try:
            date = ret['data']['items'][0]
            return f"""{date["create_time"],}{date["city"]}的疫情详情：
确诊：{date["confirm"]}
疑似：{date["suspect"]}
死亡：{date["dead"]}
治愈：{date["heal"]}"""
        except:
            return 'API调用失败，疑似用户输入错误'
    else:
        return 'API调用返回失败'
