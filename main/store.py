from config import *
from utils import *
from models import Product

index = 0 #Index of Product

products = get_products()

def keyboard_menu():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text="⏮️", callback_data="prev")
    b = types.InlineKeyboardButton(text="⏭️", callback_data="next")
    c = types.InlineKeyboardButton(text="Purchase", callback_data="buy")
    keyboard.add(a,b,c)
    return keyboard

@bot.message_handler(regexp="^🛒 Check Out")
def open_store(msg):
    "View The Store To Know What Is Going On"
                   
    # MANAGE PRODUCT SESSION TO BE A CONTINOUS CIRCLE
    global index
    product, index = get_product(products, index)

    bot.send_photo(
        msg.from_user.id,
        photo='https://ibb.co/2PnWzDc',
        caption=f"""
🎶 <b>Item: {index}</b>
💰 <b>Price: ${product['name']}</b>
--------------------
<b>Track Name:</b> {product['description']}
        """,
        parse_mode='html',
        reply_markup=keyboard_menu()
    )

    return index




# Callback Handlers
@bot.callback_query_handler(func=lambda call: True)
def callback_answer(call):
    """
    Button Response
    """
    global index

    if call.data == "prev":
        product, index = get_prev_product(products, index)

        bot.delete_message(call.message.chat.id, call.message.message_id)

        bot.send_photo(
            call.from_user.id,
            photo='https://ibb.co/2PnWzDc',
            caption=f"""
    🎶 <b>Item: {index}</b>
    💰 <b>Price: ${product['name']}</b>
    --------------------
    <b>Track Name:</b> {product['description']}
            """,
            parse_mode='html',
            reply_markup=keyboard_menu()
        )

    elif call.data == "next":
        product, index = get_next_product(products, index)

        bot.delete_message(call.message.chat.id, call.message.message_id)

        bot.send_photo(
            call.from_user.id,
            photo='https://ibb.co/2PnWzDc',
            caption=f"""
    🎶 <b>Item: {index}</b>
    💰 <b>Price: $ 20</b>
    --------------------
    <b>Track Name:</b> {product['name']}

    <b>Description:</b> {product['description']}
            """,
            parse_mode='html',
            reply_markup=keyboard_menu()
        )

    elif call.data == "buy":
        pass

    else:
        pass


    return index
