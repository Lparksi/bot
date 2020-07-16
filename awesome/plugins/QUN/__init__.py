from nonebot import on_notice, NoticeSession
from config import QUN_id_list


# 入群
@on_notice("group_increase")
async def _(session: NoticeSession):
    if session.event.group_id in QUN_id_list:
        await session.send(f"[CQ:at,qq={session.event.user_id}],欢迎入群！")


# 退群
@on_notice("group_decrease")
async def _(session: NoticeSession):
    if session.event.group_id in QUN_id_list:
        await session.send(f"{session.event.user_id}离开了我们!")


# 管理员 增加/减少
@on_notice("group_admin")
async def _(session: NoticeSession):
    if session.event.group_id in QUN_id_list:
        if session.event.sub_type == "set":
            await session.send(f"[CQ:at,qq={session.event.user_id}],恭喜成为管理员")


# 
