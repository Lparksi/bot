from nonebot import on_notice, NoticeSession

GROPUS = [866912510]
#欢迎
@on_notice('group_increase')
async def _(session: NoticeSession):
    if session.event.group_id in GROPUS:
        user_id = session.event.user_id
        await session.send(f"[CQ:at,qq={user_id}]:\n欢迎入群~,输入'help'获取机器人使用说明!")
    else:
        pass
#退出
@on_notice('group_decrease')
async def _(session: NoticeSession):
    if session.event.group_id in GROPUS:
        if session.event.sub_type == 'leave':
            user_id = session.event.user_id
            await session.send(f"""---成员离开---
天下无不散的宴席，
{user_id}离开了我们""")
        elif session.event.sub_type == 'kick':
            user_id = session.event.user_id
            operator_id = session.event.operator_id
            await session.send(f"""---成员被踢---
请遵守本群群规，禁止涉及黄色、政治。引站等相关内容
被踢者:{user_id}
操作者:{operator_id}""")
        elif session.event.sub_type == 'kick_me':
            group_id = session.event.group_id
            await session.bot.send_private_msg(user_id=2726043636,message=f"登入账号已被提出,群聊{group_id}")
        else:
            pass
    else:
        pass
#禁言
@on_notice('group_ban')
async def _(session: NoticeSession):
    if session.event.group_id in GROPUS:
        if session.event.sub_type == 'ban':
            user_id = session.event.user_id
            operator_id = session.event.operator_id
            duration = session.event["duration"]
            await session.send(f"""用户{user_id}被禁言{duration}秒,执行人：{duration}""")
    else:
        pass

#管理员变动
@on_notice("group_admin")
async def _(session: NoticeSession):
    if session.event.group_id in GROPUS:
        if session.event.sub_type == 'set':
            user_id = session.event.user_id
            await session.send(f"""---管理员增加---
获得管理资格：{user_id}""")
        elif session.event.sub_type == 'unset':
            user_id = session.event.user_id
            await  session.send(f"""---管理员减少---
取消管理资格：{user_id}""")
    else:
        pass
