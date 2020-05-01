from nonebot import on_command, CommandSession
from .get import get_zuan


@on_command('zuan', aliases=("祖安"))
async def zuan(session: CommandSession):
    await session.send(str(get_zuan()))
