from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
from database.users_chats_db import db
from info import SUPPORT_CHAT
from aiohttp import web
from utils import temp


routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response(text="Hosted On @StealthRDP™")

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

async def banned_users(_, client, message: Message):
    return (message.from_user is not None or not message.sender_chat) and (message.from_user.id in temp.BANNED_USERS)

async def disabled_chat(_, client, message: Message):
    return message.chat.id in temp.BANNED_CHATS

@Client.on_message(filters.private & filters.incoming & filters.create(banned_users))
async def ban_reply(bot, message):
    ban = await db.get_ban_status(message.from_user.id)
    await message.reply(f"Sorry {mention}, You Are Banned To Use Me. \nBan Reason: {ban['ban_reason']}")

@Client.on_message(filters.group & filters.incoming & filters.create(disabled_chat))
async def grp_bd(bot, message):
    buttons = [[InlineKeyboardButton('Support', url=f'https://t.me/{SUPPORT_CHAT}')]]
    chat = await db.get_chat(message.chat.id)
    k = await message.reply(text=f"CHAT NOT ALLOWED 🐞\n\nMy Admins Has Restricted Me From Working Here! If You Want To Know More About It Please Ask In @TheMovieSharingChat..\nReason : <code>{chat['reason']}</code>.", reply_markup=InlineKeyboardMarkup(buttons))
    try: await k.pin()
    except: pass
    await bot.leave_chat(message.chat.id)
