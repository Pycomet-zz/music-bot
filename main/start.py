from main.store import callback_answer
from config import *

def start_menu():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    a = types.InlineKeyboardButton("🛒 Check Out The MP3 Store", callback_data="store")
    b = types.InlineKeyboardButton("📞 Contact Support For Help", callback_data="help")

    keyboard.add(a,b)
    return keyboard


@bot.channel_post_handler(commands=['start'])
def startBot(msg):
    user = User(id=msg.chat.id)
    
    bot.delete_message(msg.chat.id, msg.message_id)

    bot.send_message(
        user.id,
        "<b>Welcome To The Official Telegram Mp3 🎶 Music Shop</b>",
        parse_mode='HTML',
        reply_markup=start_menu(),
    )




