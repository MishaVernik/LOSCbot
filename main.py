import telebot
import datetime

bot = telebot.TeleBot('830999920:AAFyyAO5ZIJ7sYQFJGQA9QmF201KWnObHNc')
global_bots = 0
TIMES_WAKE_UP = 2

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global global_bots
    global TIMES_WAKE_UP
    global_bots +=1

    now = datetime.datetime.now()
    bot.send_message(message.chat.id, str(now.hour))
    if message.text == "/start" and global_bots == 1:
        i = 0
        while True:
            now = datetime.datetime.now()
            #bot.send_message(message.chat.id, str(now.hour))
            i +=1
            if (int(now.hour) + 3 )% 24 == 0 and int(now.minute) %2 == 1 and int(now.second) < 20:
                print("OKAY")
                for _ in range(TIMES_WAKE_UP):
                    bot.send_message(message.chat.id, "РОТА ПОДЪЕМ!")
            if (int(now.hour) + 3 )% 24 == 1 and int(now.minute) %2 == 0 and int(now.second) < 20:
                for _ in range(TIMES_WAKE_UP):
                    bot.send_message(message.chat.id, "РОТА ОТБОЙ!")

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
