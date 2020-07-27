from nonebot import on_command, CommandSession
from config import QUN_id_list
from awesome.plugins.sleep.sql import *
import time
import random
from awesome.plugins.sleep.logsql import *

SLEEPTEXT = ["晚安，祝你好梦",
             "晚安，明天早上见",
             "睡什么睡，起来嗨！",
             "今天月亮不营业 所以由我来说晚安"]
SLEEPEDTEXT = ["今天结束啦 现在立刻马上把细碎的烦恼暂停关掉 把月亮挂好 睡个好觉",
               "晚睡的小孩不会有美梦光临哦",
               "结束了一天的忙碌，好好休息，睡个好觉，晚安。"]
GETUPTEXT = ["早安，新的一天元气满满",
             "早安，今天也要开开心心地度过",
             "早安，早安喵~",
             "早安，带着满满的勇气去征服这世界吧！"]


@on_command("sleep", aliases=("晚安", "安", "晚"), only_to_me=False)
async def sleep(session: CommandSession):
    if session.event.group_id in QUN_id_list:
        isSleeper = isSleep(session.event.user_id)
        now = time.time()
        if not isSleeper:
            if isGetup(session.event.user_id):
                delGetup(session.event.user_id)
            addSleeper(userid=session.event.user_id,
                       qunid=session.event.group_id,
                       time=now)
            sleepers = selSleepers(qunid=session.event.group_id)
            addSleepLogSleep(userid=session.event.user_id,
                             data=time.ctime(),
                             time=now)
            await session.send(f"你是今天第{sleepers}睡觉的小可爱\n{SLEEPTEXT[random.randint(0, len(SLEEPTEXT))-1]}")
        else:
            await session.send(f"{SLEEPEDTEXT[random.randint(0, len(SLEEPEDTEXT)-1)]}\n还不去睡觉？？？")


@on_command("getup", aliases=("早安", "早"), only_to_me=False)
async def getup(session: CommandSession):
    if session.event.group_id in QUN_id_list:
        isSleeper = isSleep(userid=session.event.user_id)
        now = time.time()
        if isSleeper:
            if now - getSleepTime(session.event.user_id) > 2 *60 *60:
                delSleeper(userid=session.event.user_id)
                addGetup(userid=session.event.user_id, time=now)
                addSleepLogGetup(userid=session.event.user_id,
                                 time=now,
                                 data=time.ctime())
                await session.send(f"你是今天第{selGetups(session.event.group_id)}起床的小可爱\n{GETUPTEXT[random.randint(0, len(GETUPTEXT)-1)]}")
            else:
                await session.send(f"失眠了吗，让本宝宝陪你（#+空格+文字 智能闲聊）\n起床请求未被受理！")