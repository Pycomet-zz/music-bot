from config import *
from utils import *
from models import Product
from main.support import start_complaint

index = 0  # Index of Product
payment_id = ""

products = get_products()


def keyboard_menu():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text="⏮️", callback_data="prev")
    b = types.InlineKeyboardButton(text="⏭️", callback_data="next")
    c = types.InlineKeyboardButton(text="Purchase", callback_data="buy")
    d = types.InlineKeyboardButton(text="Confirm", callback_data="confirm")
    keyboard.add(a, b, c, d)
    return keyboard

# @bot.channel_post_handler(regexp="^🛒 Check Out")
@bot.message_handler(regexp="^🛒 Check Out")
def open_store(msg):
    "View The Store To Know What Is Going On"

    # MANAGE PRODUCT SESSION TO BE A CONTINOUS CIRCLE
    global index
    product, index = get_product(products, index)
    index += 1

    bot.send_photo(
        msg.message.chat.id,
        photo='https://ibb.co/2PnWzDc',
        caption=f"""
🎶 <b>Item: {index}</b>
💰 <b>Price: ${product['metadata']['price']}</b>
--------------------
<b>Name: </b> {product['name']}
<b>Time: {product['metadata']['time']}</b>

{product['metadata']['description']}
        """,
        parse_mode='html',
        reply_markup=keyboard_menu()
    )

    bot.delete_message(msg.message.chat.id, msg.message.message_id)

    return index


# Callback Handlers
@bot.callback_query_handler(func=lambda call: True)
def callback_answer(call):
    """
    Button Response
    """
    global index
    global payment_id

    if call.data == "prev":
        product, index = get_prev_product(products, index)

        bot.delete_message(call.message.chat.id, call.message.message_id)

        bot.send_photo(
            call.message.chat.id,
            photo='https://ibb.co/vsGGbDb',
            caption=f"""
🎶 <b>Item: {index}</b>
💰 <b>Price: ${product['metadata']['price']}</b>
--------------------
<b>Name: </b> {product['name']}
<b>Time: {product['metadata']['time']}</b>

{product['metadata']['description']}
            """,
            parse_mode='html',
            reply_markup=keyboard_menu()
        )

    elif call.data == "next":
        product, index = get_next_product(products, index)

        bot.delete_message(call.message.chat.id, call.message.message_id)

        bot.send_photo(
            call.message.chat.id,
            photo='https://ibb.co/vsGGbDb',
            caption=f"""
🎶 <b>Item: {index}</b>
💰 <b>Price: ${product['metadata']['price']}</b>
--------------------
<b>Name: </b> {product['name']}
<b>Time: </b> {product['metadata']['time']}

{product['metadata']['description']}
            """,
            parse_mode='html',
            reply_markup=keyboard_menu()
        )

    elif call.data == "buy":
        # Create session and return UR
        product, index = get_next_product(products, index)

        payment_url, payment_id = buy_product(product, products[index]['price_id'])

        short_url = shortener.tinyurl.short(payment_url)

        msg = bot.send_message(
            call.message.chat.id,
            text=f"""
            
    <b>Make Your Payment Here To Receive Purchase Track</b>;
    
    {short_url}
    
You have 15 seconds before this url disappears
            """,
            parse_mode='html'
        )

        time.sleep(15)
        bot.delete_message(msg.chat.id, msg.message_id)

    elif call.data == "confirm":

        if payment_id != "":

            # confirm pay
            status = payment_status(payment_id)

            if status == False:

                bot.send_message(
                    call.message.chat.id,
                    text=f"<b>Failed Attempt! Try Again.</b>",
                    parse_mode='html'
                )

            else:
                bot.send_message(
                    call.message.chat.id,
                    text=f"<b> 🎉 Congratulations! Click the link below to download <br>{product['metadata']['location']}</br></b>",
                    parse_mode='html'
                )
        else:

            bot.send_message(
                call.message.chat.id,
                text=f"<b>Please Make Payments First</b>",
                parse_mode='html'
            )

    elif call.data == "store":

        open_store(call)

    elif call.data == "help":

        start_complaint(call)

    else:
        pass

    return index
