class Storage(object):

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
    def __init__(self, value, name):
        self.value = value  # значение из предыдущей версии
        self.name = name  # ключ из 1го файла
        #
        self._init_aliases()

    def __str__(self):
        return self.name

    def _init_aliases(self):
        # self.name
        self.aliases_all = []
        #pos = filter(aliases_all == value , self.name)
        for pos1 in self.name:
            if pos1 != " ":
                return self.name[self.aliases_all]
        self.aliases_set = []
        #pos1 = filter(aliases_set == value , self.name)
        for pos2 in self.name:
            if pos2 = "@":
                return self.name[self.aliases_set]

row = Food('255 kcl', 'йцуццу')
print(row.value)
print(str(row))

