from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import PrinceX


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ā HOW TO USE THIS BOT:

1.) First, add me to your group.
2.) Then promote me as admin and give all permissions except anonymous admin.
3.) Add @{PrinceX.ASSISTANT_NAME } to your group.
4.) Turn on the voice chat first before start to stream video.
5.) Type /vplay (reply to video) to start streaming.
6.) Type /vstop to end the video streaming.

š **note: stream & stop command can only be executed by group admin only!**

""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "š” Go Back", callback_data="cbstart")
            ],[
                InlineKeyboardButton(
                    "Dev", url=f"https://t.me/its_Prince")
            ]]
        ))


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"āØ **Hello there, I am a telegram group video streaming bot.**\n\nš­ **I was created to stream videos in group "
        f"video chats easily.**\n\nā **To find out how to use me, please press the help button below** šš»",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "ā Add me to your Group ā", url=f"https://t.me/{PrinceX.BOT_USERNAME}?startgroup=true")
            ], [
                InlineKeyboardButton(
                    "ā HOW TO USE THIS BOT", callback_data="cbguide")
            ], [
                InlineKeyboardButton(
                    "š Terms & Condition", callback_data="cbinfo")
            ], [
                InlineKeyboardButton(
                    "š¬ Group", url="https://t.me/roBots_HubSupport"),
                InlineKeyboardButton(
                    "š£ Channel", url="https://t.me/roBots_Hub")
            ], [
                InlineKeyboardButton(
                    "š©š»āš» Developer", url="https://t.me/its_Prince")
            ], [
                InlineKeyboardButton(
                    "š All Command List", callback_data="cblist")
            ]]
        ))


@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""š **Bot information !**

š¤ __This bot was created to stream video in telegram group video chats using several methods from WebRTC.__

š” __Powered by PyTgcalls the Async client API for the Telegram Group Calls, and Pyrogram the telegram MTProto API 
Client Library and Framework in Pure Python for Users and Bots.__

šØš»āš» __Thanks to the developers who participated in the development of this bot, the list of devs can be seen below:__

š©š»āāļø Ā» [Aryan](https://t.me/its_Prince)
š¤µš» Ā» [Doreamon](https://t.me/user_iz_i)
""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "š” Go Back", callback_data="cbstart")
            ]]
        ),
        disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cblist"))
async def cblist(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""š All Command List:

Ā» /vplay (reply to video or yt/live url) - to stream video
Ā» /vstop - stop the video streaming
Ā» /song (song name) - download song from YT
Ā» /vsong (video name) - download video from YT
Ā» /lyric (song name) - lyric scrapper
Ā» /vjoin - invite assistant join to your group
Ā» /vleave - order assistant leave from your group

š FUN CMD:

Ā» /asupan - check it by yourself
Ā» /chika - check it by yourself
Ā» /wibu - check it by yourself
Ā» /truth - check it by yourself
Ā» /dare - check it by yourself

š° EXTRA CMD:

Ā» /tts (reply to text) - text to speech
Ā» /alive - check bot alive status
Ā» /ping - check bot ping status
Ā» /uptime - check bot uptime status
Ā» /sysinfo - check bot system information

š” SUDO ONLY:

Ā» /rmd - remove all downloaded files
Ā» /rmw - remove all downloaded raw files
Ā» /leaveall - order assistant leave from all group
""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "š” Go Back", callback_data="cbstart")
            ]]
        ))


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
