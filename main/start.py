from config import *

def start_menu():
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    a = types.KeyboardButton("🛒 Store")
    b = types.KeyboardButton("🛍 Orders")
    c = types.KeyboardButton("💳 Wallet")
    d = types.KeyboardButton("📞 Support")

    keyboard.add(a,b,c,d)
    return keyboard


@bot.message_handler(commands=['start'])
def startBot(msg):

    user = User(id=msg.from_user.id)

    bot.reply_to(
        msg,
        "",
        parse_mode='HTML',
        reply_markup=start_menu()
    )


