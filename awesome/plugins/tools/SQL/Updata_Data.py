import json
import pymysql

CONFIG = json.loads(open(".config.json").read())
HOST = CONFIG["host"]
DATABASH = CONFIG["DataBash"]
USER = CONFIG["user"]
PASSWD = CONFIG["password"]
PORT = CONFIG["port"]

def Updata_Data(qq,nickname,sex,age,root,administrator):
    s = pymysql.connect(HOST,USER,PASSWD,DATABASH,PORT)
    c = s.cursor()
    try:
        c.execute(f"UPDATE user_info SET nickname='{nickname}',sex='{sex}',age={age},root={root},administrator={administrator} WHERE qq={qq}")
        s.connect()
    except ImportError:
        s.rollback()
        c.close()
        s.close()
Updata_Data(123456,"Parksi",str("parksi"),14,1,1)