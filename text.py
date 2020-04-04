import requests

url = "http://127.0.0.1:2666/AddData"
data = {
    "token" : "parksi2020",
    "qq" : 123456,
    "nickname" : "Parksi",
    "sex" : "男",
    "age" : 14,
}
r = requests.post(url=url,json=data)
print(r.text)