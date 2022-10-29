inp = int(input("Enter your number: "))
n = inp
i = inp-3
for row in range(inp):
    print(" "*i,end="")
    i -= 1
    for column in range(row+1):
        print("*",end="")
    print("\n")
# x = inp-1
# for i in range(inp-1):
#     for j in range(x):
#         print(" ",end='')
#     x = x-1 
#     for k in range(2*i+1):
#         print("*",end="")
#     print("\n")


