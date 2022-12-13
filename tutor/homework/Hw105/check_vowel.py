ls = ["boom","wow","prt","gty","sawas"]
vowel = ["a","e","i","o","u"]
ls_ans = []
check = False

for i in ls:
    check = False
    for k in vowel:
        if k in i:
            check = True
    if check == True:
        ls_ans.append("Have")
    else:
        ls_ans.append("Dont have")
print(ls_ans)
