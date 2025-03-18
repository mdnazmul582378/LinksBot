from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests

import requests
exec(requests.get("https://raw.githubusercontent.com/mdnazmul582378/LinksBot/main/utils.py").text)

bot = Client(
    "link_bot",
    api_id=25534833,
    api_hash="8ec7028f3b0871fe6f0ee68e8230e4bc",
    bot_token="7822994174:AAGoYfGvoSCPgsi6omB6hlTax2YMOCW5tRo"
)

@bot.on_message(filters.command("start"))
async def start(client, message):
    if not cached_movies:
        fetch_movies()
    data = message.text.split(" ")
    if len(data) == 2:
        movie_id = data[1]
        movie = get_movie_by_id(movie_id)
        if movie:
            text = f"""🍿 **Movie Information**  
🎬 **Title:** {movie['title']}  
📅 **Release Year:** {movie['year']}  
🎭 **Genre:** {movie['genre']}  

✅ Click the button below to download!
"""
            buttons = [[InlineKeyboardButton("📥 Download Now", url=movie["link"])]]

            if is_poster_valid(movie["poster"]):
                await client.send_photo(
                    chat_id=message.chat.id,
                    photo=movie["poster"],
                    caption=text,
                    reply_markup=InlineKeyboardMarkup(buttons),
                    protect_content=True
                )
            else:
                await message.reply_text(
                    text,
                    reply_markup=InlineKeyboardMarkup(buttons),
                    protect_content=True
                )
        else:
            await message.reply_text("❌ Movie not found.", protect_content=True)
    else:
        await message.reply_text("Send me a movie ID like: `/start movieid`", protect_content=True)

@bot.on_message(filters.command("update"))
async def update_json(client, message):
    fetch_movies()
    await message.reply_text("✅ Updated movie database from GitHub!", protect_content=True)

bot.run()
