from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from jieba import posseg


@on_command("sushe",  aliases=("宿舍", "寝室"), only_to_me=False)
async def sushe(session: CommandSession):
    if session.event.group_id == 818278353:
        await session.send("""一般都是6人间，上下铺，桌子一侧排，有空调，另外租（租比较贵，就这两年，跟舍友商量好要不要租）。
男生一般都是十里铺，也就是校外宿舍，当然还有三里屯之类的，就认准在十里铺就好)""")


@on_command("sushe_img", aliases=("宿舍照片", "寝室照片"), only_to_me=False)
async def suzheimg(session: CommandSession):
    if session.event.group_id == 818278353:
        await session.send("""[CQ:image,file=https://s1.ax1x.com/2020/07/27/aPVaff.jpg]""")


@on_natural_language(keywords={"宿舍", "寝室"}, only_to_me=False)
async def _(session: NLPSession):
    stripped_msg = session.msg_text.strip()
    words = posseg.lcut(stripped_msg)
    for word in words:
        if word.word == "照片":
            return IntentCommand(60.0, 'sushe_img')
        if word.word == "洗澡":
            return IntentCommand(60.0, 'xizao')
    return IntentCommand(61.0, 'sushe')


@on_command('xizao', aliases="洗澡", only_to_me=False)
async def xizao(session: CommandSession):
    if session.event.group_id == 818278353:
        await session.send("""男生宿舍有洗澡间，女生在校内澡堂，不过只有2楼可以洗热水澡，需要刷单独洗澡卡，可以好几个人同时洗有问题请联系：[CQ:at,qq=331456218]""")


@on_natural_language(keywords="洗澡", only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(60.0, 'xizao')


@on_command("kaixue", only_to_me=False, aliases="开学")
async def kaixue(session: CommandSession):
    if session.event.group_id == 818278353:
        await session.send("""具体开学时候还未确定，一般9月份，咱学校有病例，估计9月份开不了学，会延期或不开学。
有问题请联系：[CQ:at,qq=331456218]""")


@on_natural_language(keywords={"开学"}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(60.0, 'kaixue')


@on_command("zuidifen", aliases="最低分", only_to_me=False)
async def zuidifen(session: CommandSession):
    if session.event.group_id == 818278353:
        await session.send("""按最低分是不能考虑能不能上的，应该以你的专业招生的院校排名和人数拉一个单子，依次累加，根据你的排名来算，你可以问我如何算排名。
有问题请联系：[CQ:at,qq=331456218]""")


@on_natural_language(keywords={"最低分", "多少分"}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(60.0, "zuidifen")


@on_command("whoisgood", aliases="哪个好", only_to_me=False)
async def whoisgood(session: CommandSession):
    if session.event.group_id == 818278353:
        await session.send("""河南省近几年大量扩招专升本的学生，说明对专升本学生更加重视，也说明确实对省内本科教育越来越看中，同时也为河南学子争取本科权益。
当然，河南省内本科都差不多，如果考虑普通高考中的普通二本来对比专升本哪个学校好，其实省内院校都一样的，无需纠结，因为都是省内，又不是郑大那种特别好的学校，出门人家看的是学历
有问题请联系：[CQ:at,qq=331456218]""")


@on_natural_language(keywords={"哪个好"}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(60.0, "whoisgood")


@on_command("yonon", aliases="能不能上", only_to_me=False)
async def yonon(session: CommandSession):
    if session.event.group_id == 818278353:
        await session.send("[CQ:image,file=https://s1.ax1x.com/2020/07/27/aPnGgf.jpg]")


@on_natural_language(keywords={"能不能", "能"}, only_to_me=False)
async def _(session: NLPSession):
    stripped_msg = session.msg_text.strip()
    words = posseg.lcut(stripped_msg)
    for word in words:
        if word.word == "上":
            return IntentCommand(60.0, "yonon")


@on_command("spm", aliases="算排名", only_to_me=False)
async def spm(session: CommandSession):
    if session.event.group_id == 818278353:
        await session.send("[CQ:image,file=https://s1.ax1x.com/2020/07/27/aPQAde.jpg]")


@on_natural_language(keywords={"算排名", "排名"}, only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(60.0, "spm")