import telebot
import datetime
import os
from flask import Flask, request
from random import randint

TOKEN = '830999920:AAFyyAO5ZIJ7sYQFJGQA9QmF201KWnObHNc'
bot = telebot.TeleBot(TOKEN)
COMPLIMENTS = ["лучший", "ТОП", "ТОПЧИК", "огонь", "красавчик", "мыло", "ЛОСК", "классный", "садись на бутылку", "шутник"]
NAMES = ["Миша", "Бодя", "Люся", "Варя", "Егор", "Артём", "Даня", "Саня", "Дима", "Женя", "Андрей", "Макс", "Ваня", "Маша", "Наташа", "Настя", "ЛОСК", "ЛОСК"
    ,"Иванка", "Серёга"]
WORDS = ["че че","ты че э", "бе да ме", "ща на бутылку посажу", "копать лопать", "ха, а ты смИшной"]
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
    global NAMES
    global COMPLIMENTS

    global_bots +=1

    if message.text == "Ну че":
        bot.send_message(message.chat.id, WORDS[randint(0, len(WORDS))])
   # now = datetime.datetime.now()
   # bot.send_message(message.chat.id, str(now.minute))
    cnt_wake_up_0 = 1
    cnt_wake_up_1 = 0
    print(str(global_bots) + " ----BOTS ")
    if message.text == "/start" and boolVAR:
        i = 0
        times = [0,0,0,1,0,0,0,0,0,0,0,0]
        boolVAR = False
        boolT = True
        while True:
            now = datetime.datetime.now()
            if (int(now.minute) + 1) % 20 == 0:
                boolT = True
            if (int(now.second)% 20 == 0):
                print(str(global_bots) + ": ----BOTS \n Time: " + str(now))
            #bot.send_message(message.chat.id, str(now.hour))
            if (int(now.hour) + 3) % 24 > 7 and int(now.minute) % 20 == 0 and boolT == True:
                print("COMPLIMENTS")
                boolT = False
                bot.send_message(message.chat.id,
                                 NAMES[randint(0, len(NAMES))] + COMPLIMENTS[randint(0, len(COMPLIMENTS))])
                bot.send_message(message.chat.id,
                                 NAMES[randint(0, len(NAMES))] + COMPLIMENTS[randint(0, len(COMPLIMENTS))])
                bot.send_message(message.chat.id,
                                 NAMES[randint(0, len(NAMES))] + COMPLIMENTS[randint(0, len(COMPLIMENTS))])

            if (int(now.hour) + 3) % 24 == 23 and int(now.minute) == 0  and int(now.second) < 20 and times[0] == 0:
                print("WAKE UP")
                for _ in range(TIMES_WAKE_UP):
                    bot.send_message(message.chat.id, "РОТА ПОДЪЕМ!")
                times[0] = 0
                times[1] = 1
            if (int(now.hour) + 3 )% 24 == 10 and int(now.minute) == 46 and int(now.second) < 20 and times[1] == 1:
                print("GO TO BED")
                for _ in range(TIMES_WAKE_UP):
                    bot.send_message(message.chat.id, "РОТА ОТБОЙ!")
                times[1] = 0
                times[2] = 1
            if (int(now.hour) + 3) % 24 == 9  and int(now.minute) == 0  and int(now.second) < 20 and times[2] == 1:
                print("MORNING FOOD")
                for _ in range(TIMES_WAKE_UP):
                    bot.send_message(message.chat.id, "Утренняя ХАВКА!")
                times[2] = 0
                times[3] = 1
            if (int(now.hour) + 3) % 24 == 13 and int(now.minute) == 30 and int(now.second) < 20 and times[3] == 1:
                print("DAILY FOOD")
                for _ in range(TIMES_WAKE_UP):
                    bot.send_message(message.chat.id, "Дневная ХАВКА!")
                times[3] = 0
                times[4] = 1
            if (int(now.hour) + 3) % 24 == 16 and int(now.minute) == 30 and int(now.second) < 20 and times[4] == 1:
                print("NOT ENOUGH FOOD")
                for _ in range(TIMES_WAKE_UP):
                    bot.send_message(message.chat.id, "Недо ХАВКА!")
                times[4] = 0
                times[5] = 1
            if (int(now.hour) + 3) % 24 == 19 and int(now.minute) == 0  and int(now.second) < 20 and times[5] == 1:
                print("EVENING FOOD")
                for _ in range(TIMES_WAKE_UP):
                    bot.send_message(message.chat.id, "Вечерняя ХАВКА!")
                times[5] = 0
                times[6] = 1
            if (int(now.hour) + 3) % 24 == 21 and int(now.minute) == 0  and int(now.second) < 20 and times[6] == 1:
                print("VERY EVENING FOOD")
                for _ in range(TIMES_WAKE_UP):
                    bot.send_message(message.chat.id, "Очень вечерняя ХАВКА!")
                times[6] = 0
                times[0] = 1


if __name__ == '__main__':
    server.debug = True
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
    bot.polling(none_stop=True, interval=0)



