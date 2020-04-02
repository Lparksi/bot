from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQhttpError

@nonebot.scheduler.scheduled_job('cron',hour='*')
async def _():
    bot = nonebot.get_bot()
    now = datetime.ctime()
    try:
        await bot.send_group_msg(group_id=672076603,message=str(now))
    except CQhttpError:
        pass