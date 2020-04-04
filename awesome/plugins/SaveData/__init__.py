from ..tools.func.AddData import Add_Data
from nonebot import on_command, CommandSession
@on_command("load",only_to_me=True)
async def load(session: CommandSession):
    group_id = session.get('group_id')
    group_list =await session.bot.get_group_member_list(group_id=group_id)
    for x in group_list:
        user_id = x["user_id"]
        nickname = x["nickname"]
        sex = x["sex"]
        age = x["age"]
        Add_Data(qq=user_id,nickname=nickname,sex=sex,age=age)

@load.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['group_id'] = stripped_arg
        return

    if not stripped_arg:
        pass

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态

@on_command('list',only_to_me=True)
async def load(session: CommandSession):
    list = await session.bot.get_group_list()
    await session.send(str(list))