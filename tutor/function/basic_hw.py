## Mirror
## Input: pizza
## Output: pizzazzip

inp = input("Input : ")
s1 = ""
for c in inp:
    s1 = c + s1
    # print(s1)
print(inp[:-1]+s1)


# ## 1.Highlight the word (Highlight คำที่อยู่หลัง , โดยให้ตัวนั้นเป็นตัว Upper)
# ## Input: hi my name is boom,boom
# ## Output: hi my name is BOOM
# ## Input: corn it is a corn,corn
# ## Output: CORN it is a CORN
# inp = input("Input : ").split(",")
# text = inp[0]
# highlight = inp[1]
# ans = ""
# for i in text.split(" "):
#     if i == highlight:
#         ans += i.upper() + " "
#     else:
#         ans += i + " "
# print(ans)


# ## 2.Check vowel (Make by Function)
# ## Input: Non live in Thailand and Non love Thailand
# ## Output: oieiaiaaooaia
# def checkVowel(text):
#     sym = ["a","e","i","o","u"]
#     ans = ""
#     for i in text:
#         if i in sym:
#             ans += i
#         else:
#             pass
#     return ans

# inp = input("Input : ")
# print(checkVowel(inp))
