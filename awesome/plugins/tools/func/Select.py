from .CONFIG import CONFIG
import pymysql

HOST = CONFIG["host"]
DATABASH = CONFIG["DataBash"]
USER = CONFIG["user"]
PASSWD = CONFIG["password"]
PORT = CONFIG["port"]

def Select(qq):
    s = pymysql.connect(HOST,USER,PASSWD,DATABASH,PORT)
    c = s.cursor()
    c.execute(f"SELECT * FROM user_info WHERE qq={qq}")
    data = c.fetchone()
    c.close()
    s.close()
    return data