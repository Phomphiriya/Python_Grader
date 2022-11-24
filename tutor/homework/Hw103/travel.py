# ให้คำนวนค่าโดยสารจากระยะทาง อายุ และ รถเมล์คันนั้นเป็นปรับอากาศหรือไม่

# ปรับอากาศ
# 15 กิโลเมตรลงมา ราคา 15
# 16 - 30 กิโลเมตร ราคา 30
# 30 - 45 กิโลเมตร ราคา 35
# พัดลม
# 15 กิโลเมตรลงมา ราคา 8
# 16 - 30 กิโลเมตร ราคา 16
# 30 - 45 กิโลเมตร ราคา 24
# อายุ
# อายุ 0-15 ราคาลดลง 5 บาท
# อายุ 15-60 ราคาปกติ
# อายุ 60-100 ราคาลดลง 2 บาท

# ปรับอากาศ = True
# พัดลม = False

# age = อายุ
# km = ระยะทาง ใช้กิโลเมตร
# air = ปรับอากาศ
# (age,km,air)
# Example Input,Output
# Input: 12,15,True
# Output: ราคา 10

# Input: 20,40,False
# Output: ราคา 24

inp = input("Enter input : ").split(",")
age = int(inp[0])
km = int(inp[1])
air = str(inp[2])
price = 0

if air == "True":
    if km >= 30 and km <= 45:
        price = 35
    elif km >= 16 and km <= 30:
        price = 30
    elif km >= 15:
        price = 15
elif air == "False":
    if km >= 30 and km <= 45:
        price = 24
    elif km >= 16 and km <= 30:
        price = 16
    elif km >= 15:
        price = 8
if age <= 15:
    price -= 5
elif age > 60:
    price -= 2

print(price)