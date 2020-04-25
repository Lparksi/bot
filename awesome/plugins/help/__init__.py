from nonebot import on_command, CommandSession


@on_command("help", only_to_me=True)
async def help(session: CommandSession):
    await session.send("""HELP:
目前插件:
查询天气 | 天气，天气预报，查天气
查询疫情 | 疫情，查疫情，疫情详情
笑话 | 笑话，讲笑话，讲一个笑话
一言 | 一言，每日一言
文言一言 | 文言文，古诗词，古诗文，古诗词文言，古诗文言
复读 | echo
Bilibili视频简介 | BV
开源项目地址：
http://t.cn/A6ZMoP1b
Bot使用帮助：
http://t.cn/A6ZMoZGS
对应码云链接：
http://t.cn/A6Zx44Vo
http://t.cn/A6Zx4cab
作者博客：https://parksi.xyz
欢迎入群交流：
866912510
最新功能：bilibili视频简介""")