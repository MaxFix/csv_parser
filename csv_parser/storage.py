class Storage(object):

    lines = {}

    def __init__(self, path):                               # имя файла в конструкторе path
        pass

    def find_entry(self, find_str,flag):                    # строка поиска
        self.flag = False

        for find_str in lines:

        if flag in self.data.keys():                        # поиск по ключу, как в Responser`e
            print('Bot know: {}'.format(self.data[flag]))
            return self.data[flag]
        else:
            print('Bot do not know: {}'.format(flag))
            return None

    def check_aliases(self, aliases, find_str):             # метод проверки псевдонимов

        for aliases in lines:                               # запись из словаря Storag`a
            if aliases == find_str:                         # если псевдоним совпадает со строкой
                find_str = True                             # найдена верная строка
                print(find_str)
            else:
                find_str = False
                return None


