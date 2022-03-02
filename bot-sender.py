import telebot
import config
import google_table_parcer
import time

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start_bot'])
def start_bot(message):  
    isAdmin = message.from_user.id;
    if str(isAdmin) == str(config.MY_ID):
        while True:
            result = google_table_parcer.resp["values"]
            print(result)
            
            text = f'Интервал: {result[-1][2]} \nВсего голосов: {result[-1][3]} \nПрирост: {result[-1][4]} \nЗа: {result[-1][5]} \nПротив: {result[-1][7]} \nКоличество проектов: {result[-1][-1]} \n---------------------'
            bot.send_message(config.CHAT_ID, text)
            time.sleep(60 * 60 * 2) # secs x mins

if __name__ == '__main__':
    bot.infinity_polling()