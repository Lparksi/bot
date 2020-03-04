from nonebot import on_command ,CommandSession
from .get import get_xiaohau

@on_command("xiaohua",aliases=("笑话","讲笑话","讲一个笑话"),only_to_me=False)
async def xiaohua(session: CommandSession):
    xh = get_xiaohau()
    await session.send(xh)