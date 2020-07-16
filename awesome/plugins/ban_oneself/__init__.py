from nonebot import on_command, CommandSession
from config import QUN_id_list
import random


@on_command("ban_oneself_random", aliases=("随机自闭", "sjzb"), only_to_me=False)
async def ban_oneself(session: CommandSession):
    if session.event.group_id in QUN_id_list:
        time = random.randint(2, 60) * 60
        await session.send(f"[CQ:at,qq={session.event.user_id}],随机自闭成功\n本次自闭：{time / 60}分钟\n如有需要请私聊管理员或群主")
        await session.bot.set_group_ban(group_id=session.event.group_id, user_id=session.event.user_id, duration=time)
