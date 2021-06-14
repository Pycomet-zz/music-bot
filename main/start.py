from config import *

def start_menu():
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    a = types.KeyboardButton("🛒 Check Out The MP3 Store")
    b = types.KeyboardButton("📞 Contact Support For Help")

    keyboard.add(a,b)
    return keyboard


@bot.message_handler(commands=['start'])
def startBot(msg):

    user = User(id=msg.from_user.id)

    bot.reply_to(
        msg,
        "<b>Welcome To The Official Telegram Mp3 🎶 Music Shop</b>",
        parse_mode='HTML',
        reply_markup=start_menu(),
    )




