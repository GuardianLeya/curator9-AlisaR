import telebot

bot = telebot.TeleBot('6897562189:AAH9JyCu-bm9tO7WlifTiYn_D10oPcaXiUs')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Hi! I`m a new bot. How can I help you?')


@bot.message_handler(commands=['abilities'])
def main(message):
    bot.send_message(message.chat.id, 'I can`t do much right now, I simply don`t know how.', parse_mode='Markdown')


@bot.message_handler(commands=['how_are_you'])
def main(message):
    bot.send_message(message.chat.id, 'I`m good, thanks! And how are you?', parse_mode='Markdown')


@bot.message_handler(commands=['i_feel_good'])
def main(message):
    bot.send_message(message.chat.id, 'That`s great! I hope you will remain good for the rest of the day.',
                     parse_mode='Markdown')


@bot.message_handler(commands=['i_feel_bad'])
def main(message):
    bot.send_message(message.chat.id, 'That`s sad. I hope you will feel better and get over your problems soon.',
                     parse_mode='Markdown')


@bot.message_handler(commands=['i_feel_ok'])
def main(message):
    bot.send_message(message.chat.id, 'That`s good enough. As they say: *"no news - good news"*.', parse_mode='Markdown')


bot.infinity_polling()
