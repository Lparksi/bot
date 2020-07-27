import sqlite3

Sql = sqlite3.connect("./databash/sleep.db")
Cursor = Sql.cursor()


# 查询用户uid
def selUid(userid):
    Cursor.execute(f"SELECT * FROM sleeplog WHERE QQID={userid}")
    data = Cursor.fetchone()
    return data[0]


# 检查用户是否已拥有uid
def isUeer(userid):
    Cursor.execute(f"SELECT * FROM sleeplog WHERE QQID={userid}")
    data = Cursor.fetchall()
    if len(data) == 0:
        return False
    else:
        return True


# 查询不完整的记录
def selSleepLogUncomplete(userid):
    Cursor.execute(f"SELECT * FROM sleeplog WHERE QQID={userid}")
    data = Cursor.fetchall()
    for item in data:
        if data[item][4] == 0:
            return data[item][1]


# 添加记录 睡眠
def addSleepLogSleep(userid, time, data):
    if isUeer(userid=userid):
        uid = selUid(userid)
        Cursor.execute(
            f"INSERT INTO sleeplog (UID, QQID, SLEEPTIME, SLEEPDATA) VALUES ({userid}, {userid}, {time}, '{data})'")
        Sql.commit()
    else:
        Cursor.execute(
            f"INSERT INTO sleeplog (QQID, SLEEPTIME, SLEEPDATA) VALUES ({userid}, {time}, '{data})'")
        Sql.commit()


# 添加记录 起床
def addSleepLogGetup(userid, time, data):
    logid = selSleepLogUncomplete(userid)
    Cursor.execute(f"UPDATE sleeplog SET GETUPDATA={data}, GETUPTIME='{time}'")
    Sql.commit()


# 查询用户所有记录 -> dict
def selUserLogAll(userid):
    Cursor.execute(f"SELECT * FROM sleeplog WHERE QQID={userid}")
    data = Cursor.fetchall()
    return data


# 查询用户睡眠记录 -> str
def selUserLogs(userid) -> str:
    data = selUserLogAll(userid=userid)
    msg = f"[CQ:at,qq={userid}]\n你的睡眠记录如下:\n"
    msg += f"你的用户id：{data[0][0]}\n"
    for item in data:
        msg += f"logid：{data[item][1]},{data[item][5]}\n"
        msg += f"{data[item][4]}到{data[item][6]}\n"
    return msg