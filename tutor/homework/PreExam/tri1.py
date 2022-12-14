inp = int(input("Enter your number :"))
a = inp
for i in range(inp):
    for j in range(a):
        print("*",end=' ')
    a -= 1
    print(end='\n')