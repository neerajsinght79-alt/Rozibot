from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID
from movie_fetcher import get_movies_from_source
from shrinkme import generate_shortlink
from helper import user_verified, verify_user_step
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import asyncio

app = Client("RoziBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.private & filters.command("start"))
async def start(client, message):
    await message.reply("👋 Hello! Send a movie name to search.")

@app.on_message(filters.group & filters.text & ~filters.edited)
async def group_movie_search(client, message: Message):
    if not message.text:
        return
    results = await get_movies_from_source(message.text)
    if not results:
        await message.reply("❌ No movies found.")
        return

    buttons = []
    for idx, result in enumerate(results, 1):
        buttons.append([
            InlineKeyboardButton(
                f"{idx}. {result['title']}",
                url=f"https://t.me/{client.me.username}?start=movie_{result['id']}"
            )
        ])

    await message.reply("🎬 Select a movie to get link:", reply_markup=InlineKeyboardMarkup(buttons))

@app.on_message(filters.private & filters.regex(r"^movie_\d+"))
async def handle_private_movie(client, message):
    movie_id = message.text.split("_", 1)[-1]
    if await user_verified(message.from_user.id):
        await message.reply_document(f"https://example.com/moviefile/{movie_id}")  # replace with actual delivery
    else:
        short_url = await generate_shortlink(message.from_user.id)
        await verify_user_step(client, message, short_url)

app.run()
