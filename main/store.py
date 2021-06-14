from config import *


@bot.message_handler(regexp="^🛒 Check Out")
def open_store(msg):
    "View The Store To Know What Is Going On"

    # MANAGE PRODUCT SESSION TO BE A CONTINOUS CIRCLE

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text="⏮️", callback_data="prev")
    b = types.InlineKeyboardButton(text="⏭️", callback_data="next")
    c = types.InlineKeyboardButton(text="Buy", callback_data="buy")
    keyboard.add(a,b,c)

    bot.send_message(
        msg.from_user.id,
        """
🎶 <b>Item: 1</b>
--------------------
<b>Track Name:</b> Blur Musical
        """,
        file=f'files/music.png',
        parse_mode='html',
        reply_markup=keyboard
    )
