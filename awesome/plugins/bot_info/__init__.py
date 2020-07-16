from nonebot import on_command, CommandSession


@on_command("info", only_to_me=False)
async def info(session: CommandSession):
    bot_info = await session.bot.get_login_info()
    bot_qq, nickname = bot_info["user_id"], bot_info["nickname"]
    await session.send(f"""登入号：{bot_qq}\n昵称：{nickname}""")