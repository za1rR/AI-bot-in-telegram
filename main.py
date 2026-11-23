import telebot
from config import TOKEN
from logic import detect
bot=telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['photo'])
def detecting(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1] 
    downloaded_file = bot.download_file(file_info.file_path) 
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    label,score = detect(file_name)
    if label == 'car':
        bot.reply_to(message, 'На картинке машина!')
    else:
        bot.reply_to(message, 'На картинке человек!')

bot.polling()