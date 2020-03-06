from nonebot import on_command, CommandSession

@on_command("help")
async def help(session: CommandSession):
    await session.send("[CQ:file=https://s2.ax1x.com/2020/03/06/3b1k1e.png]")