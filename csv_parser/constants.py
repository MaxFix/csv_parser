# -*- coding=utf-8 -*-

SESSIONS_MAX_COUNT = 1000   # count of available sessions
SESSION_TTL = 10            # time to live for complex requests

CANCEL = -1


class Answers(object):
    dnt_know = 'Я не знаю такой продукт'
    select_one = 'Выбирите один вариант'
