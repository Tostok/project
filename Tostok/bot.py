import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('statistic/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id, 'Добро пожалавать! {0.first.name}!\nЯ -<b>{1/first_name}<b>, бот созданый чтобы быть подопытным кроликом.'.format(message.from_user, bot.get_me()),
                     parse_mode='html')




@bot.message_handler(content_types=["text"])
def lalala(message):
    bot.send_message(message.chat.id, message.text)
    
#run
bot.polling(none_stop=True)