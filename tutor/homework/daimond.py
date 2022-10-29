inp = int(input("Enter your number: "))
x = inp-1
for i in range(inp-1):
    for j in range(x):
        print(" ",end='')
    x = x-1 
    for k in range(2*i+1):
        print("*",end="")
    print("\n")
