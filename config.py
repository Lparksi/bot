from nonebot.default_config import *
from datetime import timedelta
import re

HOST = '0.0.0.0'
PORT = 8888

SUPERUSERS = {2726043636}
COMMAND_START = ['', re.compile(r'[/!]+')]
COMMAND_START = {'', '/', '!', '／', '！','.'}
SESSION_EXPIRE_TIMEOUT = timedelta(minutes=2)
SESSION_RUN_TIMEOUT = timedelta(seconds=10)