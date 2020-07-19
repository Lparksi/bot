from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.nlp.v20190408 import nlp_client, models
import json
from nonebot import on_command, CommandSession
import config


def upload(test):
    try:
        cred = credential.Credential("AKIDqWw76td4PaibJoaEBMLBlARTdaXHhoVw", "PFs7DGNNCmCYfe7bqyucBVhcZ3PabU9h")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "nlp.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = nlp_client.NlpClient(cred, "ap-guangzhou", clientProfile)

        req = models.ChatBotRequest()

        params = json.dumps({
            "Query" : test
        })

        req.from_json_string(params)

        resp = client.ChatBot(req)
        print(resp.to_json_string())
        date = json.loads(resp.to_json_string())["Reply"]
        return date

    except TencentCloudSDKException as err:
        print(err)
        return "error"


@on_command("txai", aliases="#", only_to_me=False)
async def txai(session: CommandSession):
    if session.event.group_id in config.QUN_id_list:
        resp = upload(session.state["text"])
        await session.send(resp)
    if session.event.group_id == 1060028351:
        resp = upload(session.state["text"])
        await session.send(resp)
@txai.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将城市名跟在命令名后面，作为参数传入
            # 例如用户可能发送了：天气 南京
            session.state['text'] = stripped_arg
        return