from YukkiMusic import app
from pyrogram import Client
from pyrogram.types import Message
from .admin_check import authorized_users_only




@app.on_message(
    filters.command("ban") & filters.group & ~filters.edited
)
@authorized_users_only
async def ban(client, message):
    try:
        await app.send_message(message.chat.id, "✅ userbot successfully left chat")
        await app.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            "❌ **userbot couldn't leave your group, may be floodwaits.**\n\n**» or manually kick userbot from your group**"
        )

        return
