from awesome.plugins.tools.func.CONFIG import CONFIG
import pymysql

HOST = CONFIG["host"]
DATABASH = CONFIG["DataBash"]
USER = CONFIG["user"]
PASSWD = CONFIG["password"]
PORT = CONFIG["port"]

def Add_root(qq):
    s = pymysql.connect(HOST,USER,PASSWD,DATABASH,PORT)
    c = s.cursor()
    c.execute(f"UPDATE user_info SET root=1 WHERE qq=({qq})")
    s.commit()
    c.close()
    s.close()
def Add_administrator(qq):
    s = pymysql.connect(HOST,USER,PASSWD,DATABASH,PORT)
    c = s.cursor()
    c.execute(f"UPDATE user_info SET administrator=1 WHERE qq=({qq})")
    s.commit()
    c.close()
    s.close()
def Del_root(qq):
    s = pymysql.connect(HOST,USER,PASSWD,DATABASH,PORT)
    c = s.cursor()
    c.execute(f"UPDATE user_info SET root=0 WHERE qq=({qq})")
    s.commit()
    c.close()
    s.close()
def Del_administrator(qq):
    s = pymysql.connect(HOST,USER,PASSWD,DATABASH,PORT)
    c = s.cursor()
    c.execute(f"UPDATE user_info SET administrator=0 WHERE qq=({qq})")
    s.commit()
    c.close()
    s.close()
Del_root(2726043636)