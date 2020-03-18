from nonebot import on_command, RequestSession
from .get import get_wenyan

@on_command('wenyan',aliases=("文言文","古诗文","古诗词","古诗词文言","古诗一言"),only_to_me=False)
async def wenyan(session: RequestSession):
    await session.send(await get_wenyan())