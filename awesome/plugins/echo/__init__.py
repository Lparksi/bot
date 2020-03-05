from nonebot import on_command, CommandSession

@on_command("echo")
async def echo(session: CommandSession):
    await session.send(session.state.get("message") or session.current_arg)