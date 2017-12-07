# -*- coding=utf-8 -*-
from __future__ import absolute_import

import telebot
import csv
from datetime import datetime

import settings
from constants import Answers
from csv_parser.exceptions import Cancel, MissIndex

bot = telebot.TeleBot(settings.token)
print(bot.get_me())


def log(message, answer):
    print('\n{}'.format("-"*50))
    print(datetime.now())
    print("Сообщение от {0} {1} (id = {2})\nchat: {3}\nТекст: {4}"
          "".format(
                message.from_user.first_name,
                message.from_user.last_name,
                message.from_user.id,
                message.chat.id,
                message.text))
    # print('Ответ: {}'.format(answer))


class Responser(object):

    lines = []
    data = {}

    def __init__(self, path):
        # TODO this logic will be moved to separated class
        self.lines = []
        self.data = {}
        for line in csv.reader(open(path, 'r', encoding='utf-8'), delimiter='—'):
            self.lines.append(line)
            print(line)
            self.data[line[0].strip().lower()] = line[1].strip().lower()

    def get_answer(self, question, *args, **kwargs):
        que = question.strip().lower()
        if que in self.data.keys():
            print('Bot know: {}'.format(self.data[que]))
            return self.data[que]
        else:
            # bot.send_message(chat_id, '{}: {}'.format(Answers.dnt_know, que))

            print('Bot do not know: {}'.format(que))
            return None
            # log(message, answer)  # return default response


responser = Responser(path=settings.csv_file)
len(responser.lines)


@bot.message_handler(commands=['start'])
def handle_message(message):
        bot.send_message(message.chat.id, "Показывается калорийность продуктов "
                                          "на 100 грамм веса.\n"
                                          "Введитите команду /help для получения"
                                          " подсказок по использованию")


@bot.message_handler(commands=['help'])
def handle_message(message):
        bot.send_message(message.chat.id, "Введите названия продукта для "
                                          "которого нужно узнать каллорийность")


@bot.message_handler(content_types=['text'])
def handle_message(message):
    log(message, None)

    try:
        answ = responser.get_answer(message.text, message.chat.id)
    except (Cancel, MissIndex):
        return

    if answ:
        bot.send_message(message.chat.id, answ)
    else:
        bot.send_message(message.chat.id,
                         '{}: {}'.format(Answers.dnt_know, message.text))

