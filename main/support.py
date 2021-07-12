from config import *


@bot.channel_post_handler(regexp="^📞 Contact")
def start_complaint(msg):
    "Returns a helper message"

    question = bot.send_message(
        msg.message.chat.id,
        "What can we help you do today? Please explain it to us here ...",
    )
    # question = question.wait()
    bot.delete_message(msg.message.chat.id, msg.message_id)
    
    bot.register_next_step_handler(question, send_complaint)



def send_complaint(msg):
    "Sends Complaint Message To Admin"

    # get Admin ID
    bot.send_message(
        ADMIN_ID,
        f"<b>Complaint From @{msg.from_user.username} - </b> {msg.text}",
        parse_mode='html'
    )

    bot.send_message(
        msg.chat.id,
        "<b>Succesfully sent complaint, you would be contacted by a support agent soon. Thank you for using our service!</b>",
        parse_mode='html'
    )

    