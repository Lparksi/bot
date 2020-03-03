import requests
from .get_city_code import get_city_code

def get_weather_of_city(city):
    code = get_city_code(city)
    url = f"http://t.weather.sojson.com/api/weather/city/{code}"
    r = requests.get(url)
    w = weather = r.json()
    w_status = w["status"]
    if w_status == 200:
        w_updatetime = w["cityInfo"]["updateTime"]
        w_req_time = w["time"]

        #未来天气
        w_f = w["data"]["forecast"]

        return f"""
{w["cityInfo"]["parent"]}-{w["cityInfo"]["city"]}的天气情况：
更新时间：{w_updatetime},数据接收时间：{w_req_time}
{w_f[0]["ymd"]}:\n{w_f[0]["high"]},{w_f[0]["low"]}
日出:{w_f[0]["sunrise"]},日落:{w_f[0]["sunset"]}
风向:{w_f[0]["fx"]},风力{w_f[0]["fl"]}
天气状态:{w_f[0]["type"]}
随心笔记:{w_f[0]["notice"]}
{w_f[1]["ymd"]}:\n{w_f[1]["high"]},{w_f[1]["low"]}
日出:{w_f[1]["sunrise"]},日落:{w_f[1]["sunset"]}
风向:{w_f[1]["fx"]},风力{w_f[1]["fl"]}
天气状态:{w_f[1]["type"]}
随心笔记:{w_f[1]["notice"]}
{w_f[2]["ymd"]}:\n{w_f[2]["high"]},{w_f[2]["low"]}
日出:{w_f[2]["sunrise"]},日落:{w_f[2]["sunset"]}
风向:{w_f[2]["fx"]},风力{w_f[2]["fl"]}
天气状态:{w_f[2]["type"]}
随心笔记:{w_f[2]["notice"]}
{w_f[3]["ymd"]}:\n{w_f[3]["high"]},{w_f[3]["low"]}
日出:{w_f[3]["sunrise"]},日落:{w_f[3]["sunset"]}
风向:{w_f[3]["fx"]},风力{w_f[3]["fl"]}
天气状态:{w_f[3]["type"]}
随心笔记:{w_f[3]["notice"]}
{w_f[4]["ymd"]}:\n{w_f[4]["high"]},{w_f[4]["low"]}
日出:{w_f[4]["sunrise"]},日落:{w_f[4]["sunset"]}
风向:{w_f[4]["fx"]},风力{w_f[4]["fl"]}
天气状态:{w_f[4]["type"]}
随心笔记:{w_f[4]["notice"]}
{w_f[5]["ymd"]}:\n{w_f[5]["high"]},{w_f[5]["low"]}
日出:{w_f[5]["sunrise"]},日落:{w_f[5]["sunset"]}
风向:{w_f[5]["fx"]},风力{w_f[5]["fl"]}
天气状态:{w_f[5]["type"]}
随心笔记:{w_f[5]["notice"]}
{w_f[6]["ymd"]}:\n{w_f[6]["high"]},{w_f[6]["low"]}
日出:{w_f[6]["sunrise"]},日落:{w_f[6]["sunset"]}
风向:{w_f[6]["fx"]},风力{w_f[6]["fl"]}
天气状态:{w_f[6]["type"]}
随心笔记:{w_f[6]["notice"]}
{w_f[7]["ymd"]}:\n{w_f[7]["high"]},{w_f[7]["low"]}
日出:{w_f[7]["sunrise"]},日落:{w_f[7]["sunset"]}
风向:{w_f[7]["fx"]},风力{w_f[7]["fl"]}
天气状态:{w_f[7]["type"]}
随心笔记:{w_f[7]["notice"]}
{w_f[8]["ymd"]}:\n{w_f[8]["high"]},{w_f[8]["low"]}
日出:{w_f[8]["sunrise"]},日落:{w_f[8]["sunset"]}
风向:{w_f[8]["fx"]},风力{w_f[8]["fl"]}
天气状态:{w_f[8]["type"]}
随心笔记:{w_f[8]["notice"]}
{w_f[9]["ymd"]}:\n{w_f[9]["high"]},{w_f[9]["low"]}
日出:{w_f[9]["sunrise"]},日落:{w_f[9]["sunset"]}
风向:{w_f[9]["fx"]},风力{w_f[9]["fl"]}
天气状态:{w_f[9]["type"]}
随心笔记:{w_f[9]["notice"]}
{w_f[10]["ymd"]}:\n{w_f[10]["high"]},{w_f[10]["low"]}
日出:{w_f[10]["sunrise"]},日落:{w_f[10]["sunset"]}
风向:{w_f[10]["fx"]},风力{w_f[10]["fl"]}
天气状态:{w_f[10]["type"]}
随心笔记:{w_f[10]["notice"]}
{w_f[11]["ymd"]}:\n{w_f[11]["high"]},{w_f[11]["low"]}
日出:{w_f[11]["sunrise"]},日落:{w_f[11]["sunset"]}
风向:{w_f[11]["fx"]},风力{w_f[11]["fl"]}
天气状态:{w_f[11]["type"]}
随心笔记:{w_f[11]["notice"]}
{w_f[12]["ymd"]}:\n{w_f[12]["high"]},{w_f[12]["low"]}
日出:{w_f[12]["sunrise"]},日落:{w_f[12]["sunset"]}
风向:{w_f[12]["fx"]},风力{w_f[12]["fl"]}
天气状态:{w_f[12]["type"]}
随心笔记:{w_f[12]["notice"]}
{w_f[13]["ymd"]}:\n{w_f[13]["high"]},{w_f[13]["low"]}
日出:{w_f[13]["sunrise"]},日落:{w_f[13]["sunset"]}
风向:{w_f[13]["fx"]},风力{w_f[13]["fl"]}
天气状态:{w_f[13]["type"]}
随心笔记:{w_f[13]["notice"]}
{w_f[14]["ymd"]}:\n{w_f[14]["high"]},{w_f[14]["low"]}
日出:{w_f[14]["sunrise"]},日落:{w_f[14]["sunset"]}
风向:{w_f[14]["fx"]},风力{w_f[14]["fl"]}
天气状态:{w_f[14]["type"]}
随心笔记:{w_f[14]["notice"]}
        """

    else:
        return "获取失败！"

