import requests
from nonebot import on_command, CommandSession
@on_command("load",only_to_me=True)
async def load(session: CommandSession):
    group_list =await session.bot.get_group_member_list(group_id=866912510)
    data = group_list[0]
    age = data["age"]
    nickname = data["nickname"]
    sex = data["sex"]
    user_id = data["user_id"]

@on_command("text")
async def text(session: CommandSession):
    pass