# 授权命令
from nonebot.permission import SUPERUSER
from nonebot import on_command, CommandSession
from ..tools.func.AUTH import Add_administrator, Add_root, Del_administrator, Del_root
from ..tools.func.Select import Select

@on_command('AddRoot',aliases=("添加超级管理员"),permission=SUPERUSER)
async def AddRoot(session: CommandSession):
    user_id = int(session.get("user_id"))

    try:
        Add_root(user_id)
        Add_administrator(user_id)
        code1 = Select(user_id)[5]
        code2 = Select(user_id)[6]
        if code1 and code2 == 1:
            await session.send(f"超级管理员：[CQ:at,qq={user_id}],已添加")
        else:
            await session.send("添加失败")
    except IOError:
        await session.send("添加失败")
@AddRoot.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['user_id'] = stripped_arg
        return

    if not stripped_arg:
        pass

@on_command('Addadministrator',aliases=("添加管理员"),permission=SUPERUSER)
async def Addadministrator(session: CommandSession):
    user_id = int(session.get("user_id"))

    try:
        Add_administrator(user_id)
        code = Select(user_id)[6]
        if code == 1:
            await session.send(f"管理员：[CQ:at,qq={user_id}],已添加")
        else:
            await session.send("添加失败")
    except:
        await session.send("添加失败")
@Addadministrator.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['user_id'] = stripped_arg
        return

    if not stripped_arg:
        pass


@on_command('DelRoot', aliases=("删除超级管理员"), permission=SUPERUSER)
async def DelRoot(session: CommandSession):
    user_id = int(session.get("user_id"))

    try:
        Del_root(user_id)
        Del_administrator(user_id)
        code1 = Select(user_id)[5]
        code2 = Select(user_id)[6]
        if code1 ==0 and code2 == 0:
            await session.send(f"超级管理员：[CQ:at,qq={user_id}],已删除")
        else:
            await session.send("删除失败，请手动删除")
    except:
        await session.send("删除失败")


@DelRoot.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['user_id'] = stripped_arg
        return

    if not stripped_arg:
        pass


@on_command('Deladministrator', aliases=("删除管理员"), permission=SUPERUSER)
async def Deladministrator(session: CommandSession):
    user_id = int(session.get("user_id"))

    try:
        Del_administrator(user_id)
        code = Select(user_id)[6]
        if code ==0:
            await session.send(f"管理员：[CQ:at,qq={user_id}],已删除")
        else:
            await session.send("删除失败，请手动删除")
    except:
        await session.send("删除失败")


@Deladministrator.args_parser
async def _(session: CommandSession):
    stripped_arg = int(session.current_arg_text.strip())

    if session.is_first_run:
        if stripped_arg:
            session.state['user_id'] = stripped_arg
        return

    if not stripped_arg:
        pass
