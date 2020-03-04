from nonebot import on_command, CommandSession
from .get import get_yiyan

@on_command('yiyan',aliases=("一言","每日一言"))
async def yiyan(session: CommandSession):
    message = get_yiyan()
    await session.send(message)