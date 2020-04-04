from .CONFIG import CONFIG
import pymysql

HOST = CONFIG["host"]
DATABASH = CONFIG["DataBash"]
USER = CONFIG["user"]
PASSWD = CONFIG["password"]
PORT = CONFIG["port"]

def Add_Data(qq,nickname=0,sex=0,age=1,root=0,administrator=0):
    s = pymysql.connect(HOST,USER,PASSWD,DATABASH,PORT)
    c = s.cursor()
    try:
        c.execute(f"""INSERT INTO user_info (qq,nickname,sex,age,root,administrator) VALUES ({qq},'{nickname}','{sex}',{age},{root},{administrator})""")
        s.commit()
    except KeyError:
        s.rollback()
    c.close()
    s.close()