
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

with open('text.txt', mode = 'rt', encoding = 'utf-8') as MyFile:
    text = MyFile.read()


# Заполняем list необходимыми кодами ascii
MyAsc = []
for i in range(0,48):
    MyAsc.append(i)
for i in range(58,65):
    MyAsc.append(i)
for i in range(91,97):
    MyAsc.append(i)
for i in range(123,192):
    MyAsc.append(i)


#Меняем все значения на " "

for i in MyAsc:
    text = text.replace(chr(i)," ")


# Меняем '—', которого не было в таблице, двойные пробелы меняем на одиночные
text = text.replace('—'," ")
for i in range(5):
    text = text.replace("  ", " ")

text = text.strip()
print(text)

#2=================================================
#Формируем List со словами
MyList = text.split(' ')
print(MyList)

#3.1 приводим к нижнему регистру
MyList_2 = list(map(lambda x: x.lower(), MyList))
print(MyList_2)

#3.2 Лематизацйия



morph = pymorphy2.MorphAnalyzer()
NewMyList_2 = []
for i in MyList_2:
    NewMyList_2.append(morph.parse(i)[0].normal_form)
print(NewMyList_2)
#4.1 Вывести количество разных слов в тексте (set)
MyList_3 = set(MyList_2)
print(len(MyList_3))
#4.2 вывести 5 наиболее часто встречающихся слов (sort)
MyDic = {}

for i in MyList_2:
    if i in MyDic:
        MyDic[i]  += 1
    else:
        MyDic[i] = 1

a = 1
MyItog = []
for i in sorted(MyDic.items(),key=lambda x: x[1], reverse = True):
    if a < 6:
        MyItog.append(i)
        a = a + 1
    else:
        break
print(MyItog)





