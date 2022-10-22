# 60 15 (60-15)
# 45 (4-5)
# 1

inp = list(map(int,input("Enter 2 Num: ").split( )))
x = inp[0] - inp[1]
xstring = str(x)
temp = 0

for i in range(len(xstring)):
    if len(xstring) > 1:
        temp = abs(int(xstring[0]) - int(xstring[1]))
        xstring = str(temp)+xstring[2:]
        print(xstring)
