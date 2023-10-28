class Node:
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None # ссылка на предыдущий узел


class Stack:

    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        try:
            val = self.end.data
            self.end = self.end.pref
            return val
        except AttributeError:
            print("Стек пуст")

    def push(self, val):
        if self.end == None:
            node = Node(val)
            self.end = node
        else:
            node = Node(val)
            node.pref = self.end
            self.end = node

    def print(self):
        item = self.end
        while item:
            print(item.data)
            item = item.pref
