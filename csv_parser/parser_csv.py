import csv

first = True
header = None
lines = []
for line in csv.reader(open('test_csv.csv', 'r'), delimiter=':'):

        lines.append(line)
        print(line)

def search_csv(prod):
    for x in lines:
        if prod == x:
            return (prod)
        else:
            print("Пока что нет такого продукта")
