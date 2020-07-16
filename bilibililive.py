import requests
from time import time, sleep

QUNLIST = {
    866912510
}
ROOMLIST = {
    936475,
    173551,
    97687
}
LIVES = {

}
LIVEROOMBASHURL = "https://api.live.bilibili.com/xlive/web-room/v1/index/getInfoByRoom?room_id="
BOTAPIBASHURP = "http://127.0.0.1:5700/send_group_msg"
SERVERBASHAPI = "https://sc.ftqq.com/SCU106022T8552c245baf3a4c46f68203a62ac65a85f104e66058af.send"
while True:
    for roomid in ROOMLIST:
        r = requests.get(url=LIVEROOMBASHURL + str(roomid)).json()
        livestatus = r["data"]["room_info"]["live_status"]
        try:
            if LIVES[roomid] != livestatus:
                LIVES[roomid] = livestatus
        except:
            LIVES[roomid] = livestatus
        finally:
            LIVES["lasttime" + str(roomid)] = time()
            if ( (livestatus == 1) and ( ((time() - LIVES["lasttime" + str(roomid)] >= 60 * 10) ))):
                text = f"{r['data']['anchor_info']['base_info']['uname']}已开播！\n前来围观：https://live.bilibili.com/{roomid}"
                desp = text * 10
                msg = f"{text}[CQ:image,file={r['data']['anchor_info']['base_info']['face']}]"
                for qun in QUNLIST:
                    data = {
                        "group_id": qun,
                        "message": msg
                    }
                    requests.post(url=BOTAPIBASHURP, data=data)
                ser_data = {
                    "text": text,
                    "desp": str(desp)
                }
                requests.post(url=SERVERBASHAPI, data=ser_data)
        print(f"{r['data']['anchor_info']['base_info']['uname']}--[{livestatus}]--{time()}")
    sleep(30)
