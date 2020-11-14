#Ported from Nana remix by @buddhhu
#imported admin_cmd for DC by @hellboi_atul
import pygments, os, asyncio
from pygments.lexers import Python3Lexer
from pygments.formatters import ImageFormatter
from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern="pcode ?(.*)"))
async def coder_print(event):
	cmd = event.text
	a = await event.get_reply_message()
	coder = ""
	if len(cmd) > 7:
		coder = " ".join(cmd[7:])
	elif event.reply_to_msg_id and len(cmd) == 6:
		coder = a.message
	elif len(cmd) == 6:
		await event.reply("`No text Given`")
		await asyncio.sleep(2)
		await event.delete()
		return
	pygments.highlight(f"{coder}", Python3Lexer(), ImageFormatter(font_name="DejaVu Sans Mono", line_numbers=True), "out.png")
	await event.client.send_file(event.chat_id, "out.png", force_document=False)
	await event.delete()
	os.remove('out.png')
