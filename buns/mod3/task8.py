number = input()
ans = number.replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
print(ans)