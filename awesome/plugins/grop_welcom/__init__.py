from nonebot import on_notice, NoticeSession

@on_notice('group_increase')
async def _(session: NoticeSession):
    if session.event.group_id == 866912510:
        user_id = session.event.user_id
        await session.send(f"[CQ:at,qq={user_id}]:\n欢迎入群~,输入'help'获取机器人使用说明!")
    else:
        pass