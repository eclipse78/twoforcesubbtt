# (©)Codexbotz

from bot import Bot
from config import OWNER
from Data import Data
from pyrogram import filters
from pyrogram.errors import MessageNotModified
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, Message


@Bot.on_message(filters.private & filters.incoming & filters.command("getabout"))
async def _about(client: Bot, msg: Message):
    await client.send_message(
        msg.chat.id,
        Data.GETABOUT.format(client.username, OWNER),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.mbuttons),
    )


@Bot.on_message(filters.private & filters.incoming & filters.command("gethelp"))
async def _help(client: Bot, msg: Message):
    await client.send_message(
        msg.chat.id,
        "<b>How to Use this Bot</b>\n" + Data.GETHELP,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.buttons),
    )


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "getabout":
        try:
            await query.message.edit_text(
                text=Data.GETABOUT.format(client.username, OWNER),
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(Data.mbuttons),
            )
        except MessageNotModified:
            pass
    elif data == "gethelp":
        try:
            await query.message.edit_text(
                text="<b>How to Use this Bot</b>\n" + Data.GETHELP,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(Data.buttons),
            )
        except MessageNotModified:
            pass
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
