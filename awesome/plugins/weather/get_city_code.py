import json
from .weather import city_code

jsonbj = json.loads(city_code())
def get_city_code(city):
    count = True
    di = 0
    while(count):
        if jsonbj[di]["city_name"] == city:
            return jsonbj[di]["city_code"]
            break
        elif di >= 10000:
            return 0
        else:
            #print(f"第{di}次未命中")
            di+=1