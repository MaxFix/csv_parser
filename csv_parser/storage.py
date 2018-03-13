import csv

class Storage(object):

    data = {}

    def __init__(self, path):
        # TODO this logic will be moved to separated class

        for foo in csv.reader(open(path, 'r', encoding='utf-8'), delimiter='—'):
            food = Food(foo[0].strip().lower(), foo[1].strip().lower())
            self.data[food.name.lower()] = food

    def find_entry(self, sought_for, search_aliases=False):     # строка поиска
        """
        :param sought_for: Искомое
        :param search_aliases: флаг, показывает нужно ли искать в алиасах
        :return:
        """
        # res = None
        # for item in Food:                                      # item будет инстансом нового класса
        #     if item.name == sought_for:                         # нужно привести в одинаковый регистр
        #         res = item
        #         break
        # if res != item: #?
        #     return
        try:
            res = self.data[sought_for.lower().strip()]
        except KeyError:
            res = None

        al_res = []
        if search_aliases == True:  # условие не полное, нужно дополнить: ищем, если установлен флаг и не нашли res
            # искать в алиасах

            al_res = self.check_aliases(sought_for)

        return res, al_res

    def check_aliases(self, find_str, aliases):                 # метод проверки псевдонимов (alias`ов)

        for aliases in []:
            if aliases == find_str:
                find_str = True
                print(find_str)
            else:
                find_str = False
                return None            #ПЕРЕПИСАТЬ!!!
        pass


class Food(object):
    aliases_all = []
    def __init__(self, name, value):
        self.value = value  # значение из предыдущей версии
        self.name = name  # ключ из 1го файла
        self._init_aliases()

    def __str__(self):
        return self.name

    def _init_aliases(self):
        # self.name
        name = self.name.strip()
        name = self.name.split(" ")

        symb = '.,<>!?/\[]()~_-=+`@#$%^&*'
        for element in symb:
            self.name.replace(element, '')

        self.aliases_all = []
        self.aliases_all.append(name)
