# 2.ระบบตรวจคนไข้เบื้องต้น
# ถ้าคนไข้มีไข้ >=37.5 และมีอาการไอจาม ให้ = เป็นไข้หวัดทั่วไป ให้กรอกข้อมูลคนไข้จาก input
# input มีชื่อ นามสกุล ไข้เท่าไหร่ ไอจามไหม(ให้ใช้1กับ0แทน) ใช้วรรคในการแยก แล้วเอาเข้าไปเก็บไว้ในลิสต์
# output ว่าคนไข้คนนี้เป็นไข้หวัดทั่วไปหรือไม่

inp = input("Enter input : ").split()
temp = float(inp[2])
sneeze = inp[3]

if temp >= 37.5:
    if sneeze == "1":
        print("ํYou have Flu")
    else:
        print("Normal state")
print(temp,sneeze)