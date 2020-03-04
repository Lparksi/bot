import requests

def short_url(long_url):
    api_url = "http://shorturl.8446666.sojson.com/sina/shorturl"
    patload = {"url":long_url}
    r = requests.get(api_url,params=patload)
    j = r.json()
    if j["status"] == 200:
        return j["shorturl"]
    else:
        return f"{long_url},\n短链接错误:{j['message']}"