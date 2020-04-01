from nonebot import on_command,CommandSession
from .get_bilibili_video import *
from .get_bilibili_liveroom_info import *
@on_command("Bilibili_Video",aliases=("B站视频","BV","bv"),only_to_me=False)
async def Bilibili_Video(session: CommandSession):
    Video_id = session.get("BV", prompt="查询哪个视频？")
    if len(Video_id) > 10:
        bv = find_bv(Video_id)
    else:
        bv = Video_id
    ret = get_video_info(bv)
    for x in ret:
        await session.send(x)
@Bilibili_Video.args_parser
async def _(session: CommandSession):
    str_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if str_arg:
            session.state['BV'] = str_arg
        return
    if not str_arg:
        session.pause('视频号不能为空，请重新输入')
    session.state[session.current_key] = str_arg

@on_command("B_live",aliases=("直播","B"))