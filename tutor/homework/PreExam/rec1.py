inp = int(input())

for row in range(inp):
    if row == 0 or row == inp-1:
        print("#"*inp,end=' ')
    else:
        print("#" + " "*(inp-2) +"#",end=' ')
    print(end="\n")