class Stack:
    def __init__(self,items = None):
        if items == None:
            self.items = []
        else:
            self.items = items
    def push(self,k):
        self.items.append(k)
    def pop(self):
        self.items.pop()
    def peek(self):
        return self.items[-1]
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)

def isMatch(i,j):
    if i == "(" and j == ")":
        return True
    elif i == "{" and j == "}":
        return True
    elif i == "[" and j == "]":
        return True
    else:
        return False

inp = input("Enter bracket : ")
s = Stack()
openB = ["(","{","["]
closeB = [")","}","]"]

try:
    for i in inp:
        if i in openB:
            s.push(i)
        elif i in closeB:
            a = s.peek()
            if isMatch(a,i):
                s.pop()
        else:
            pass
    if s.isEmpty():
        print("YES")
    else:
        print("NO")
except:
    print("NO")



