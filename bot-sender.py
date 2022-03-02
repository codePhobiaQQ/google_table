import telebot
import config
import google_table_parcer
import time
import datetime
import pytz
import schedule

bot = telebot.TeleBot(config.TOKEN)


def sending_message():
    print('бот попал во временной промежуток')
    resp = google_table_parcer.start_parce()

    result = resp["values"]

    findIndex = -1

    for i in range(0, len(result) - 1):
        if result[i][3] == "" or result[i][4] == "" or result[i][6] == "" or result[i][8] == "" or result[i][-1] == "":
            findIndex = i
            break

    # print(findIndex)
    # print(result[findIndex - 1])

    if result[findIndex - 1][3] != "" and result[findIndex - 1][4] != "" and result[findIndex - 1][6] != "" and result[findIndex - 1][8] != "" and result[findIndex - 1][-1] != "":
        text = f'Интервал: {result[findIndex - 1][2]} \nВсего голосов: {result[findIndex - 1][3]} \nПрирост: {result[findIndex - 1][4]} \nЗа: {result[findIndex - 1][6]} \nПротив: {result[findIndex - 1][8]} \nКоличество красных проектов: {result[findIndex - 1][-1]} \n---------------------'
        bot.send_message(config.TEST_CHAT_ID, text)


@bot.message_handler(commands=['start_bot'])
def start_bot(message):
    print('бот был запущен')
    # isAdmin = message.from_user.id;
    # if str(isAdmin) == str(config.MY_ID):


    schedule.every().days.at('07:20').do(sending_message)
    schedule.every().days.at('09:20').do(sending_message)
    schedule.every().days.at('11:20').do(sending_message)
    schedule.every().days.at('13:20').do(sending_message)
    schedule.every().days.at('15:20').do(sending_message)


    while True:
        schedule.run_pending()



if __name__ == '__main__':
    bot.polling()