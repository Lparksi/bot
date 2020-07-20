import sqlite3
from time import time

Sql = sqlite3.connect("./databash/roll.db")
MainCursor = Sql.cursor()
LogCursor = Sql.cursor()


def addrolllog(userid, qunid, roll , time=time()):
    LogCursor.execute(f"INSERT INTO rolllog (QQID, QUNID, ROLL, TIME) VALUES ({userid}, {qunid}, {roll}, {time})")
    Sql.commit()


def isEmpty(userid):
    MainCursor.execute(f"SELECT * FROM roll WHERE QQID={userid}")
    data = len(MainCursor.fetchall())
    if data == 0:
        return True
    else:
        return False


def newUser(userid, qunid):
    MainCursor.execute(f"INSERT INTO roll (QQID, QUNID, ROLL) VALUES ({userid}, {qunid}, 0)")
    Sql.commit()


def updata(userid, roll):
    allroll = roll + selRoll(userid)
    MainCursor.execute(f'UPDATE roll SET ROLL={allroll} WHERE QQID={userid}')
    Sql.commit()


def selRoll(userid):
    MainCursor.execute(f"SELECT * FROM roll WHERE QQID={userid}")
    data = MainCursor.fetchone()[3]
    return int(data)


def selTime(userid):
    LogCursor.execute(f"SELECT * FROM rolllog WHERE QQID={userid}")
    data = MainCursor.fetchall()
    TIMES = []
    for item in data:
        TIMES.append(item[4])
    return max(TIMES)