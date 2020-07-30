import sqlite3
import time

Sql = sqlite3.connect('../status.db')
Cursor = Sql.cursor()


def inList(roomid):
    Cursor.execute(f"SELECT * FROM status WHERE ROOMID={roomid}")
    ret = Cursor.fetchall()
    if len(ret) == 0:
        return False
    else:
        return True


def addRoom(roomid, status, time=time.time()):
    Cursor.execute(f"INSERT INTO status (ROOMID, STATUS, TIME) VALUES ({roomid}, {status}, {time})")
    Sql.commit()


def upRoom(roomid, time, status):
    Cursor.execute(f"UPDATE status SET (TIME={time}, STATUS={status}) WHERE ROOMID={roomid}")
    Sql.commit()


def selStatus(roomid):
    Cursor.execute(f"SELECT * FROM status WHERE ROOMID={roomid}")
    ret = Cursor.fetchone()
    return ret[2]


def selTime(roomid):
    Cursor.execute(f"SELECT * FROM status WHERE ROOMID={roomid}")
    ret = Cursor.fetchone()
    return ret[3]