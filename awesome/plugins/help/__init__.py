from nonebot import on_command, CommandSession

@on_command("help",only_to_me=False)
async def help(session: CommandSession):
    await session.send("""HELP:
    目前插件:
    查询天气 | 天气，天气预报，查天气
    查询疫情 | 疫情，查疫情，疫情详情
    笑话 | 笑话，讲笑话，讲一个笑话
    一言 | 一言，每日一言
    文言一言 | 文言文，古诗词，古诗文，古诗词文言，古诗文言
    复读 | echo
    开源项目地址：http://t.cn/A67B9Hq6
    Bot使用帮助：http://t.cn/A67B9nmf""")