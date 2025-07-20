from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated
from config import APPROVAL_NOTE
from database import is_premium

@Client.on_chat_member_updated(filters.group)
async def approve(bot: Client, update: ChatMemberUpdated):
    if update.new_chat_member.status == "member":
        try:
            if is_premium(update.new_chat_member.user.id):
                await bot.restrict_chat_member(
                    chat_id=update.chat.id,
                    user_id=update.new_chat_member.user.id,
                    permissions={"can_send_messages": True}
                )
                await bot.send_message(
                    chat_id=update.chat.id,
                    text=f"{update.new_chat_member.user.mention} {APPROVAL_NOTE}"
                )
        except Exception as e:
            print(f"Error approving user: {e}")
