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
WORDS = ["че че","ты че э", "бе да ме", "ща на бутылку посажу", "копать лопать", "ха, а ты смИшной", "Пац, ты не понял?", "Ой ты милаха)", "Цемик", "Лайк и подписочка", "Лайк", "Просто киця"]
GREETS = ["Приветули", "Утро утро добро", "Дароу", "Привет.", "ДАРОВА", "Хай", "А на зарядку?", "Доброе)", "Привет)", "Приветик)"]
MEMES = []
for _ in range(30):
    MEMES.append( "/Memes/"+ str(_) + ".jpg")
CUTES = ["Ты чудо)", "У тебя все выйдет", "Уряяя", "Так держать!", "Поднять щиты!!!", "Ты готов", "Если не ты, то кто?", "Герой", "3 богатыря с тобой", "Оленей больше", "Спасибо что живой"]
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


def print2(times, msg):
    print(msg)
    print(times)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global global_bots
    global TIMES_WAKE_UP
    global boolVAR
    global NAMES
    global COMPLIMENTS
    global GREETS
    global MEMES
    global CUTES

    global_bots +=1

    if message.text == "Ну че":
        bot.send_message(message.chat.id, WORDS[randint(0, len(WORDS))])

    if message.text == "Привет" or message.text == "привет" or message.text == "Прив":
        bot.send_message(message.chat.id, GREETS[randint(0, len(GREETS))])
    if message.text == "Хочу милости" or message.text == "Милость" or message.text == "Поддержки дай" or message.text == "Поддержи":
        bot.send_message(message.chat.id, CUTES[randint(0, len(CUTES))])
    if message.text == "Хочу мем" or message.text == "мем":
        if (len(MEMES) == 0):
            bot.send_message(message.chat.id, "эх, пусто...")
        else:
            photo = open(MEMES[randint(0, len(MEMES))], 'rb')
            bot.send_photo(message.chat.id, photo)
    if message.text == "на лицо пжлста":
        photo = open('food.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    # now = datetime.datetime.now()
   # bot.send_message(message.chat.id, str(now.minute))
    cnt_wake_up_0 = 1
    cnt_wake_up_1 = 0
    print(str(global_bots) + " ----BOTS ")
    if message.text == "/start" and boolVAR:
        i = 0
        times = [0,0,0,0,0,1,0,0,0,0,0,0]
        boolVAR = False
        boolT = True
        timeBool = True
        while True:
            now = datetime.datetime.now()
            if (int(now.minute) + 1) % 20 == 0:
                boolT = True
            if int(now.second) % 30 == 0 and timeBool == True:
                print(str(global_bots) + ": ----BOTS \n Time: " + str(now))
                timeBool = False
            if int(now.second) % 30 != 0 and timeBool == False:
                timeBool = True

            #bot.send_message(message.chat.id, str(now.hour))
            if (int(now.hour) + 3) % 24 > 7 and int(now.minute) % 50 == 0 and boolT == True and int(now.hour) % 2 == 0:
                print("COMPLIMENTS")
                boolT = False
                bot.send_message(message.chat.id,
                                 NAMES[randint(0, len(NAMES))] + " " + COMPLIMENTS[randint(0, len(COMPLIMENTS))])
                bot.send_message(message.chat.id,
                                 NAMES[randint(0, len(NAMES))] + " " + COMPLIMENTS[randint(0, len(COMPLIMENTS))])
                bot.send_message(message.chat.id,
                                 NAMES[randint(0, len(NAMES))] + " " + COMPLIMENTS[randint(0, len(COMPLIMENTS))])


            if (int(now.hour) + 3) % 24 == 23 and int(now.minute) == 0   and times[0] == 0:
                print("WAKE UP")
                for _ in range(TIMES_WAKE_UP):
                    bot.send_message(message.chat.id, "РОТА ПОДЪЕМ!")
                print2(times, "BEFORE: ")
                times[0] = 0
                times[1] = 1
                print2(times, "AFTER: ")
            if (int(now.hour) + 3) % 24 == 7  and int(now.minute) == 50  and times[1] == 1:
                print("GO TO BED")
                for _ in range(TIMES_WAKE_UP):
                    bot.send_message(message.chat.id, "РОТА ОТБОЙ!")
                print2(times, "BEFORE: ")
                times[1] = 0
                times[2] = 1
                print2(times, "AFTER: ")
            if (int(now.hour) + 3) % 24 == 9  and int(now.minute) == 0   and times[2] == 1:
                print("MORNING FOOD")
                for _ in range(TIMES_WAKE_UP):
                    bot.send_message(message.chat.id, "Утренняя ХАВКА!")

                print2(times, "BEFORE: ")
                times[2] = 0
                times[3] = 1
                print2(times, "AFTER: ")
                photo = open('food.jpg', 'rb')
                bot.send_photo(message.chat.id, photo)
            if (int(now.hour) + 3) % 24 == 13 and int(now.minute) == 30  and times[3] == 1:
                print("DAILY FOOD")
                for _ in range(TIMES_WAKE_UP):
                    bot.send_message(message.chat.id, "Дневная ХАВКА!")
                print2(times, "BEFORE: ")
                times[3] = 0
                times[4] = 1
                print2(times, "AFTER: ")
                photo = open('food.jpg', 'rb')
                bot.send_photo(message.chat.id, photo)
            if (int(now.hour) + 3) % 24 == 16 and int(now.minute) == 30  and times[4] == 1:
                print("NOT ENOUGH FOOD")
                for _ in range(TIMES_WAKE_UP):
                    bot.send_message(message.chat.id, "Недо ХАВКА!")
                times[4] = 0
                times[5] = 1
                photo = open('food.jpg', 'rb')
                bot.send_photo(message.chat.id, photo)
            if (int(now.hour) + 3) % 24 == 19 and int(now.minute) == 0   and times[5] == 1:
                print("EVENING FOOD")
                for _ in range(TIMES_WAKE_UP):
                    bot.send_message(message.chat.id, "Вечерняя ХАВКА!")

                print2(times, "BEFORE: ")
                times[5] = 0
                times[6] = 1
                print2(times, "AFTER: ")
                photo = open('food.jpg', 'rb')
                bot.send_photo(message.chat.id, photo)
            if (int(now.hour) + 3) % 24 == 21 and int(now.minute) == 0   and times[6] == 1:
                print("VERY EVENING FOOD")
                for _ in range(TIMES_WAKE_UP):
                    bot.send_message(message.chat.id, "Очень вечерняя ХАВКА!")
                print2(times, "BEFORE: ")
                times[6] = 0
                times[0] = 1
                print2(times, "AFTER: ")
                photo = open('food.jpg', 'rb')
                bot.send_photo(message.chat.id, photo)


if __name__ == '__main__':
    server.debug = True
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
    bot.polling(none_stop=True, interval=0)



