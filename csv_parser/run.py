# -*- coding=utf-8 -*-

"""
This module is entrypoint
"""

from csv_parser.main import bot


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=1)
