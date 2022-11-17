# 1.อินพุตตัวอักษรใดๆก็ได้กี่ตัวก็ได้ แล้วให้แยกเป็นตัวที่คู่ ตัวที่คี่ 
# ให้จับส่วนที่นับได้คู่มารวมกันเป็น a แล้วจับที่ที่เป็นคี่มารวมกันเป็น 
# b แล้วให้เอา a กับ b มาบวกกัน เช่น abcdef ให้ออกมาเป็น acebdf

inp=input("Enter input : ")
ls = []
str_odd = ""
str_even = ""
count = 0

for i in inp:
    ls.append(i)
# print(ls)

for k in ls:
    if count % 2 == 1:
        str_odd += k
    else:
        str_even += k
    count += 1
# print(str_even)
# print(str_odd)
print(str_even+str_odd)