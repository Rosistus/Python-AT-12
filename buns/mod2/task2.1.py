import csv

print("Введите название файла")
doc = input()
with open(doc, 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    doc = list(reader)
    title = doc[0]
    content = doc[1:]
print(title)
print(content)
