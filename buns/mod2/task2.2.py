import csv

#print("Введите название файла")
#doc = input()
doc = 'vacancies2.2.csv'
dictionary = {}
contentList = [[]]
#Открытие и "очищение" файла от переносов и пробелов
with open(doc, 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    doc = list(reader)
    for i in range(len(doc)):
        for j in range(len(doc[i])):
            if doc[i][j][0] == " ":
                doc[i][j] = doc[i][j][1:]
            if doc[i][j][len(doc[i][j])-1] == " ":
                doc[i][j] = doc[i][j][:len(doc[i][j])-1]
            if "\n" in doc[i][j]:
                doc[i][j] = doc[i][j].split("\n")
    file.close()
#форматирование результата под критерии вывода
for i in range(0, len(doc[0])):
    contentList.append([])
for i in range(1, len(doc)):
    for j in range(len(doc[i])):
        contentList[j].append(doc[i][j])
for title in range(len(doc[0])):
    dictionary[doc[0][title]] = contentList[title]

#Вывод
for i in range(len(dictionary["name"])):
    for j in dictionary.keys():
        if type(dictionary[j][i]) is list:
            print(j + ": ", ", ".join(dictionary[j][i]))
        else:
            print(j + ": ", dictionary[j][i])
    print('')

