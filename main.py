import telebot
import datetime
import os
from flask import Flask, request

TOKEN = '830999920:AAFyyAO5ZIJ7sYQFJGQA9QmF201KWnObHNc'
bot = telebot.TeleBot(TOKEN)

global_bots = 0
TIMES_WAKE_UP = 4
boolVAR = True
server = Flask(__name__)

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://evening-tor-60826.herokuapp.com/' + TOKEN)
    return "!", 200


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global global_bots
    global TIMES_WAKE_UP
    global boolVAR

    global_bots +=1

   # now = datetime.datetime.now()
   # bot.send_message(message.chat.id, str(now.minute))
    cnt_wake_up_0 = 1
    cnt_wake_up_1 = 0
    print(str(global_bots) + " ----BOTS ")
    if message.text == "/start" and boolVAR:
        i = 0
        boolVAR = False
        while True:
            now = datetime.datetime.now()
            print(str(global_bots) + ": ----BOTS \n Time: " + str(now))
            #bot.send_message(message.chat.id, str(now.hour))
            i +=1
            if (int(now.hour) + 3)% 24 == 23 and int(now.minute) == 0 and int(now.second) < 20 and cnt_wake_up_0 == 0:
                print("WAKE UP")
                for _ in range(TIMES_WAKE_UP):
                    bot.send_message(message.chat.id, "РОТА ПОДЪЕМ!")
                cnt_wake_up_0 = 1
                cnt_wake_up_1 = 0
            if (int(now.hour) + 3 )% 24 == 10 and int(now.minute) == 46 and int(now.second) < 20 and cnt_wake_up_0 == 1:
                print("GO TO BED")
                for _ in range(TIMES_WAKE_UP):
                    bot.send_message(message.chat.id, "РОТА ОТБОЙ!")
                cnt_wake_up_0 = 0
                cnt_wake_up_1 = 1

if __name__ == '__main__':
    server.debug = True
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
    bot.polling(none_stop=True, interval=0)



