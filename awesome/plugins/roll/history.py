import sqlite3

Sql = sqlite3.connect("./databash/roll.db")
LogCursor = Sql.cursor()

def getHistory(qunid, rows=10):
    LogCursor.execute(f"SELECT * FROM rolllog WHERE QUNID={qunid}")
    data = LogCursor.fetchall()
    ITEMS = 0
    bashmsg = f"以下是本群roll点列表，本次显示{rows}行\n"
    bashmsg += "QQ | ROLL\n"
    for item in data:
        bashmsg += f"{item[1]} | {item[3]}\n"
        if ITEMS == rows:
            break
    msg = bashmsg
    return msg