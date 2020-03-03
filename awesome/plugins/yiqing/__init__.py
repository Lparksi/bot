from nonebot import on_command, CommandSession
from .get_yiqing_of_city import get_yiqing_of_city

@on_command('yiqing',aliases=('疫情','查疫情'))
async def yiqing(session: CommandSession):
    city = session.get('city',prompt='你想查询哪个城市的疫情？（仅市级，不带市）')
    yiqing_report = get_yiqing_of_city(city)
    await session.send(yiqing_report)

@yiqing.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    #第一次运行
    if session.is_first_run:
        if session.state['city'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('要查询的城市不能为空')
    session.state[session.current_key] = stripped_arg
