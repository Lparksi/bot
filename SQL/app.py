from flask import Flask, request
from SQL.func.AddData import Add_Data
from SQL.func.DelData import Del
from SQL.func.Updata_Data import Updata_Data
from SQL.func.Authentication import Authentication_Root, Authentication_Administrator
app = Flask(__name__)

@app.route('/',methods=["POST"])
def authentication():
    if request["token"] == 'parksi2020':
        if request["type"] == "Root":
            data = {
                "code" : 200,
                "authority" : Authentication_Root(request["qq"])
            }
            return data,200
        elif request["type"] == "Administrator":
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
    if request["token"] == "parksi2020":
        qq = request["qq"]
        nickname = request["nickname"]
        sex = request["sex"]
        age = request["age"]
        Add_Data(qq=qq, nickname=nickname, sex=sex, age=age)
        return "ok", 200
    else:
        return "Token Error", 0

@app.route('/DelData',methods=["POST"])
def delData():
    if request["token"] == "parksi2020":
        Del(request["qq"])
        return "ok", 200
    else:
        return "Token Error", 0

@app.route('/Updata_Data',methods=["POST"])
def updata_Data():
    if request["token"] == "parksi2020":
        qq = request["qq"]
        nickname = request["nickname"]
        sex = request["sex"]
        age = request["age"]
        Updata_Data(qq=qq,nickname=nickname,sex=sex,age=age)
        return "ok", 200
    else:
        return "Token Error", 0

app.run(port=2666)