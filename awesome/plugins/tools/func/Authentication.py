from .CONFIG import CONFIG
import pymysql

HOST = CONFIG["host"]
DATABASH = CONFIG["DataBash"]
USER = CONFIG["user"]
PASSWD = CONFIG["password"]
PORT = CONFIG["port"]
def Authentication_Root(qq):
    s = pymysql.connect(HOST,USER,PASSWD,DATABASH,PORT)
    c = s.cursor()
    c.execute(f"SELECT * FROM user_info WHERE qq={qq}")
    ret = c.fetchone()
    c.close()
    s.close()
    try:
        if ret[5] == 1:
            return True
        else:
            return False
    except TypeError:
        return False
def Authentication_Administrator(qq):
    s = pymysql.connect(HOST,USER,PASSWD,DATABASH,PORT)
    c = s.cursor()
    c.execute(f"SELECT * FROM user_info WHERE qq={qq}")
    ret = c.fetchone()
    c.close()
    s.close()
    try:
        if ret[6] == 1:
            return True
        else:
            return False
    except TypeError:
        return False