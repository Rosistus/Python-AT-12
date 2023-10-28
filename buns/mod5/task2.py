class Node:
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        val = self.start.data
        try:
            if self.start == self.end:
                self.start = None
                self.end = None
            else:
                self.start = self.start.nref
                self.start.pref = None
            return val
        except AttributeError:
            print("Очередь пуста")

    def push(self, val):
        node = Node(val)
        if self.start is None:
            self.start = node
            self.end = node
        else:
            node.pref = self.end
            self.end.nref = node
            self.end = node

    def insert(self, n, val):
        node = Node(val)
        if self.start is None:
            self.start = node
            self.end = node
        else:
            i = 0
            item = self.start
            while item:
                if i == n:
                    node.pref = item.pref
                    node.nref = item
                    if item.pref:
                        item.pref.nref = node
                    else:
                        self.start = node
                    item.pref = node
                    break
                item = item.nref
                i += 1
            if i == n and not item:
                self.end.next = node
                node.pref = self.end
                self.end = node


    def print(self):
        item = self.end
        while item:
            print(item.data)
            item = item.pref


que = Queue()
que.push(1)
que.push(2)
que.push(3)
que.push(4)
que.insert(2, 23)
que.print()
