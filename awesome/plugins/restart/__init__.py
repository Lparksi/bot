from nonebot import on_command, CommandSession, permission


@on_command("restart", only_to_me=False)
async def restart(session: CommandSession):
    if await permission.check_permission(session.bot, session.event, permission.SUPERUSER):
        await session.send("用户鉴权通过，用户组:SUPERUSER\n正在执行操作：重启")
        await session.bot.set_restart_plugin()
    else:
        await session.send("用户鉴权失败!")