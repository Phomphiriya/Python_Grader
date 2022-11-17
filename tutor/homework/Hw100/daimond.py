inp = int(input("Enter your number: "))
x = inp-1
y = 1
z = (2*inp-1)-2
for row in range(inp):
    for i in range(x):
        print(" ",end="")
    x -= 1
    for j in range(2*row+1):
        print("A",end="")
    print("\n")
for row2 in range(inp-1,0,-1):
    for k in range(y):
        print(" ",end="")
    y += 1
    for m in range(z):
        print("A",end="")
    z -= 2
    print("\n")
