num = input("введите число:")
print(*[bin(int(num))[2:], oct(int(num))[2:], hex(int(num))[2:]] if "." not in num else "Неверный код")