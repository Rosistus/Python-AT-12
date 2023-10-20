text = input()

bank = {}
counter = 0
answer = ''
end = ''
for key in set(text):
    if key in text:
        bank[key.lower()] = 0
    for i in text:
        if key == i.lower():
            bank[key] += 1
for key in bank.keys():
    if bank[key] % 2 != 0:
        counter += 1
        end = key
    else:
        answer += key*(bank[key]//2)
    if counter > 1:
        print('Нельзя составить полиндром')
        break
if counter < 2:
    print(answer + end + answer[::-1])
