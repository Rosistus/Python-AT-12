inp = input()
isTrue = inp.count("0") == inp.count("1")
print(("no", "yes")[isTrue])