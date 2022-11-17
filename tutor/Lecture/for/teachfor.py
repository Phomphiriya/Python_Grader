
# ans = 0
# for i in range(10,1,-2):
#     print(i)
# print(ans)

check = 0
ls = []
while check != 3:
    x = input("enter input: ")
    ls.append(x) ## append คือการเอาเข้าไปไว้ในกล่อง
    check += 1
print(ls)
print(ls[0])
for i in range(ls[0]):
    i += ls[0]


