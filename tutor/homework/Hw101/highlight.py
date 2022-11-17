# ## 1.Highlight the word (Highlight คำที่อยู่หลัง , โดยให้ตัวนั้นเป็นตัว Upper)
# ## Input: hi my name is boom,boom
# ## Output: hi my name is BOOM
# ## Input: corn it is a corn,corn
# ## Output: CORN it is a CORN

inp = input("Input : ").split(",") # hi my name is boom   boom
text = inp[0]
highlight = inp[1]
ans = ""
for i in text.split(" "):
    if i == highlight:
        ans += i.upper() + " "
    else:
        ans += i + " "
print(ans)