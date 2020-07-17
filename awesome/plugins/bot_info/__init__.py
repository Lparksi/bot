from nonebot import on_command, CommandSession


@on_command("info", only_to_me=False)
async def info(session: CommandSession):
    bot_info = await session.bot.get_login_info()
    bot_qq = bot_info["user_id"]
    nickname_dict = await session.bot.get_group_member_info(group_id=session.event.group_id, user_id=session.self_id)
    nickname = nickname_dict["card"]
    qun_info = await session.bot.get_group_info(group_id=session.event.group_id)
    group_id = qun_info["group_id"]
    group_name = qun_info["group_name"]
    member_count = qun_info["member_count"]
    max_member_count = qun_info["max_member_count"]
    await session.send(f"""登入号：{bot_qq}\n昵称：{nickname}\n群信息：{group_name}({group_id}),{member_count}/{max_member_count}""")