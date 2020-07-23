from nonebot import on_command, CommandSession, on_startup
import random
import sqlite3
from config import QUN_id_list
from awesome.plugins.roll.sql import *
from time import time
from awesome.plugins.roll.history import getHistory

MIN = 0
MAX = 100


@on_startup
def LoadSql():
    print("-" * 10 + "正在加载roll点数据库" + "-" * 10)
    Sql = sqlite3.connect("./databash/roll.db")
    Cursor = Sql.cursor()
    Cursor.execute("SELECT * FROM rolllog")
    logitems = len(Cursor.fetchall())
    print(f"已加载[{logitems}]条roll点记录")
    Cursor.execute("SELECT * FROM roll")
    useritems = len(Cursor.fetchall())
    print(f"已加载[{useritems}]个用户")


@on_command("roll", only_to_me=False)
async def roll(session: CommandSession):
    if session.event.group_id in QUN_id_list:
        if isEmpty(userid=session.event.user_id):
            newUser(userid=session.event.user_id, qunid=session.event.group_id)
            await session.send("你是新用户，正在注册账户\n注册成功")
        roll = random.randint(MIN, MAX)
        updata(userid=session.event.user_id, roll=roll)
        allroll = selRoll(session.event.user_id)
        await session.send(f"本次roll点数为：{roll}\n你的所有roll点的总和是{allroll}")
        addrolllog(userid=session.event.user_id, qunid=session.event.group_id, roll=roll, time=time())


@on_command("roll_his", only_to_me=False)
async def roll_his(session: CommandSession):
    if session.event.group_id in QUN_id_list:
        msg = getHistory(qunid=session.event.group_id)
        await session.send(msg)