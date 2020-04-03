import json
import pymysql

CONFIG = json.loads(open("config.json").read())
HOST = CONFIG["host"]
DATABASH = CONFIG["DataBash"]
USER = CONFIG["user"]
PASSWD = CONFIG["password"]
PORT = CONFIG["port"]

def Del(qq):
    s = pymysql.connect(HOST,USER,PASSWD,DATABASH,PORT)
    c = s.cursor()
    try:
        c.execute(f"DELETE FROM user_info WHERE qq={qq}")
        s.commit()
    except:
        s.rollback()
    c.close()
    s.close()