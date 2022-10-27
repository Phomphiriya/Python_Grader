# inp = int(input("Enter your Rec: "))

# for row in range(inp):
#     if row == 0 or row == inp-1:
#         print("#"*inp)
#     else:
#         print("#" + " "*(inp-2) + "#")


inp = int(input("Enter student member : "))
ans = 0
for i in range(inp):
    score = int(input("Enter Score student : "))
    ans += score
print(ans)