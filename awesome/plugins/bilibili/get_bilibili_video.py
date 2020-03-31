from bilibili_api import video

def get_video_info(BV)-> str:
    try:
        v = video.VideoInfo(bvid=str(BV))
        info = v.get_video_info()
        print(info)
        bv_id = info["bvid"]
        title = info["title"]
        desc = info["desc"]
        dynamic = info["dynamic"]
        mid = info['owner']["mid"]
        name = info["owner"]["name"]
        return f"""{title}:
Bvid:{BV}
{desc}
标签：{dynamic}
发布者：{name}
""",f"""视频链接：https://www.bilibili.com/video/BV{BV}/
发布者主页：https://space.bilibili.com/{mid}/"""
    except :
        return "请求错误！"
def find_bv(url):
    bv = url.split("/")[-1][2:]
    return bv