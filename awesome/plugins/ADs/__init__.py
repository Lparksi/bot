from nonebot import on_command, CommandSession


@on_command("ads", aliases=("友链", "换友链"))
async def ads(session: CommandSession):
    await session.send("""https://parksi.xyz换友链
已收录的友链：
https://skina.cn/
https://www.myxx-writer.club/
https://saky.site/
https://linghan.gearhostpreview.com/
https://blog.itjoker.cn/
https://kzero.vip/
https://qqfloatingice.github.io/
https://sosilent.top/
https://alastor.top/""")