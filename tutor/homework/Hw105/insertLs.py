ls = [1,3,5,8,6,4,7]
ls_ans = ls.copy()
count = 0

for i in ls:
    pos = (2*count)+1
    if i > len(ls):
        ls_ans.insert(pos, "More Than")
    else:
        ls_ans.insert(pos, "Less Than")
    count += 1
print(ls_ans)