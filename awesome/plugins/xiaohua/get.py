import requests

def get_xiaohau():
    url = " http://route.showapi.com/341-5"
    patload = {
        "showapi_appid":"153532",
        "showapi_sign":"a1202046add84686802a578b9b003a33"
    }
    r = requests.get(url,params=patload)
    xh_dict = r.json()
    if xh_dict["showapi_res_code"] == 0:
        xh_dic = xh_dict["showapi_res_body"]
        if xh_dic["ret_code"] == 0:
            return f'{xh_dic["list"][0]["text"]}'
        else:
            return "API调用错误"
    else:
        return "API认证错误"