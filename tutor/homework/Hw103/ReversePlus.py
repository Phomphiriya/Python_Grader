# การบวกเลขปกติมันง่ายไปอยากให้บวกเลขโดยการกลับค่าเลข หรือก็คือผลรวมของ A และ B แต่ตอบจากหลังมาหน้า

# Example Input/Output
# Input: 41,467
# Output: 805
# Input: 334,500
# Output: 438

def reverse_num(num):
    ans = ""
    for i in num:
        ans = i + ans
    return ans

inp = input("Enter number : ").split(",")
num1 = reverse_num(inp[0])
num2 = reverse_num(inp[1])

print(int(num1)+int(num2))

