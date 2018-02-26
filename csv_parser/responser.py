# -*- coding=utf-8 -*-

from cachetools import TTLCache
from csv_parser.exceptions import Cancel, MissIndex

import constants
from constants import Answers


class Session(object):
    pass


class PollSession(Session):
    variants = None

    def __init__(self, variants):
        self.variants = variants

    def is_choose(self, request):
        if str(request).isdigit():
            try:
                index = int(request)
            except ValueError:
                return False

            available = list(range(len(self.variants)+1))

            if index in available:
                return True
            else:
                raise MissIndex()

        return False

    def get_choose(self, request):
        index = int(request)

        print(request)
        if index == 0:
            raise Cancel()
        else:
            return self.variants[index-1]

    def get_answer(self, request):
        if self.is_choose(request):
            return self.get_choose(request)
        else:
            return None


class Responser(object):

    lines = []
    data = {}

    sessions = None

    def __init__(self, csv_path=None):
        self.sessions = \
            TTLCache(constants.SESSIONS_MAX_COUNT, ttl=constants.SESSION_TTL)

        # TODO fill this code when storage will be implemented
        # self.storage = Storage(csv_path=csv_path)

        # TODO remove this monkey patch code
        self.storage = type('Storage', (), dict(find=lambda x, y: None))
        self.storage.find_mock = lambda x, y: ['Apple', 'Applet', 'Appolo']

    def get_answer(self, question, chat_id):
        request = question.strip().lower()

        answ = None
        if chat_id in self.sessions.keys():
            session = self.sessions[chat_id]

            try:
                answ = session.get_answer(request)
            except Cancel as e:
                del self.sessions[chat_id]
                raise e

            del self.sessions[chat_id]

        if not answ:
            result = self.storage.find_mock(request, True)

            if not result:
                return None

            elif isinstance(result, list):
                try:
                    del self.sessions[chat_id]
                except KeyError:
                    print("That key does not exist")

                self.sessions[chat_id] = PollSession(result)

                answ = self.make_poll_answer(result)
                return answ

            else:
                return result
        else:
            return answ

    def make_poll_answer(self, options):
        lines = []
        for i in range(len(options)):
            lines.append('{}. {}'.format(str(i+1).ljust(2), str(options[i])))

        answ = '\n'.join(lines)
        answ = '{}\n0. {}'.format(answ, 'Отмена')
        answ = '{}\n\n{}'.format(answ, Answers.select_one)

        return answ
