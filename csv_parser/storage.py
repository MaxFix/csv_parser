

def get_words(src):
    res = list()

    name_c = src
    symb = '.,<>!?/\[]()~_-=+`@:\'#$%^&*'

    for i in symb:
        name_c = name_c.replace(i, '')

    name_c = name_c.strip().split(" ")
    res = name_c

    return res


class Storage(object):

    def __init__(self, path):                                   # имя файла в конструкторе path
        pass

    def find_entry(self, sought_for, search_aliases=False):     # строка поиска
        res = None
        for item in Entry:                                      # item будет инстансом нового класса
            if item.name == sought_for:                         # нужно привести в одинаковый регистр
                res = item
                break
        if res:
            return res

        elif search_aliases:
            pass

        if search_aliases in self.data.keys():                            # поиск по ключу, как в Responser`e
            print('Bot know: {}'.format(self.data[search_aliases]))
            return self.data[search_aliases]
        else:
            print('Bot do not know: {}'.format(search_aliases))
            return None

    def check_aliases(self, aliases, find_str):                 # метод проверки псевдонимов (alias`ов)

        for aliases in Entry:                                   # запись из нового класса Entry, вместо строк
            if aliases == find_str:                             # если псевдоним совпадает со строкой
                find_str = True                                 # найдена верная строка
                print(find_str)
            else:
                find_str = False
                return None


class Food(object):
    def __init__(self, name, value):
        self.name = name  # ключ из 1го файла
        self.value = value  # значение из предыдущей версии
        self._init_aliases()

    def __str__(self):
        return self.name

    def _init_aliases(self):
        name_c = self.name
        symb = '.,<>!?/\[]()~_-=+`@:\'#$%^&*'

        for i in symb:
            name_c = name_c.replace(i, '')

        name_c = name_c.strip().split(" ")
        self.aliases_all = name_c

    def has_alias(self, sought):
        for s in self.aliases_all:
            if s == sought:
                return True
