from nonebot import on_command, CommandSession
from json import loads


@on_command("status", only_to_me=False)
async def status(session: CommandSession):
    data = await session.bot.get_version_info()
    edition = data["coolq_edition"]
    version = data["plugin_version"]
    build_number = data["plugin_build_number"]
    build_configuration = data["plugin_build_configuration"]
    msg = f"""平台：CQ {edition}
CQHTTP版本：{version} build：{build_number}
插件配置：{build_configuration}"""
    await session.send(msg)