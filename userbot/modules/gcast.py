
from userbot.events import register
from userbot import CMD_HELP, bot
# KEN KAN Ganteng


@register(outgoing=True, pattern="^.gcast (.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("`Kaisar, Mohon Berikan Sebuah Pesan`")
    tt = event.text
    msg = tt[6:]
    kk = await event.edit("`Kaisar Sedang Mengirim Pesan Secara Global... 📢`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"**Kaisar Berhasil Mengirim Pesan Ke** `{done}` **Grup, Gagal Mengirim Pesan Ke** `{er}` **Grup**")

CMD_HELP.update(
    {
        "gcast": "`.gcast <pesan>`\
    \nPenjelasan: Global Broadcast mengirim pesan ke Seluruh Grup yang Lord Masuki."
    })
