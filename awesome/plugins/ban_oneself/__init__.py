from nonebot import on_command, CommandSession, permission, on_startup
from config import QUN_id_list
import random
import sqlite3
from time import time


BANLIST = []

Qsql = sqlite3.connect(database="./databash/ban.db")
Qcursor = Qsql.cursor()


def addBan(qqid, qunid, bantime, duration):
    Qcursor.execute(f"""INSERT INTO banlist (QQID, QUNID, BANtime, duration) VALUES ({qqid}, {qunid}, {bantime}, {duration})""")
    Qsql.commit()


def delBan(qqid):
    Qcursor.execute(f"DELETE FROM banlist WHERE QQID={qqid}")
    Qsql.commit()


def isInBan(qqid):
    Qcursor.execute(f"SELECT * FROM banlist WHERE QQID={qqid}")
    date = Qcursor.fetchall()
    if len(date) != 0:
        return True
    else:
        return False
def selectBan(qqid):
    Qcursor.execute(f"SELECT * FROM banlist WHERE QQID={qqid}")
    date = Qcursor.fetchone()
    return date

@on_startup
def _():
    print("正在加载ban列表")
    sql = sqlite3.connect(database="./databash/ban.db")
    cursor = sql.cursor()
    cursor.execute("SELECT * FROM banlist")
    oldList = cursor.fetchall()
    oldBan = []
    for item in oldList:
        if ( item[3] + item[4] < time() ):
            cursor.execute(f"DELETE FROM banlist WHERE QQID={item[1]}")
            oldBan.append(item[1])
    try:
        sql.commit()
        print(f"加载成功，共加载[{len(oldList)}]个数据\n已删除[{len(oldBan)}]个过期数据")
    except:
        print("加载失败，请留意错误信息")
    for item in oldList:
        if item not in oldBan:
            BANLIST.append(item)


@on_command("banoneself", aliases=("随机自闭", "我要自闭"), only_to_me=False)
async def banoneself(session: CommandSession):
    duration = random.randint(2, 60) * 60
    user_role_dict = await session.bot.get_group_member_info(group_id=session.event.group_id, user_id=session.event.user_id)
    user_role = user_role_dict["role"]
    if user_role == "member":
        await session.send(f"随机自闭成功，本次自闭{int(duration/60)}分钟\n如需帮助请私聊群主或管理员\n私聊本机器人“我后悔了”可以解禁")
        bantime = time()
        await session.bot.set_group_ban(group_id=session.event.group_id, user_id=session.event.user_id, duration=duration)
        addBan(qqid=session.event.user_id, qunid=session.event.group_id, bantime=bantime, duration=duration)
    else:
        await session.send("你是管理员，无法进行禁言操作！")


@on_command("unbanoneself", aliases="我后悔了")
async def unbanoneself(session: CommandSession):
    user = session.event.user_id
    if isInBan(user):
        delBan(user)
        await session.bot.set_group_ban(group_id=selectBan(user)[2], user_id=user, duration=0)
        await session.send("已为你解除禁言状态")
    else:
        await session.send("你的禁言不是由“随机自闭插件“引起的")