from pyrogram import Client, filters
from YukkiMusic import userbot as USER
from config import OWNER_ID



@Client.on_message(filters.command(["alljoin"]))
@sudo_users_only
async def leave_all(client, message):
    if message.from_user.id not in OWNER_ID:
        return

    left = 0
    failed = 0
    lol = await message.reply("🔄 **userbot** leaving all chats !")
    async for dialog in USER.iter_dialogs():
        try:
            await USER.join_chat(dialog.chat.id)
            join += 1
            await lol.edit(
                f"Userbot leaving all group...\n\nLeft: {join} chats.\nFailed: {failed} chats."
            )
        except:
            failed += 1
            await lol.edit(
                f"Userbot joininh...\n\nLeft: {join} chats.\nFailed: {failed} chats."
            )
        await asyncio.sleep(0.7)
    await client.send_message(
        message.chat.id, f"✅ join to: {join} chats.\n❌ Failed in: {failed} chats."
    )
