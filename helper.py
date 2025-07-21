from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

user_db = {}

async def user_verified(user_id: int) -> bool:
    return user_db.get(user_id, False)

async def verify_user_step(client, message: Message, short_url: str):
    user_db[message.from_user.id] = False
    buttons = InlineKeyboardMarkup(
        [[InlineKeyboardButton("✅ I’ve Verified", callback_data="verify_done")]]
    )
    await message.reply(
        f"🔐 Please verify yourself by visiting this link:\n{short_url}",
        reply_markup=buttons
    )

@app.on_callback_query(filters.regex("verify_done"))
async def handle_verification_done(client, callback_query):
    user_db[callback_query.from_user.id] = True
    await callback_query.message.edit("✅ Verification successful! Please resend the movie name.")
