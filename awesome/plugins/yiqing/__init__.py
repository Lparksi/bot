from nonebot import on_command, CommandSession
from .get_yiqing_of_city import get_yiqing_of_city

@on_command('yiqing',aliases=('疫情','查疫情'),only_to_me=False)
async def yiqing(session: CommandSession):
    city = session.get('city',prompt='你想查询哪个城市的疫情？（仅市级，不带市）')
    yiqing_report = get_yiqing_of_city(city)
    await session.send(yiqing_report)

@yiqing.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将城市名跟在命令名后面，作为参数传入
            # 例如用户可能发送了：天气 南京
            session.state['city'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('要查询的城市名称不能为空呢，请重新输入')
