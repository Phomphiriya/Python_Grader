inp_stu = int(input("Enter number of student : "))
count = 0
ls_score = []
ls_check = []

while count < inp_stu:
    inp_score = input("Enter score : ")
    ls_score.append(int(inp_score))
    count += 1
print(ls_score)
for i in ls_score:
    # print(i)
    # print(type(i))
    if i >= 85:
        ls_check.append("Pefect")
    elif i >= 60:
        ls_check.append("Pass")
    else:
        ls_check.append("Not Pass")
print(ls_check)
