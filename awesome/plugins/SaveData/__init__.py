from ..tools.func.AddData import Add_Data
from ..tools.func.Select import Select
from nonebot import on_command, CommandSession
@on_command("load",only_to_me=True)
async def load(session: CommandSession):
    group_id = session.get('group_id')
    group_list =await session.bot.get_group_member_list(group_id=group_id)
    for x in group_list:
        user_id = x["user_id"]
        nickname = x[r"nickname"]
        sex = x["sex"]
        age = x["age"]
        if Select(user_id) == None:
            Add_Data(qq=user_id,nickname=nickname,sex=sex,age=age)
        else:
            pass
    await session.send("执行完毕！")
@load.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['group_id'] = stripped_arg
        return

    if not stripped_arg:
        pass
@on_command('list',only_to_me=True)
async def load(session: CommandSession):
    list = await session.bot.get_group_list()
    await session.send(str(list))