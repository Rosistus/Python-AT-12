name = input()
doc = {}
with open(name, 'r', encoding='UTF-8') as file:
    text = file.read()
    file.close()

letters = set(text)
for k in letters:
    if k != "\n" and k != ' ':
        doc[k] = 0
for l in text:
    if l in doc.keys():
        doc[l] += 1

doc = sorted(doc.items(), key=lambda item: item[1])
ans = ''
for item in doc:
    ans += item[0] + ': ' + str(item[1]) + '\n'

with open('task5_asnwer.txt', 'w') as f:
    f.write(ans)

#print(ans)
