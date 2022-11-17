# ## 2.Check vowel (Make by Function)
# ## Input: Non live in Thailand and Non love Thailand
# ## Output: oieiaiaaooaia

def checkVowel(text):
    sym = ["a","e","i","o","u"]
    ans = ""
    for i in text:
        if i in sym:
            ans += i
        else:
            pass
    return ans

inp = input("Input : ")
print(checkVowel(inp))