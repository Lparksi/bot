from flask import Flask, request
from SQL.func.AddData import Add_Data
from SQL.func.DelData import Del
from SQL.func.Updata_Data import Updata_Data
from SQL.func.Authentication import Authentication_Root, Authentication_Administrator
from SQL.func.Select import Select
import json
app = Flask(__name__)

@app.route('/Authentication',methods=["POST"])
def authentication():
    dit = json.loads(request.get_data())
    if dit["token"] == 'parksi2020':
        if dit["type"] == "Root":
            data = {
                "code" : 200,
                "authority" : Authentication_Root(request["qq"])
            }
            return data,200
        elif dit["type"] == "Administrator":
            data = {
                "code" : 200,
                "authority" : Authentication_Administrator(request["qq"])
            }
            return data,200
        else:
            return "ERROR", 200
    else:
        return "Toker Error!", 0

@app.route('/AddData',methods=["POST"])
def addData():
    dit = json.loads(request.get_data())
    if dit["token"] == "parksi2020":
        qq = dit["qq"]
        nickname = dit["nickname"]
        sex = dit["sex"]
        age = dit["age"]
        Add_Data(qq=qq, nickname=nickname, sex=sex, age=age)
        return "ok", 200
    else:
        return "Token Error", 0

@app.route('/DelData',methods=["POST"])
def delData():
    dit = json.loads(request.get_data())
    if dit["token"] == "parksi2020":
        Del(dit["qq"])
        return "ok", 200
    else:
        return "Token Error", 0

@app.route('/Updata_Data',methods=["POST"])
def updata_Data():
    dit = json.loads(request.get_data())
    if dit["token"] == "parksi2020":
        qq = dit["qq"]
        nickname = dit["nickname"]
        sex = dit["sex"]
        age = dit["age"]
        Updata_Data(qq=qq,nickname=nickname,sex=sex,age=age)
        return "ok", 200
    else:
        return "Token Error", 0

@app.route("/select",methods=["POST"])
def select():
    dit = json.loads(request.get_data())
    if dit["token"] == "parksi2020":
        data = Select(qq=dit["qq"])
        ret = {
            "id": data[0],
            "qq": data[1],
            "nickname": data[2],
            "sex": data[3],
            "age": data[4],
            'root': data[5],
            "administrator" : data[6]
                }
        return ret, 200
    else:
        return "Token Error", 0
app.run(port=2666)