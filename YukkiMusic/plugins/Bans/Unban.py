from YukkiMusic import app
from pyrogram import filters
from .admin_check import authorized_users_only
from pyrogram.types import Message


@app.on_message(filters.command("unban") & ~filters.edited & ~filters.private)
@authorized_users_only
async def unban_func(_, message: Message):
    # we don't need reasons for unban, also, we
    # don't need to get "text_mention" entity, because
    # normal users won't get text_mention if the user
    # they want to unban is not in the group.
    reply = message.reply_to_message

    if reply and reply.sender_chat and reply.sender_chat != message.chat.id:
        return await message.reply_text("You cannot unban a channel")

    if len(message.command) == 2:
        user = message.text.split(None, 1)[1]
    elif len(message.command) == 1 and reply:
        user = message.reply_to_message.from_user.id
    else:
        return await message.reply_text(
            "Provide a username or reply to a user's message to unban."
        )
    try:
        mention = (await app.get_users(user)).mention
    except IndexError:
        mention = (
            message.reply_to_message.sender_chat.title
            if message.reply_to_message
            else "Anon"
        )

    msg = (
        f"**UNBanned User:** {mention}\n"
        f"**UNBanned By:** {message.from_user.mention if message.from_user else 'Anon'}\n"
    )
    await message.chat.unban_member(user)
    await message.reply_text(msg)
