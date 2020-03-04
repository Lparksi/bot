from jieba import posseg
from nonebot import (CommandSession, IntentCommand, NLPSession, on_command,
                     on_natural_language)

from .get_yiqing_of_city import get_yiqing_of_city


@on_command('yiqing',aliases=("疫情","查疫情","疫情详情"))
async def yiqing(session: CommandSession):
    city = session.get('city',prompt="你要查询哪个城市的")
    yiqing_report = get_yiqing_of_city(city)
    await session.send(yiqing_report)

@yiqing.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['city'] = stripped_arg
            return
    if not stripped_arg:
       session.pause("要查询的城市不能为空")
    session.state[session.current_key] = stripped_arg       

@on_natural_language(keywords={"疫情"})
async def _(session: NLPSession):
    stripped_msg = session.msg_text.strip()
    words = posseg.lcut(stripped_msg)

    city = None
    for word in words:
        if word.flag == "ns":
            city = word.word
            break
    return IntentCommand(90.0,"yiqing")
