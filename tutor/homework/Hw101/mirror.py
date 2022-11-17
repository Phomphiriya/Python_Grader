## Mirror
## Input: pizza
## Output: pizzazzip

inp = input("Input : ")
s1 = ""
for c in inp:
    s1 = c + s1
    # print(s1)
print(inp[:-1]+s1)