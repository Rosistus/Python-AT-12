class DoubleElement:

    data = []

    def __init__(self, *lst):
        self.data = list(lst)
        self.pos = 0

    def __next__(self):
        if len(self.data) == 0 or self.pos >= len(self.data):
            raise StopIteration
        else:

            pair = (self.data[self.pos], self.data[self.pos+1] if self.pos+1 < len(self.data) else None)
            self.pos += 2
            return pair

    def __iter__(self):
        return self


dL = DoubleElement(1, 2, 3, 4)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1, 2, 3, 4, 5)
for pair in dL:
    print(pair)
