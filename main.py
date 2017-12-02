import telebot
import settings

bot = telebot.TeleBot(settings.token)


print(bot.get_me())


def log(message, answer):
    print("\n ---------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст {3}".format(message.from_user.first_name,
                                                                 message.from_user.last_name,
                                                                 str(message.from_user.id),
                                                                 message.text))
    print(answer)

answer = "Ты не умеешь играть в эту игру..."


class Responser(object):
    class Responser(object):
        def __init__(self):
            f = open('cal.csv')
            f.read(message)

        def get_answer(self, question):
            if question in self.data:
                return self.data[question]
            else:
                bot.send_message(message.chat.id, answer)
                log(message, answer)  # return default response

@bot.message_handler(commands=['help'])
def handle_message(message):
        bot.send_message(message.chat.id, "Я работаю!!!")


@bot.message_handler(content_types=['text'])


def handle_message(message):

    """ answer = "Ты не умеешь играть в эту игру..."
    if message.text == "шампиньоны":
        answer = "27 кал/100гр"
        bot.send_message(message.chat.id, "27 кал/100гр")
        log(message,answer)
    elif message.text == "булгур":
        answer = "342 кал/100гр"
        bot.send_message(message.chat.id, "342 кал/100гр")
        log(message,answer)
    else:
        bot.send_message(message.chat.id, answer)
        log(message,answer) """

bot.polling(none_stop = True, interval = 0)