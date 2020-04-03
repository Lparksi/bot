from nonebot import on_command, CommandSession
from ..tools.SQL.AddData import Add_Data


@on_command("load",only_to_me=True,permission=2726043636)
async def load(session: CommandSession):
    group_list =await session.bot.get_group_member_list(group_id=866912510)
    for x in group_list:
        print(x)
        user_id = x["user_id"]
        sex = x["sex"]
        nickname = x["nickname"]
        age = x["age"]
        Add_Data(qq=123456,nickname="123",sex="man",age=14)
