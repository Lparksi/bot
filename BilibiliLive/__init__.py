import time

import requests
import sql as sql

HttpApi = 'http://127.0.0.1:5700'
FTqqApi = 'https://sc.ftqq.com/SCU106022T8552c245baf3a4c46f68203a62ac65a85f104e66058af.send'
BilibiliApi = 'https://api.live.bilibili.com/xlive/web-room/v1/index/getInfoByRoom?room_id='

HttpApiQun = HttpApi + '/send_group_msg'
HttpApiUser = HttpApi + '/send_private_msg'

QunIdList = []
UserIdList = [2726043636]
RoomIdList = [936475, 97687]

while True:
    for item in RoomIdList:
        r = requests.get(url=BilibiliApi + str(item))
        ret = r.json()
        LiveRoomAnchorName = ret["data"]["anchor_info"]["base_info"]["uname"]
        LiveRoomAnchorFace = ret["data"]["anchor_info"]["base_info"]["face"]
        Livestatus = ret["data"]["room_info"]["live_status"]
        Livetitle = ret["data"]["room_info"]["title"]
        Livetags = ret["data"]["room_info"]["tags"]
        Livecover = ret["data"]["room_info"]["cover"]
        LiveKeyimage = ret["data"]["room_info"]["keyframe"]
        # 图片版本 1
        # qqmsg = f"""---Bilibili 直播助手---
        # 当前主播：{LiveRoomAnchorName}\n[CQ:image,file={LiveRoomAnchorFace}]
        # 直播间：{item} -- {Livetitle}
        # 标签：{Livetags}
        # 关键帧：[CQ:image,file={Livecover}],[CQ:image,file={LiveKeyimage}]
        # """
        qqmsg = f"""---Bilibili 直播助手---
当前主播：{LiveRoomAnchorName}
直播间：{item} -- {Livetitle}
标签：{Livetags}
直通车：https://live.bilibili.com/{item}
"""
        wxmsg = f"""---Bilibili 直播助手---
当前主播：{LiveRoomAnchorName}
直播间：{item} -- {Livetitle}
标签：{Livetags}
"""
        wxdata = {
            'text': LiveRoomAnchorName,
            'desp': wxmsg
        }


        def sendALL():
            print(f"[{time.ctime()}]正在发送[{LiveRoomAnchorName}-{Livetitle}]的直播间推送")
            for qqid in UserIdList:
                qqdata = {
                    'user_id': qqid,
                    'message': qqmsg
                }
                requests.post(url=HttpApiUser,
                              data=qqdata)
            for qunid in QunIdList:
                qqdata = {
                    'group_id': qunid,
                    'message': qqmsg
                }
                requests.post(url=HttpApiQun,
                              data=qqdata)
            requests.post(url=FTqqApi,
                          data=wxdata)


        if not sql.inList(item):
            sql.addRoom(roomid=item,
                    status=Livestatus,
                    time=time.time())
            if Livestatus == 1:
                sendALL()
        if not (sql.selStatus(roomid=item) == Livestatus):
            sql.upRoom(roomid=item,
                   status=Livestatus,
                   time=time.time())
        if time.time() - sql.selTime(roomid=item) > (10 * 60):
            if Livestatus == 1:
                print("时间超出10分钟，已批准发送")
                sendALL()
        if Livestatus == 1:
            print(f"[{time.ctime()}][{LiveRoomAnchorName}]-正在直播")
        elif Livestatus == 2:
            print(f"[{time.ctime()}][{LiveRoomAnchorName}]-正在轮播")
        elif Livestatus == 0:
            print(f"[{time.ctime()}][{LiveRoomAnchorName}]-未直播")
    time.sleep(2 * 60)
