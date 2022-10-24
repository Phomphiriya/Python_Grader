class Stack:
    def __init__(self, items = None):
        if items == None:
            self.items = []
        else:
            self.items = items
    def push(self,k):
        self.items.append(k)
    def pop(self):
        self.items.pop()
    def isEmpty(self):
        return self.items == []
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)

class Queue:
    def __init__(self,items = None):
        if items == None:
            self.items = []
        else:
            self.items = items
    def enQueue(self,k):
        self.items.append(k)
    def deQueue(self):
        self.items.pop(0)
    def isEmpty(self):
        return self.items == []
    def head(self):
        return self.items[0]
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)

s = Stack()
q = Queue()
inp = input("Enter word : ")
ans = "Match"

for i in inp:
    s.push(i)
    q.enQueue(i)

for i in range(len(inp)):
    a = q.head()
    q.deQueue()
    b = s.peek()
    s.pop()
    if a == b:
        pass
    else:
        ans = "Not Match"
        break
print(ans)
