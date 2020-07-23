import sqlite3

Sql = sqlite3.connect("./databash/sleep.db")
Cursor = Sql.cursor()


def addSleeper(userid, qunid, time):
    Cursor.execute(f"INSERT INTO sleeper (QQID, QUNID, TIME) VALUES ({userid}, {qunid}, {time})")
    Sql.commit()


def delSleeper(userid):
    Cursor.execute(f"DELETE FROM sleeper WHERE QQID={userid}")
    Sql.commit()


def isSleep(userid):
    Cursor.execute(f"SELECT * FROM sleeper WHERE QQID={userid}")
    status = len(Cursor.fetchall())
    if status == 0:
        return False
    else:
        return True


def getSleepTime(userid):
    Cursor.execute(f"SELECT * FROM sleeper WHERE QQID={userid}")
    return Cursor.fetchone()[3]


def selSleepers(qunid):
    Cursor.execute(f"SELECT * FROM sleeper WHERE QUNID={qunid}")
    return len(Cursor.fetchall())


def addGetup(userid, time):
    Cursor.execute(f"INSERT INTO getups (QQID, TIME) VALUES ({userid}, {time})")
    Sql.commit()


def delGetup(userid):
    Cursor.execute(f"DELETE FROM getups WHERE QQID={userid}")
    Sql.commit()


def isGetup(userid):
    Cursor.execute(f"SELECT * FROM getups WHERE QQID={userid}")
    status = len(Cursor.fetchall())
    if status == 0:
        return False
    else:
        return True


def selGetups(qunid):
    Cursor.execute(f"SELECT * FROM  getups")
    return len(Cursor.fetchall())


def getGetUpTime(userid):
    Cursor.execute(f"SELECT * FROM getups WHERE QQID={userid}")
    return Cursor.fetchone()[3]
