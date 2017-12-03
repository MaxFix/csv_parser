# -*- coding=utf-8 -*-
# from __future__ import CO_FUTURE_ABSOLUTE_IMPORT

import telebot
import settings
import csv
from datetime import datetime

bot = telebot.TeleBot(settings.token)


print(bot.get_me())


class Answers(object):
    do_not_know = 'I do not know this'


def log(message, answer):
    print("\n ---------")
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст {3}"
          "".format(
                message.from_user.first_name,
                message.from_user.last_name,
                str(message.from_user.id),
                message.text))
    print(answer)


class Responser(object):

    lines = []
    data = {}

    def __init__(self, path):
        self.lines = []
        self.data = {}
        for line in csv.reader(open(path, 'r'), delimiter='—'):
            self.lines.append(line)
            print(line)
            self.data[line[0].strip().lower()] = line[1].strip().lower()

    def get_answer(self, question):
        que = question.strip().lower()
        if que in self.data.keys():
            print('Bot know: {}'.format(self.data[que]))
            return self.data[que]
        else:
            # bot.send_message(chat_id, '{}: {}'.format(Answers.do_not_know, que))

            print('Bot do not know: {}'.format(que))
            return None
            # log(message, answer)  # return default response


responser = Responser(settings.csv_file)

@bot.message_handler(commands=['help'])
def handle_message(message):
        bot.send_message(message.chat.id, "Показывается калорийность продуктов на 100 грамм веса")


@bot.message_handler(content_types=['text'])
def handle_message(message):
    log(message, None)

    answ = responser.get_answer(message.text)

    if answ:
        bot.send_message(message.chat.id, answ)
    else:
        bot.send_message(message.chat.id, '{}: {}'.format(Answers.do_not_know, message.text))


bot.polling(none_stop = True, interval=1)
