from nonebot import on_notice, NoticeSession
from config import QUN_id_list
from awesome.plugins.ban_oneself import delBan, BANLIST, selectBan
from time import sleep


# 入群
@on_notice("group_increase")
async def _(session: NoticeSession):
    if session.event.group_id in QUN_id_list:
        # await session.send(f"[CQ:at,qq={session.event.user_id}],欢迎入群！[CQ:image,file=http://q.qlogo.cn/headimg_dl?dst_uin=2726043636&spec=100]")
        await session.send("敏感问题请加tg群:https://tg.parksi.xyz，[CQ:image,file=https://s1.ax1x.com/2020/07/17/Us5h7T.png]")


# 退群
@on_notice("group_decrease")
async def _(session: NoticeSession):
    if session.event.group_id in QUN_id_list:
        await session.send(f"{session.event.user_id}离开了我们!")


# todo: 管理员 增加/减少
# @on_notice("group_admin")
# async def _(session: NoticeSession):
#    if session.event.group_id in QUN_id_list:
#        if session.event.sub_type == "set":
#            await session.send(f"[CQ:at,qq={session.event.user_id}],恭喜成为管理员")
#        else:
#            nickname_dict = await session.bot.get_group_member_info(group_id=session.event.group_id, user_id=session.event.user_id)
#            nickname = nickname_dict["card"]
#            await session.send(f"非常遗憾，{nickname}失去了管理员资格")


# 禁言
# TODO:优化禁言时间
@on_notice("group_ban")
async def _(session: NoticeSession):
    if session.event.group_id in QUN_id_list:
        # 是否是随机自闭插件造成 逆转返回
        # if session.event.user_id in BANLIST:
        #    status = False
        # else:
        #     status = True

        # if session.event.sub_type == "ban" :
        #     await session.send(f"[CQ:at,qq={session.event.user_id}],你已被禁言\n操作者：[CQ:at,qq={session.event.operator_id}]")
        # elif session.event.sub_type == "lift_ban":
        #     await session.send(f"[CQ:at,qq={session.event.user_id}],你已被取消禁言，请注意发言！")
        #     delBan(qqid=session.event.user_id)
        # else:
        #     pass
        if session.event.sub_type == "lift_ban":
            if len(selectBan(session.event.user_id)) != 0:
                delBan(session.event.user_id)
            else:
                await session.send(f"[CQ:at,qq={session.event.user_id}]你已被解除禁言，请注意发言")
        if session.event.sub_type == "ban":
            if len(selectBan(session.event.user_id)) != 0:
                pass
            else:
                await session.send(f"[CQ:at,qq={session.event.user_id}]，你已被禁言，请遵守群规.")
