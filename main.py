import telebot
import datetime

bot = telebot.TeleBot('830999920:AAFyyAO5ZIJ7sYQFJGQA9QmF201KWnObHNc')
global_bots = 0
TIMES_WAKE_UP = 4

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global global_bots
    global TIMES_WAKE_UP
    global_bots +=1

    now = datetime.datetime.now()
    bot.send_message(message.chat.id, str(now.hour))
    cnt_wake_up_0 = 1
    cnt_wake_up_1 = 0
    if message.text == "/start" and global_bots == 1:
        i = 0
        while True:
            now = datetime.datetime.now()
            #bot.send_message(message.chat.id, str(now.hour))
            i +=1
            if (int(now.hour) + 3)% 24 == 0 and int(now.minute) %2 == 0 and int(now.second) < 20:
                print("OKAY")
                for _ in range(TIMES_WAKE_UP):
                    bot.send_message(message.chat.id, "РОТА ПОДЪЕМ!")
                cnt_wake_up_0 = 1
                cnt_wake_up_1 = 0
            if (int(now.hour) + 3 )% 24 == 0 and int(now.minute) %2 == 0 and int(now.second) < 20:
                print("OKAY1")
                for _ in range(TIMES_WAKE_UP):
                    bot.send_message(message.chat.id, "РОТА ОТБОЙ!")
                cnt_wake_up_0 = 0
                cnt_wake_up_1 = 1

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
