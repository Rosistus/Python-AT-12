class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None

    def push(self, val):
        node = Node(val)
        if self.start is None:
            self.start = node
        else:
            current = self.start
            while current.next is not None:
                current = current.next
            current.next = node

    def insert(self, n, val):
        node = Node(val)
        if n < 0:
            print("Ошибка - индекс меньше нуля")
            return
        elif n == 0:
            self.push(val)
        else:
            current = self.start
            for i in range(n - 1):
                if current.next is None:
                    return
                current = current.next
            node = Node(val)
            node.next = current.next
            current.next = node

    def get(self, index):
        if index < 0:
            print("Ошибка - индекс меньше нуля")
            return
        else:
            current = self.start
            for i in range(index):
                if current.next is None:
                    return None
                current = current.next
            return current.data

    def remove(self, index):
        if self.start is None:
            print("Ошибка - Список пуст")
            return
        elif index < 0:
            print("Ошибка - индекс меньше нуля")
            return
        else:
            current = self.start
            prev = None
            for i in range(index):
                if current.next is None:
                    return None
                prev = current
                current = current.next
            prev.next = current.next

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data

# lis = LinkedList()
# lis.push(1)
# lis.push(2)
# lis.push(3)
# lis.insert(2, 4)
# for i in lis:
#     print(i)
# lis.remove(1)
# for i in lis:
#     print(i)
