from nonebot import on_command, CommandSession
from config import QUN_id_list


@on_command("info", only_to_me=False)
async def info(session: CommandSession):
    bot_info = await session.bot.get_login_info()
    bot_qq = bot_info["user_id"]
    nickname_dict = await session.bot.get_group_member_info(group_id=session.event.group_id, user_id=session.self_id)
    nickname = nickname_dict["card"]
    qun_info = await session.bot.get_group_info(group_id=session.event.group_id)
    group_id = qun_info["group_id"]
    group_name = qun_info["group_name"]
    member_count = qun_info["member_count"]
    max_member_count = qun_info["max_member_count"]
    await session.send(
        f"""登入号：{bot_qq}\n昵称：{nickname}\n群信息：{group_name}({group_id}),{member_count}/{max_member_count}""")


@on_command("userinfo", only_to_me=False)
async def userinfo(session: CommandSession):
    if session.event.group_id in QUN_id_list:
        userid = session.get('userid', prompt="你要查询哪个QQ的信息呢?")
        dict = await session.bot.get_stranger_info(user_id=userid)
        nickname, sex, age = dict["nickname"], dict["sex"], dict["age"]
        bashmsg = f"用户：{nickname}({userid})的信息如下：\n"
        if sex == 'male':
            sex = "男"
        elif sex == "female":
            sex = "女"
        else:
            sex = "未知"
        bashmsg += f"昵称：{nickname}\n性别：{sex}\n年龄：{age}"
        await session.send(bashmsg)
        session.finish()


@userinfo.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['userid'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的QQ不能为空呢，请重新输入')

        # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg
