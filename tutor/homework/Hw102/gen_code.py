# 3.โค๊ดหนังสือจะประกอบด้วยตัวเลข 9 ตัว รหัส 1 ตัวและเครื่องหมายคั่นกลางอีก
# 3 ตัว (x-xxx-xxxxx-x) (9 ตัวแรกคือหมายเลข และตัวสุดท้ายคือรหัส) 
# วิธีการตั้งรหัสตัวสุดท้ายคือ ให้เอาตัวเลขจากซ้ายไปขวา คูณด้วย1,2,3,...,9 
# เอาผลรวมทั้งหมดบวกกันแล้วหารด้วย 11 แล้วเหลือเศษจึงเอามาทำเป็นรหัส 
# ถ้าเหลือเศษ 10 ให้ใช้รหัสเป็น X
# ให้พิจารณาดูว่าโค๊ดหนังสือเล่มนี้ถูกต้องไหม ถ้าถูกต้องให้เอ้าท์พุต = right แต่ถ้าไม่ถูกต้อง ให้ปริ๊นท์ออกมาเป็นค่าที่ถูกต้อง เช่น
# input = 0-670-82162-4
# output = Right
# input = 0-670-82162-0
# output = 0-670-82162-4
# input = 1-670-81162-4
# output = 1-670-81162-X

inp = input("input = ")
ans = inp[0:-2]
temp = ans.replace("-","")
count = 1
sum = 0
# print(temp)
# print(ans)

for i in range(len(temp)):
    # print(temp[i])
    sum += int(temp[i]) * count
    # print("current sum =",sum)
    count += 1
# print(sum)

print("output = ",end="")
if sum % 11 == 10:
    print(ans+"-X")
else:
    check = sum % 11
    check_ans = str(ans)+"-"+str(check)
    if check_ans == inp:
        print("right")
    else:
        print(check_ans)
